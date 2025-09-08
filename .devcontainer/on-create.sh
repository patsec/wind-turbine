#!/bin/bash

apt update && apt install -y git-lfs unzip

git lfs pull

curl -L -o /tmp/opensearch.zip "https://grafana.com/api/plugins/grafana-opensearch-datasource/versions/2.13.0/download?os=linux&arch=amd64"
unzip -d configs/grafana/plugins /tmp/opensearch.zip

docker compose pull wireshark main-ctlr opensearch grafana
