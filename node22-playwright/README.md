# node22-playwright

Production-ready Docker image for Node.js automation with Playwright and Chromium.

## Base Image

- `ghcr.io/parkervcp/yolks:nodejs_22`

## Included

- Node.js 22
- Playwright 1.62
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

## Build

```bash
docker build -t node22-playwright:1.62 .
```

## Test

```bash
docker run --rm node22-playwright:1.62 node -v
docker run --rm node22-playwright:1.62 npx playwright --version
docker run --rm node22-playwright:1.62 ls -1 /ms-playwright
docker run --rm node22-playwright:1.62 which ss-local
```

## Publish

```text
ghcr.io/xdevcom/node22-playwright:latest
ghcr.io/xdevcom/node22-playwright:1.62
```

## Usage

Use this image in your Pterodactyl Egg:

```text
ghcr.io/xdevcom/node22-playwright:1.62
```
