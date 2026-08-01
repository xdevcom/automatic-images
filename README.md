# Docker Images for Pterodactyl

Repository for custom Docker images used with Pterodactyl servers.

## Images

- `ghcr.io/<your-github-username>/node22-playwright:latest`
- `ghcr.io/<your-github-username>/node22-playwright:1.62`
- `ghcr.io/<your-github-username>/python312-playwright:latest`
- `ghcr.io/<your-github-username>/python312-playwright:1.61`

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
docker-images/
├── README.md
├── .gitignore
├── node22-playwright/
│   ├── Dockerfile
│   └── README.md
├── python312-playwright/
│   ├── Dockerfile
│   └── README.md
└── .github/
    └── workflows/
        ├── node22-playwright.yml
        └── python312-playwright.yml
```
