# my-flux-kubernetes

## Development Notes

## Debugging

```shell
# check the sha1 hash to whatever the latest hash is in the repo to ensure it's updating properly
kubectl get gitrepositories.source.toolkit.fluxcd.io -n flux-system
```

```shell
# watch it look for changes as the interval applies
flux get kustomizations --watch
```

```shell
# check deployments
flux -n default get hr
```

```shell
# to force a HelmRelease reconciliation, use suspend then resume
flux suspend hr my-helmrelease -n myhelmrelease-ns
flux resume hr my-helmrelease -n myhelmrelease-ns
```

https://github.com/onedr0p/cluster-template#-debugging

## References
