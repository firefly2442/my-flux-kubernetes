# my-flux-kubernetes

My personal Kubernetes cluster using [k3s](https://k3s.io/), [flux](https://fluxcd.io/),
[renovate](https://github.com/renovatebot/renovate), and more.

## Setup

Use [Ansible](https://github.com/firefly2442/myhomelab-ansible) to setup OS level applications,
software, and Kubernetes deployment of k3s.

```shell
# run this once at the very beginning
# Github PAT: https://github.com/settings/tokens
# full "repo" and "admin:org" permissions seemed to be sufficient
# creates the Github repo if it doesn't exist
# creates the "flux-system" namespace in our Kubernetes cluster and some pods, see: kubectl get pods -n flux-system
# https://github.com/firefly2442/my-flux-kubernetes
export GITHUB_TOKEN=secret
flux bootstrap github --token-auth --owner=firefly2442 --repository=my-flux-kubernetes --branch=master --path=clusters/home --personal --private=false
```

## Development Notes

```shell
pip3 install pre-commit
# lint and check all files
pre-commit run --all-files
```

```shell
# convert a 'ClusterIP' type to a 'LoadBalancer' type so it gets an IP address from metallb
kubectl patch svc <service-name> -n <namespace> -p '{"spec": {"type": "LoadBalancer"}}'
kubectl get svc -A
```

Cilium requires a compatible BGP router and seems pretty complicated to setup.
Metallb seems a lot easier to setup and will assign IP addresses from an available
range specified which then are routable.

To get the generated Kubernetes Dashboard token to login:

```shell
kubectl get secret admin-user-token -n kubernetes-dashboard -o jsonpath="{.data.token}" | base64 --decode
```

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

```shell
kubectl describe kustomization flux-system -n flux-system
```

Exec into a running pod:

```shell
kubectl exec -it <pod-name> -- /bin/bash
```

* [onedr0p debugging tips](https://github.com/onedr0p/cluster-template#-debugging)
* [flux troubleshooting cheatsheet](https://fluxcd.io/flux/cheatsheets/troubleshooting/)

## References

* [home-ops example](https://github.com/onedr0p/home-ops)
* [pikluster example](https://github.com/dvignoles/pikluster)
* [untouchedwagons example](https://github.com/UntouchedWagons/K3S-Cluster-Setup)
* [red-lichtie example](https://github.com/red-lichtie/homelab-cluster)
* [budimanjojo example](https://github.com/budimanjojo/home-cluster)
* [chamburr example](https://github.com/chamburr/homelab)
* [dvignoles example](https://github.com/dvignoles/pikluster/tree/main)
* [vehagn example](https://github.com/vehagn/homelab/tree/main/infra/cilium)
* [chrede88 example](https://github.com/chrede88/home-ops)
* [mischavandenburg example](https://github.com/mischavandenburg/homelab)
* [Flux Gitops Experiences](https://dvignoles.github.io/blog/post-flux-gitops/)
* [flux Github](https://github.com/fluxcd/flux2)
* [flux](https://fluxcd.io/)
* [Tutorial on Flux](https://anaisurl.com/full-tutorial-getting-started-with-flux-cd/)
* [TechnoTim Tutorial on Flux](https://technotim.live/posts/flux-devops-gitops/)
* [Github Flux and Helm Example](https://github.com/fluxcd/flux2-kustomize-helm-example)
* [renovate Github](https://github.com/renovatebot/renovate)
* [TechnoTime Tutorial on Renovate](https://technotim.live/posts/renovate-bot-kubernetes/)
* [My Renovate Developer Profile](https://developer.mend.io/github/firefly2442)
* [k3s Kubernetes](https://k3s.io/)
* [metallb with flux tutorial](https://geek-cookbook.funkypenguin.co.nz/kubernetes/loadbalancer/metallb/)
* [metallb with flux discussion](https://forum.funkypenguin.co.nz/t/metallb/1546/9)
* [awesome k8s resources](https://github.com/tomhuang12/awesome-k8s-resources)
* [awesome self-hosted resources](https://github.com/awesome-selfhosted/awesome-selfhosted)
* [migrating from metallb to cilium](https://isovalent.com/blog/post/migrating-from-metallb-to-cilium/)
