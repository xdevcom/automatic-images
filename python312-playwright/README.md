# python312-playwright

Production-ready Docker image for Python automation with Playwright and Chromium.

## Base Image

- `ghcr.io/ptero-eggs/yolks:python_3.12`

## Included

- Python 3.12
- Playwright 1.61
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
docker build -t python312-playwright:1.61 .
```

## Test

```bash
docker run --rm python312-playwright:1.61 python --version
docker run --rm python312-playwright:1.61 playwright --version
docker run --rm python312-playwright:1.61 ls -1 /ms-playwright
docker run --rm python312-playwright:1.61 which ss-local
```

## Publish

```text
ghcr.io/xdevcom/python312-playwright:latest
ghcr.io/xdevcom/python312-playwright:1.61
```

## Usage

Use this image in your Pterodactyl Egg:

```text
ghcr.io/xdevcom/python312-playwright:1.61
```
