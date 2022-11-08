# Proxy-Wol-Redirect

Source for https://hub.docker.com/r/waaman/proxy-wol-redirect

This image provides a way to wake up machine that host web services before requesting those services.

You need to run this container on "host" mode for correctly sending the magic packet.

Environnement Variables

**SERVER_PORT**
The listening port waiting the initial HTTP request

**TIMEOUT**
Delay before timeout

**MAC**
The target MAC Address of the target machine

**REDIRECT**
The redirect URL when machine is awake.

```docker
docker run -d \
                --name pwr \
                --restart unless-stopped \
                -e TZ=Europe/Paris \
                -e SERVER_PORT=8565 \
                -e TIMEOUT=120 \
                -e MAC=52:54:00:42:35:5C \
                -e REDIRECT=http://your.awaken.service \
                --network host \
                waaman/proxy-wol-redirect:latest
```
