import asyncio
import click
import os

import questionary

from async_worker import start_worker, submit_task
from logger import logger
from auth import check_auth
from db import Database


# Grup principal Click
@click.group()
def cli():
    """Microserviciu CLI pentru operatii matematice asincrone."""
    logger.info("CLI pornit.")

@cli.command()
@click.option('--base', required=True, type=int, help="Baza pentru operatia pow")
@click.option('--exp', required=True, type=int, help="Exponentul pentru operatia pow")
def pow(base, exp):
    """Calculeaza baza la puterea exponentului."""
    asyncio.run(run_cli_command("pow", [base, exp]))

@cli.command()
@click.option('--n', required=True, type=int, help="Indexul n pentru Fibonacci")
def fib(n):
    """Calculeaza al n-lea numar Fibonacci."""
    asyncio.run(run_cli_command("fib", [n]))

@cli.command()
@click.option('--n', required=True, type=int, help="Numarul pentru factorial")
def fact(n):
    """Calculeaza factorialul unui numar."""
    asyncio.run(run_cli_command("fact", [n]))

@cli.command()
def interactive():
    """Mod interactiv prietenos pentru utilizator."""
    def is_integer(val: str) -> bool:
        return val.isdigit() or (val.startswith("-") and val[1:].isdigit())

    def int_validator(message="Introdu un numar intreg valid!"):
        return lambda val: True if is_integer(val) else message

    operation = questionary.select(
        "Alege operatia matematica:",
        choices=["pow", "fib", "fact"]
    ).ask()

    args = []

    if operation == "pow":
        base = questionary.text(
            "Introdu baza:",
            validate=int_validator()
        ).ask()
        exp = questionary.text(
            "Introdu exponentul:",
            validate=int_validator()
        ).ask()
        args = [int(base), int(exp)]

    elif operation == "fib":
        n = questionary.text(
            "Introdu indexul n pentru Fibonacci:",
            validate=int_validator()
        ).ask()
        args = [int(n)]

    elif operation == "fact":
        n = questionary.text(
            "Introdu numarul pentru factorial:",
            validate=int_validator()
        ).ask()
        args = [int(n)]

    asyncio.run(run_cli_command(operation, args))


async def run_cli_command(operation: str, args: list):
    token = os.getenv("AUTH_TOKEN", "")
    if not check_auth(token):
        click.echo("Eroare: acces neautorizat. Seteaza AUTH_TOKEN corect.")
        return
    
    await start_worker()
    await submit_task(operation, args)

    # Pauza scurta pentru a permite workerului sa proceseze
    await asyncio.sleep(1)

    logger.info(f"Cerere procesata: {operation} {args}")

    # Afisam rezultatul din baza de date
    db = Database()
    result_message = await db.get_last_result(operation, str(tuple(args)))
    click.echo(result_message)

if __name__ == "__main__":
    cli()
