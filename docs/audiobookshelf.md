# Audiobookshelf

Self-hosted audiobook and podcast server.

Upload to `/audiobooks` in the pod.

Use `kubectl cp` to copy files from the local filesystem to a running pod
and thus the corresponding pvc.
For example:

```shell
kubectl cp ./ audiobookshelf-b8b8fffbb-vzlmp:/audiobooks -n audiobookshelf
```

## Links

* [https://github.com/advplyr/audiobookshelf](https://github.com/advplyr/audiobookshelf)
* [https://truecharts.org/charts/stable/audiobookshelf/](https://truecharts.org/charts/stable/audiobookshelf/)
