# Proxy-Wol-Redirect

Source for https://hub.docker.com/r/waaman/proxy-wol-redirect

This image provides **PWR**, a way to wake up machine hosting web services before requesting those services.

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

**USAGE**

As an example:
- the host running this container has ip 192.168.1.40.
- i set 8565 as SERVER_PORT
- i set the MAC address of the target machine i want to wake up
- i set the webui of the service this target machine offer when awake. Ex: http://192.168.1.50

Result:

When i go to http://192.168.1.40:8565:
- the magic packet is sent to the target machine MAC address
- waiting until TIMEOUT for wake up
- when wake up the HTTP request is redirected to http://192.168.1.50



