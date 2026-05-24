# Searxng

SearXNG is a free internet metasearch engine which aggregates
results from various search services and databases. Users are neither
tracked nor profiled.

## Post Setup

Manually get into the shell of the running pod and edit `/etc/searxng/settings.yml`.
Add `json` to the following section so it will be:

```shell
search:
    formats:
        - html
        - json
```

Then restart the pod.

Validate it's running and check to make sure it output JSON results

```shell
curl -s "https://searxng.homelab.rivetcode.com/search?q=test&format=json"
```

## Links

* [https://github.com/searxng/searxng](https://github.com/searxng/searxng)
* [https://docs.searxng.org/](https://docs.searxng.org/)
* [https://truecharts.org/charts/stable/searxng/](https://truecharts.org/charts/stable/searxng/)
