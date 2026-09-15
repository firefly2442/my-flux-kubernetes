# Volcano

Volcano is a cloud-native batch system for distributing workloads.  It has
an accompanying dashboard to show jobs and workloads.

## Debugging

To force a restart of the dashboard deployment

```shell
kubectl rollout restart deployment/volcano-dashboard -n volcano-system
```

The web-ui dashboard does not yet have a Helm chart.
[This Github issue](https://github.com/volcano-sh/dashboard/issues/176) outlines
the request and a potential implementation.
See [this folder](https://github.com/volcano-sh/dashboard/tree/main/deployment)
for manually deploying the pieces needed in Kubernetes.

## Links

* [https://github.com/volcano-sh/volcano](https://github.com/volcano-sh/volcano)
* [https://github.com/volcano-sh/dashboard](https://github.com/volcano-sh/dashboard)
