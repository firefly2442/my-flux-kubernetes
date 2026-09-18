# Birdnet-Go

Self-hosted realtime soundscape analyser for birds, bats
and other wildlife. Multi-model local AI inference, runs 24/7 as a server.

## Setup

Location is handled through two environment variables:

* `BIRDNET_LATITUDE`
* `BIRDNET_LONGITUDE`

This location helps with filtering and accurately identifying birds that are
reasonble for the area and season.

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

Then add the RTSP camera feed

```shell
urls:
    - "rtsp://admin:secret@192.168.1.111:554/cam/realmonitor?channel=1&subtype=0"
```

Save the file.

Then delete the pod and have it re-launch with the new configuration.

## Storage and Data

By default, the application will process and store data until it gets to 80% full and then
it will start to delete old recordings.  See Settings -> Audio -> Retention.

## Links

* [https://github.com/tphakala/birdnet-go](https://github.com/tphakala/birdnet-go)
* [https://truecharts.org/charts/stable/birdnet-go/](https://truecharts.org/charts/stable/birdnet-go/)
