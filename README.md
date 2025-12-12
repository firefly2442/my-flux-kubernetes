# my-flux-kubernetes

My personal Kubernetes cluster using [k3s](https://k3s.io/), [flux](https://fluxcd.io/),
[renovate](https://github.com/renovatebot/renovate), and more.

## Setup

Use [Ansible](https://github.com/firefly2442/myhomelab-ansible) to setup OS level applications,
software, and Kubernetes deployment of k3s.

When the cluster is deleted and re-instantiated from scratch, the sealed secrets backup file can be applied
using `kubectl apply -f sealed-secrets-key-backup.yaml` and then restart the `kube-system` sealed secrets pod using
something like: `kubectl delete pod sealed-secrets-f478c47cc-hcnlg -n kube-system`.  This will delete it and then it
should come right back up.

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

Next go into Longhorn and disable the plain worker nodes so no data gets stored there.  Edit the nodes then select disable scheduling
and set eviction request to true.  This will move any existing PVCs that are bound to those nodes to other nodes.

Authentik should already have initialized a username and password through the stored secret.
For the oauth2 enabled applications, make sure the client ID and client secret match what is stored
in the sealed secrets for each application.  On a fresh install, authentik will generate new
values so these may need to be overwritten.

Some applications like Headlamp require some manual tweaks to the provider in Authentik.
Go into the provider itself, for example `headlamp-oauth2` and set the Signing Key
to be the self-signed Authentik certificate.

## Development Notes

See details in `docs` folder for each service/application.

Use git pre-commit hooks:

```shell
pip3 install pre-commit
# lint and check all files
pre-commit run --all-files
# check for any updates
pre-commit autoupdate
```

## Application URL List

* [Heimdall Application Portal](http://portal.homelab.rivetcode.com)
* [Homepage Portal](https://homepage.homelab.rivetcode.com)
* [Traefik Dashboard](https://traefik.homelab.rivetcode.com)
* [Authentik](https://authentik.homelab.rivetcode.com)
* [Headlamp Dashboard](https://headlamp.homelab.rivetcode.com)
* [Gitea](https://gitea.homelab.rivetcode.com)
* [Podinfo](https://podinfo.homelab.rivetcode.com)
* [Longhorn Storage](https://longhorn.homelab.rivetcode.com)
* [Kubernetes Dashboard](https://kubernetes-dashboard.homelab.rivetcode.com) - disabled
* [Gatus Service Status Dashboard](https://gatus.homelab.rivetcode.com)
* [Prometheus Logging Dashboard](https://prometheus.homelab.rivetcode.com)
* [Grafana Dashboard](https://grafana.homelab.rivetcode.com)
* [Rabbitmq Dashboard](https://rabbitmq.homelab.rivetcode.com)
* [DefectDojo Dashboard](https://defectdojo.homelab.rivetcode.com) - disabled
* [Stirling PDF](https://stirlingpdf.homelab.rivetcode.com)
* [My Recipes](https://recipes.homelab.rivetcode.com)
* [My Boardgames](https://boardgames.homelab.rivetcode.com)
* [Data Science Tools](https://datascience.homelab.rivetcode.com)
* [Volcano Dashboard](https://volcano.homelab.rivetcode.com)
* [Photoprism](https://photoprism.homelab.rivetcode.com)
* [Vertsh](https://vertsh.homelab.rivetcode.com)
* [Excalidraw](https://excalidraw.homelab.rivetcode.com)
* [Ray Cluster Dashboard](https://kuberay.homelab.rivetcode.com)
* [Home Assistant](https://home-assistant.homelab.rivetcode.com)
* [Frigate Dashboard](https://frigate.homelab.rivetcode.com)

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

Check all kustomizations:

```shell
flux get kustomizations --all-namespaces
```

Check all Helm releases:

```shell
flux get helmrelease -A
```

Local inter-cluster networking can use .local domain so things like:

```shell
<service-name>.<namespace>.svc.cluster.local
```

Check resouce utilization:

```shell
kubectl top nodes
```

List all custom resource definitions (CRDs):

```shell
kubectl get crds
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
* [vehagn example](https://github.com/vehagn/homelab/)
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
* [awesome k8s resources](https://github.com/tomhuang12/awesome-k8s-resources)
* [awesome self-hosted resources](https://github.com/awesome-selfhosted/awesome-selfhosted)
* [hmajid2301 example](https://github.com/hmajid2301/k3s-config)
* [Christian Lempa's Boilerplates](https://github.com/ChristianLempa/boilerplates)
