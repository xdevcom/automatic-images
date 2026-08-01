FROM ghcr.io/ptero-eggs/yolks:python_3.12

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

RUN pip install --no-cache-dir playwright==1.61.0

RUN PLAYWRIGHT_BROWSERS_PATH=/ms-playwright \
    playwright install --with-deps chromium

RUN chmod -R 755 /ms-playwright

USER container

CMD ["/entrypoint.sh"]
