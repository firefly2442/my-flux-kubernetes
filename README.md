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

* [home-ops](https://github.com/onedr0p/home-ops)
* [flux Github](https://github.com/fluxcd/flux2)
* [flux](https://fluxcd.io/)
* [Tutorial on Flux](https://anaisurl.com/full-tutorial-getting-started-with-flux-cd/)
* [TechnoTim Tutorial on Flux](https://technotim.live/posts/flux-devops-gitops/)
* [renovate Github](https://github.com/renovatebot/renovate)
* [TechnoTime Tutorial on Renovate](https://technotim.live/posts/renovate-bot-kubernetes/)
* [My Renovate Developer Profile](https://developer.mend.io/github/firefly2442)
