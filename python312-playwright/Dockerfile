# ghcr.io/xdevcom/python312-playwright:<playwright-version>
# One image tag = one Playwright version, with the matching Chromium build
# already downloaded. Nothing runs `playwright install` at container start —
# that's why this image exists.

ARG PLAYWRIGHT_VERSION=1.62.0

FROM ghcr.io/ptero-eggs/yolks:python_3.12

ARG PLAYWRIGHT_VERSION
ENV PLAYWRIGHT_BROWSERS_PATH=/ms-playwright \
    PIP_NO_CACHE_DIR=1 \
    PYTHONUNBUFFERED=1

USER root

# One RUN layer: pip install playwright, let Playwright install the
# Chromium binaries + most OS packages via --with-deps, then explicitly
# pin the handful of shared libs --with-deps has been observed to miss for
# the chromium_headless_shell binary (libnspr4 in particular). Belt and
# suspenders: --with-deps stays the primary mechanism so it keeps working
# across future Playwright versions, this list is just a safety net.
RUN pip install --upgrade pip \
    && pip install --no-cache-dir "playwright==${PLAYWRIGHT_VERSION}" \
    && playwright install --with-deps chromium \
    && apt-get update \
    && apt-get install -y --no-install-recommends libnspr4 libnss3 libasound2 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /root/.cache /tmp/*

# Base yolks images run as the unprivileged "container" user at runtime.
# Give it ownership of the browser directory now, as root, once.
RUN chown -R container:container /ms-playwright

USER container
WORKDIR /home/container

LABEL org.opencontainers.image.source="https://github.com/xdevcom/automatic-images" \
      org.opencontainers.image.description="Python 3.12 + Playwright ${PLAYWRIGHT_VERSION} + Chromium, prebaked, non-root runtime" \
      playwright.version="${PLAYWRIGHT_VERSION}"
