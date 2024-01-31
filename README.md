# my-flux-kubernetes

## Development Notes

```shell
# check the sha1 hash to whatever the latest hash is in the repo to ensure it's updating properly
kubectl get gitrepositories.source.toolkit.fluxcd.io -n flux-system
```

```shell
# watch it look for changes as the interval applies
flux get kustomizations --watch
```

## References
