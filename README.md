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

docker-compose pull main-ctlr
docker compose up -d
```

You can then access the Node-RED UI [here](http://localhost:1880/ui).

## Gitpod Deployment

This repo can alternatively be launched in
[Gitpod](https://gitpod.io/#https://github.com/patsec/wind-turbine/tree/simple).
