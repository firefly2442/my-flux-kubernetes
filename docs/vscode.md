# VSCode

This is our customized VSCode environment for doing development with
Generative AI, agents, or other sandboxed needs.
See also the `opencode` namespace and application
which uses the same image.

## Setup

`opencode` configuration is setup via a `ConfigMap`.

## Usage

Deploy and access the web-interface.  Store files in
`/config/workspace` to persist them.

Copy files from the local machine into the running pod

```shell
kubectl get pods -n vscode

kubectl cp <local-path> <namespace>/<pod-name>:<remote-path>

kubectl cp ~/src/chromadb-photo-organizer vscode/vscode-docker-vscode-customized-7c94578cb9-l6kz8:/config/projects/chromadb-photo-organizer
```

## Sandbox

Most egress traffic is blocked out of the pod.  Ingress traffic through the Traefik
ingress controller is the only way in.  Pod security standards are enforced.
The only way to get data in and out is via `kubectl cp`.

## Debugging

Exec/shell into the running pod using `k9s`.

## Links

* [https://github.com/firefly2442/docker-vscode-customized](https://github.com/firefly2442/docker-vscode-customized)
