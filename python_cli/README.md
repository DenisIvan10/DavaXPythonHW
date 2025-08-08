# Python Async Math CLI

Acest proiect este un microserviciu asincron scris in Python care permite rularea de operatii matematice precum `pow`, `Fibonacci`, `factorial` prin intermediul unei interfete de linie de comanda, folosind:

- `Click` pentru CLI si subcomenzi
- `Pydantic` pentru validare input
- `SQLite` pentru persistare asincrona
- `asyncio` pentru cozi si worker asincron
- `In-memory caching` cu TTL
- `Autentificare` simpla pe baza de token
- `Logging` in fisier si consola
- `Monitorizare` in fisier JSON
- `Interfata interactiva` pentru utilizatori non-tehnici
- `Afisarea rezultatului in consola` dupa fiecare operatie

---

## Instalare

1. Cloneaza proiectul sau descarca arhiva.
2. Instalează dependentele:
```bash
pip install -r requirements.txt
```
---

## Utilizare

- CLI clasic:
```bash
python cli.py pow --base 2 --exp 10
python cli.py fib --n 20
python cli.py fact --n 5
```

- Mod interactiv:
```bash
python cli.py interactive
```

---

## Persistenta 

- Operatiile efectuate sunt salvate in baza de date operations.db (SQLite).

---

## Monitorizare

- Statistici runtime sunt exportate automat in fisierul monitoring.json:

```json
{
  "total_requests": 6,
  "operations": {
    "pow": 2,
    "fib": 3,
    "fact": 1
  },
  "last_updated": "2025-07-16T15:34:22.987Z"
}
```

---

## Autentificare

- Pentru a executa comenzi, trebuie sa setezi variabila AUTH_TOKEN din fisierul de configurare

```bash
$env:AUTH_TOKEN="math-secret-token"
```

---

## Linting

- Proiectul respecta PEP8 si poate fi verificat cu flake8.

---

## Structura

```bash
proiectPython/
├── cli.py               # CLI principal + interactive
├── async_worker.py      # Worker async si coada taskuri
├── services.py          # Functii matematice
├── db.py                # Initializare si interactiune SQLite
├── models.py            # Modele Pydantic
├── cache.py             # Cache in-memory
├── auth.py              # Autentificare prin token
├── monitor.py           # Export JSON statistici
├── logger.py            # Configurare logging
├── config.py            # Configuratii generale
├── requirements.txt     # Dependente
├── .flake8              # Configurare linters
├── README.md            # Documentatia proiectului
└── operations.db        # Baza SQLite (generata la runtime)
```
