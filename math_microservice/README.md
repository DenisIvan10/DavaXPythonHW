# Math Microservice

Microserviciu Python pentru operații matematice: **putere**, **factorial**, **Fibonacci**.
- Expune o API REST
- Salvează fiecare request în SQLite
- Suportă caching, logging cu streaming simulare, autorizare (token-based)
- Arhitectură extensibilă

## Stack & Tehnologii

- **Flask** (API)
- **SQLAlchemy** (ORM, SQLite)
- **Pydantic** (validare)
- **Token-based Auth** (demo, hardcodat)
- **In-memory cache**
- **Logging**
- **Flasgger** (Swagger UI pentru documentație și testare interactivă)

## Instalare & Pornire

1. **Clonare repo / Descarcă codul**
2. **Instalează dependențele:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Pornește aplicația:**
   ```bash
   python -m app.main
   ```

## Documentație interactivă cu Swagger (Flasgger)
- Accesează în browser:
``` bash
http://localhost:5000/apidocs/
```
- Poți testa toate endpoint-urile direct din UI.
- Pentru endpoint-urile securizate, apasă pe butonul "Authorize" (lacăt dreapta sus) și introdu:
```bash
Bearer token123
```
sau
```bash
Bearer token456
```

## API Endpoints
- **POST /api/math/pow**
```json
{
  "base": 2,
  "exp": 8
}
```
- **POST /api/math/factorial**
```json
{
  "n": 5
}
```
- **POST /api/math/fibonacci**
```json
{
  "n": 10
}
```
- **GET /api/math/history**
- Returnează ultimele 100 de operații ale userului autentificat.

## Autorizare
- **Adaugă header:**
```bash
Authorization: Bearer <token>
```
- **Token-uri demo valabile:**
- token123 (user: alice@endava.com)
- token456 (user: bob@endava.com)

## Configurare
- **Poți folosi variabile de mediu pentru customizare (vezi config.py):**
- DATABASE_URL – URI SQLite custom
- CACHE_TTL – timp cache (secunde)
- LOG_STREAM_ENABLED – true/false pentru streaming loguri

## Testare
- **Testele se află în folderul tests. Rulează cu:**
```bash
pytest
```