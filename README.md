# Automatic Images

Production-ready Docker images for Pterodactyl automation projects.

## Images

- `ghcr.io/xdevcom/node22-playwright:latest`
- `ghcr.io/xdevcom/node22-playwright:1.62`
- `ghcr.io/xdevcom/python312-playwright:latest`
- `ghcr.io/xdevcom/python312-playwright:1.61`

## Included

- Playwright
- Chromium
- `shadowsocks-libev` (`ss-local`)
- Curl
- Wget
- Unzip
- jq
- dnsutils
- iproute2
- iputils-ping
- ca-certificates

## How it works

Push to `main` and GitHub Actions will build and publish the images to GitHub Container Registry (GHCR).

## Folder structure

```text
automatic-images/
├── README.md
├── .gitignore
├── node22-playwright/
│   ├── Dockerfile
│   └── README.md
├── python312-playwright/
│   ├── Dockerfile
│   └── README.md
├── .github/
│   └── workflows/
│       ├── node22-playwright.yml
│       └── python312-playwright.yml
└── eggs/
    ├── egg-node-xdevcom.json
    └── egg-python-xdevcom.json
