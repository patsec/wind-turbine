# Wind Turbine Model

This repo contains the relevant Docker and [OT-sim](https://github.com/patsec/ot-sim) configuration files required to simulate the control portion of a wind turbine. The turbine controls represented in this model are simplistic, and are meant to provide useful examples of how control devices exchange data with each other using industrial protocols and operate on the data accordingly.

## Getting Started

This project was designed to be deployed using [Development Containers](https://containers.dev), such as GitHub Codespaces or locally in VS Code directly. Codespaces (free) is the recommended deployment system and is documented here.

From the main GitHub page for this [repo](https://github.com/patsec/wind-turbine), click on the green `<> Code` button and then the `Codespaces` tab. From there, click `Create codespace on main`, which will deploy a new codespace in the browser based on the `main` branch of this repo (this may take several minutes).

![](media/new-codespace.png)

Once the codespace is fully deployed, there should be (at least) four ports automatically mapped in the browser instance of VS Code.

> [!TIP]
> If you click on the Docker extension that's added to the browser instance of VS Code, you'll also be able to see when all of the containers have started.
>
> ![](media/container-list.png)

> [!NOTE]
> If the codespace takes more than a few minutes to come up, it may be that the codespace was deployed in a region other than `US East`, which is the only region the prebuild is available in. You can select the region to deploy the codespace to when you create a new codespace by clicking the `...` instead of `Create codespace on main` and then `+ New with options...`.
>
> ![](media/new-custom-codespace.png)
>
> Or... just [click here](https://github.com/codespaces/new?repo=701012652&ref=main&hide_repo_select=true).

> [!WARNING]
> In some cases, the ports do not automatically get mapped. When this happens, the ports needed for this model (`1880, 3000, 8080, 8090`) can be manually added via the `PORTS` tab.
>
> ![](media/manual-ports.gif)

## Interacting With the Model

Once the codespace is deployed, you can access UIs for the different containers by navigating to the `PORTS` tab, hovering over the `Forwarded Address` for each port, and clicking on the `Globe` icon. This will open up the UI in a different browser tab.

> [!IMPORTANT]
> When opening the `Turbine HMI`, you will need to manually add the `/ui` path onto the end of the URL of the newly opened tab.

> [!IMPORTANT]
> When opening `Wireshark` and `Adversary`, you'll need to click on the `vnc.html` link and then `Connect` in the noVNC app.

### Traffic Analysis

The Wireshark application will automatically start when the `Wireshark` port is accessed. Select the interface that starts with `br-` and then filter on `modbus` to see all the Modbus TCP traffic being sent between the turbine controllers.

![](media/wireshark.gif)

### Adversary-in-the-Middle Attack

When the `Adversary` port is accessed, right click on the desktop and open the `Terminal` application. Maximize the terminal window and run the attack by typing `./attack.sh` in the terminal. This will start a `tmux` session with `mitmproxy` running in the left pane and `arpspoof` running in the two right panes. This attack intercepts all Modbus responses from the anemometer controller and sets the values to zero, making the main controller think their is no wind and causing it to instruct the blade controllers to feather.

![](media/aitm.gif)
