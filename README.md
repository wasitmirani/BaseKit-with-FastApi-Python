# BaseKit with FastAPI

Advanced, production-ready FastAPI starter with modular architecture, SQLAlchemy ORM, Celery workers, Redis caching, WebSockets, and Alembic migrations.

## Project Structure

```
app/
├── main.py                 # Application factory and lifespan
├── api/                    # API router aggregation and shared dependencies
├── config/                 # App, auth, cache, database, queue, and service settings
├── core/                   # Settings, security, middleware, logging, DB engine
│   └── configs/db/         # SQLAlchemy Base, session helpers, init_db
├── modules/                # Domain modules (users, add your own)
│   └── users/              # controller, models, schemas, service, router
├── shared/                 # Shared exceptions, responses, pagination, validators
├── lib/                    # Integrations (email, redis, storage, sms, stripe, …)
├── services/               # App-level services (e.g. logger)
├── migrations/             # Alembic env and revision scripts
├── workers/                # Celery background tasks
├── websocket/              # WebSocket manager and routes
├── storage/                # Runtime storage (logs, private/public files)
├── templates/              # Email/HTML templates
├── static/                 # Static assets
└── tests/                  # Test suite
```

## Quick Start

### 1. Create virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # Linux/macOS
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment

```bash
cp .env.example .env
# Edit .env with your database URL, Redis, and SECRET_KEY
```

### 4. Run database migrations

```bash
alembic revision --autogenerate -m "initial"
alembic upgrade head
```

### 5. Start the server

```bash
uvicorn app.main:app --reload
```

- API docs: http://localhost:8000/api/v1/docs
- ReDoc: http://localhost:8000/api/v1/redoc
- Health check: http://localhost:8000/health

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | Health check |
| WS | `/ws/{room}` | WebSocket room |

Register domain routers on `app/api/router.py` (for example, mount `app.modules.users.router`).

## Architecture

- **Layered modules**: Add domains under `app/modules/` with `router → service → models/schemas`
- **Dependency injection**: FastAPI `Depends()` for DB sessions (`app/core/dependencies.py`, `app/core/configs/db/session.py`)
- **Standardized responses**: `{ success, message, data }` envelope in `app/shared/common/responses.py`
- **Security utilities**: JWT and password hashing in `app/core/security.py`
- **Integrations**: External clients live under `app/lib/`
- **Background jobs**: Celery workers for email and notifications

## Running Tests

```bash
pytest
```

## Running Celery Worker

```bash
celery -A app.workers.celery_app worker --loglevel=info
```

## Author

Wasit Mirani - [GitHub Profile](https://github.com/wasitmirani)

## License

This project is licensed under the MIT License - see the LICENSE file for details.
