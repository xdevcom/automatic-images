FROM ghcr.io/parkervcp/yolks:nodejs_22

USER root

WORKDIR /home/container

ENV PLAYWRIGHT_BROWSERS_PATH=/ms-playwright

RUN apt-get update && apt-get install -y --no-install-recommends \
    shadowsocks-libev \
    curl \
    wget \
    unzip \
    jq \
    dnsutils \
    iproute2 \
    iputils-ping \
    ca-certificates && \
    rm -rf /var/lib/apt/lists/*

RUN npm install -g playwright@1.62.0

RUN PLAYWRIGHT_BROWSERS_PATH=/ms-playwright \
    npx playwright install --with-deps chromium

RUN chmod -R 755 /ms-playwright

USER container

CMD ["/entrypoint.sh"]
