# HelpDeskPro

A full-stack IT service desk platform for managing support tickets, users, assets, and IT operations.

## Current Status

**Phase 1 — Backend Foundation**

- FastAPI application initialized
- Health-check endpoint added
- Environment-based configuration added
- SQLAlchemy database foundation added
- Automated health-check test added

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Pytest

## Run Locally

```bash
python -m venv .venv

# Windows
.venv\\Scripts\\activate

# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
uvicorn app.main:app --reload --app-dir backend
```

Health endpoint:

`GET /api/health`

API documentation is available at `/docs` while the application is running.

## Roadmap

- [ ] User authentication and roles
- [ ] Ticket management
- [ ] Ticket comments and audit history
- [ ] IT asset management
- [ ] Employee dashboard
- [ ] IT agent dashboard
- [ ] Admin dashboard
- [ ] Automated testing and CI/CD
- [ ] Docker containerization
- [ ] Azure deployment
