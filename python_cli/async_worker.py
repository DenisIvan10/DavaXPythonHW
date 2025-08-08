import asyncio
from typing import Callable, Any, Dict
from models import OperationRequest
from db import Database
from logger import logger
from datetime import datetime

from services import calculate_pow, calculate_fib, calculate_fact
from cache import cache
from monitor import monitor

# Tip functie mapare
OperationFunc = Callable[..., int]

# Dictionar pentru a asocia nume cu functii
OPERATION_FUNCTIONS: Dict[str, OperationFunc] = {
    "pow": calculate_pow,
    "fib": calculate_fib,
    "fact": calculate_fact,
}

# Coada de taskuri
task_queue: asyncio.Queue = asyncio.Queue()
db = Database()

async def worker():
    logger.info("Worker async pornit.")
    while True:
        task = await task_queue.get()
        try:
            await process_task(task)
        except Exception as e:
            logger.error(f"Eroare la procesarea task-ului: {e}")
        finally:
            task_queue.task_done()

async def process_task(task: Dict[str, Any]):
    operation = task["operation"]
    args = tuple(task["args"])  

    logger.debug(f"Procesam task: {operation} {args}")

    if operation not in OPERATION_FUNCTIONS:
        raise ValueError(f"Operatie necunoscuta: {operation}")

    # Verificam in cache
    cached_result = cache.get(operation, args)
    if cached_result is not None:
        result = cached_result
        logger.info(f"Rezultat returnat din cache pentru {operation}{args}: {result}")
    else:
        func = OPERATION_FUNCTIONS[operation]
        result = func(*args)
        cache.set(operation, args, result)
        logger.info(f"Rezultat calculat: {operation}({args}) = {result}")

    # DB
    op_request = OperationRequest(
        operation=operation,
        input=str(args),
        result=str(result),
        timestamp=datetime.utcnow()
    )
    await db.insert_operation(op_request)

    # Actualizam monitorul
    monitor.update(operation)

async def start_worker():
    """Porneste workerul asincron intr-un task separat."""
    await db.initialize()
    asyncio.create_task(worker())

async def submit_task(operation: str, args: list):
    """Adauga un task in coada."""
    await task_queue.put({
        "operation": operation,
        "args": args
    })
    logger.debug(f"Task adaugat in coada: {operation} {args}")
