# Birdnet-Go

Self-hosted realtime soundscape analyser for birds, bats
and other wildlife. Multi-model local AI inference, runs 24/7 as a server.

## Setup RTSP Cameras

For the final setup, after the server is launched, shell into the running pod.

```shell
cd /config
nano config.yaml
```

Find the YAML section under

```shell
realtime:
    rtsp:
        urls:
```

Then add the camera feed

```shell
urls:
    - "rtsp://admin:secret@192.168.1.111:554/cam/realmonitor?channel=1&subtype=0"
```

Save the file.

Then delete the pod and have it re-launch with the new configuration.

## Links

* [https://github.com/tphakala/birdnet-go](https://github.com/tphakala/birdnet-go)
* [https://truecharts.org/charts/stable/birdnet-go/](https://truecharts.org/charts/stable/birdnet-go/)
