# CampusLibrary Backend

Prototype FastAPI service that powers the CampusLibrary catalogue.

## Setup

```bash
cd server
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8080
```

Open `http://localhost:8080/docs` for interactive documentation.

## Running Tests

```bash
pytest
```

## Next Steps

- Replace the in-memory `ResourceService` with a persistence layer (SQLite/Postgres).
- Connect the service to the LAN crawler once it is implemented.
- Extend schemas for peer availability and download statistics.
- Add auth or moderation hooks if required by campus policy.
