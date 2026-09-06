# fnsm-app

Clone of the popular Friendly Neighborhood Spider-Man app from Insomniac's Marvel Spider-Man 2 — centered on Toronto, the way the in-game app is centered on New York City.

## Web app prototype

A starter web implementation now lives in `/home/runner/work/fnsm-app/fnsm-app/frontend` using Vite.

- FNSM-inspired layout shell (header, hero card, and section panels) branded for Toronto
- A crime reporting form backed by the FastAPI service, plus a live feed of reported incidents and Toronto neighbourhoods
- Frontend Dependabot updates configured in `/home/runner/work/fnsm-app/fnsm-app/.github/dependabot.yml`

## Backend API

A FastAPI service lives in `/home/runner/work/fnsm-app/fnsm-app/backend` and lets users report crimes around Toronto.

- SQLite-backed storage (SQLAlchemy models) with a small seeded dataset of sample Toronto reports
- `POST /api/crimes` to submit a report (title, description, category, neighbourhood, optional coordinates/reporter name); coordinates are validated to fall within Toronto's bounding box and categories against a fixed list
- `GET /api/crimes` to list reports, with optional `neighbourhood`/`category` filters
- `GET /api/crimes/{id}` and `PATCH /api/crimes/{id}` (status transitions) for a single report
- `GET /api/neighbourhoods` and `GET /api/categories` for the reference data used to populate the frontend's form
- Interactive API docs at `/docs` once running

### Running it locally

```bash
cd backend
python -m venv .venv
./.venv/Scripts/activate  # or `source .venv/bin/activate` on macOS/Linux
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

Then, in another terminal:

```bash
cd frontend
npm install
npm run dev
```

The frontend expects the API at `http://localhost:8000` by default (override with a `VITE_API_BASE` env var).

## Safari “Add to Home Screen” implementation

Research-backed baseline applied in `/home/runner/work/fnsm-app/fnsm-app/frontend/index.html` and `/home/runner/work/fnsm-app/fnsm-app/frontend/public/manifest.webmanifest`:

- `manifest.webmanifest` with `display: standalone`, theme/background colors, and app icons
- Apple web app meta tags (`apple-mobile-web-app-capable`, title, status bar style)
- `apple-touch-icon` link for iOS home screen icon

To fully ship this as a production-quality installable web app, host over HTTPS and add an offline-capable service worker (Safari and other browsers provide best install/PWA behavior with that setup).
