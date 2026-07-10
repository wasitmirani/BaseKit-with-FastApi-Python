# BaseKit with FastAPI

Advanced, production-ready FastAPI starter with modular architecture, JWT authentication, SQLAlchemy ORM, Celery workers, Redis caching, WebSockets, and Alembic migrations.

## Project Structure

```
app/
├── main.py              # Application entry point
├── core/                # Config, security, middleware, logging
├── api/                 # API router aggregation (v1)
├── modules/             # Domain modules (auth, users, orders, products)
├── db/                  # Database base, session, migrations
├── common/              # Shared utilities, responses, pagination
├── services/            # External services (email, redis, storage, ai)
├── workers/             # Celery background tasks
├── websocket/           # WebSocket manager and routes
├── templates/           # Email/HTML templates
├── static/              # Static assets
└── tests/               # Test suite
```

## Quick Start

### 1. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Linux/macOS
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment

```bash
cp .env.example .env
# Edit .env with your database and secret key
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
- Health check: http://localhost:8000/health

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/v1/auth/register` | Register a new user |
| POST | `/api/v1/auth/login` | Login and get tokens |
| POST | `/api/v1/auth/refresh` | Refresh access token |
| GET | `/api/v1/users/me` | Get current user profile |
| GET | `/api/v1/products/` | List products |
| POST | `/api/v1/orders/` | Create an order |
| WS | `/ws/{room}` | WebSocket room |

## Architecture

- **Layered modules**: Each domain has `router → service → repository → model`
- **Dependency injection**: FastAPI `Depends()` for DB sessions and auth
- **Standardized responses**: `{ success, message, data }` envelope
- **JWT auth**: Access + refresh tokens with bcrypt password hashing
- **Background jobs**: Celery workers for email and notifications

## Running Tests

```bash
pytest
```

## Running Celery Worker

```bash
celery -A app.workers.celery_app worker --loglevel=info
```

## License

MIT
