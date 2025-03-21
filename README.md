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

DNS and Fully Qualified Domain Names (FQDN):

`homelab.rivetcode.com` and `*.homelab.rivetcode.com` point to the k3s Traefik
ingress controller at `192.168.1.10`.  HAProxy on the Raspberry Pi routes traffic for the Kubernetes
control plane so that we can use `kubectl` on any machine.

CloudFlare provides the DNS nameservers.  These are setup in Westhost for the `rivetcode.com`
domain name.  This way Cloudflare handles DNS, not Westhost.
We use dns01 and an API token from Cloudflare to leverage cert-manager
to request certificates and have them be properly signed.  Otherwise, we would have to
use self-signed certs which would be annoying in the web-browser.

Secrets are managed using sealed secrets.  This way we can store the actual values
in Git and the values are decrypted upon deployment and usage.  To create new secrets:

```shell
kubectl create secret generic my-api-token \
  --namespace kube-system \
  --from-literal=api-token='MY_SECRET_TOKEN' \
  --dry-run=client -o yaml > secret.yaml
```

The above api token from Cloudflare is allowed DNS edit permissions on
only the `rivetcode.com` domain name.

This unencrypted secret then needs to be encrypted using `kubeseal`:

```shell
kubeseal --controller-namespace kube-system --controller-name sealed-secrets < secret.yaml > sealed-secret.yaml --format=yaml
```

This `sealed-secret.yaml` file can then be safely added to Flux since the only
way to get to the plaintext value is by decrypting it with the sealed secrets private key.

The private key for all sealed secrets can be exported and backed up using:

```shell
kubectl get secret -n kube-system -l sealedsecrets.bitnami.com/sealed-secrets-key -o yaml > sealed-secrets-key-backup.yaml
```

This should be secured and saved in a password manager.

When the cluster is deleted and re-instantiated from scratch, this file can be applied
using `kubectl` and then the sealed secrets pod restarted.

## Application URL List

* [Heimdall Application Portal](http://portal.homelab.rivetcode.com)
* [Homepage Portal](https://homepage.homelab.rivetcode.com)
* [Traefik Dashboard](https://traefik.homelab.rivetcode.com)
* [Authentik](https://authentik.homelab.rivetcode.com)
* [Headlamp Dashboard](https://headlamp.homelab.rivetcode.com)
* [Gitea](https://gitea.homelab.rivetcode.com)
* [Podinfo](https://podinfo.homelab.rivetcode.com)
* [Longhorn Storage](https://longhorn.homelab.rivetcode.com)
* [Kubernetes Dashboard](https://kubernetes-dashboard.homelab.rivetcode.com)
* [Gatus Service Status Dashboard](https://gatus.homelab.rivetcode.com)

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
* [Setting up Authentik Tutorial](https://www.youtube.com/watch?v=N5unsATNpJk)
* [Setting up Traefik and Cert Manager](https://www.youtube.com/watch?v=vJweuU6Qrgo)
* [Tutorial on Authentik and Traefik](https://github.com/brokenscripts/authentik_traefik)
* [Tutorial Combining Authentik and Traefik Middleware](https://www.youtube.com/watch?v=_I3hUI1JQP4)
* [TechnoTim Tutorial on cert-manager and Lets Encrypt](https://www.youtube.com/watch?v=G4CmbYL9UPg)
