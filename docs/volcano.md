# Volcano

Volcano is a cloud-native batch system for distributing workloads.  It has
an accompanying dashboard to show jobs and workloads.

## Debugging

To force a restart of the dashboard deployment

```shell
kubectl rollout restart deployment/volcano-dashboard -n volcano-system
```

## Links

* [https://github.com/volcano-sh/volcano](https://github.com/volcano-sh/volcano)
* [https://github.com/volcano-sh/dashboard](https://github.com/volcano-sh/dashboard)
