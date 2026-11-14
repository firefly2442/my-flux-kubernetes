# gogs

Self-hosted Git service.

## Setup

If you make changes to the `ConfigMap`, shell into the running
container and then delete `/data/gogs/conf/app.ini`.  Then restart the pod
to force the init to re-create the file.

## Links

* [https://gogs.io/getting-started/introduction](https://gogs.io/getting-started/introduction)
* [https://github.com/gogs/gogs](https://github.com/gogs/gogs)
