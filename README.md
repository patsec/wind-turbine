# Wind Turbine Control Model

This repo contains the relevant Docker and
[OT-sim](https://github.com/patsec/ot-sim) configuration files required to
simulate the control portion of a wind turbine. The turbine controls represented
in this model are simplistic, and are meant to be the basis for developing a
more accurate representation of such controls.

## Getting Started

Run the following after cloning this content.

```
git lfs pull

curl -L -o /tmp/opensearch.zip "https://grafana.com/api/plugins/grafana-opensearch-datasource/versions/2.13.0/download?os=linux&arch=amd64"
unzip -d configs/grafana/plugins /tmp/opensearch.zip

docker-compose pull wireshark main-ctlr opensearch grafana
docker compose up -d
```

You can then access the Node-RED UI [here](http://localhost:1880/ui).

There is also a Grafana dashboard available
[here](http://localhost:3000/d/IUzSfUhVz/turbine).

A container running the Wireshark UI can be accessed
[here](http://localhost:8080/vnc.html).

An adversary container can be accessed [here](http://localhost:8090/vnc.html).
It contains a script, `attack.sh`, that can be run to conduct an AitM attack
against the turbine's main controller and the anemometer. This is a contrived
attack, but is a good example of AitMing the Modbus protocol none-the-less.

## Gitpod Deployment

This repo can alternatively be launched in
[Gitpod](https://gitpod.io/#https://github.com/patsec/wind-turbine).
