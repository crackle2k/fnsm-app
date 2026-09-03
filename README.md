# fnsm-app

Clone of the popular Friendly Neighborhood Spider-Man app from Insomniac's Marvel Spider-Man 2.

## Web app prototype

A starter web implementation now lives in `/home/runner/work/fnsm-app/fnsm-app/frontend` using Vite.

- Base FNSM-inspired layout shell (header, hero card, and section panels)
- Frontend Dependabot updates configured in `/home/runner/work/fnsm-app/fnsm-app/.github/dependabot.yml`

## Safari “Add to Home Screen” implementation

Research-backed baseline applied in `/home/runner/work/fnsm-app/fnsm-app/frontend/index.html` and `/home/runner/work/fnsm-app/fnsm-app/frontend/public/manifest.webmanifest`:

- `manifest.webmanifest` with `display: standalone`, theme/background colors, and app icons
- Apple web app meta tags (`apple-mobile-web-app-capable`, title, status bar style)
- `apple-touch-icon` link for iOS home screen icon

To fully ship this as a production-quality installable web app, host over HTTPS and add an offline-capable service worker (Safari and other browsers provide best install/PWA behavior with that setup).
