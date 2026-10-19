# opencode

Opencode is setup with the integrated web server.
See also the `vscode` namespace and deployment
which uses the same base image.

## Usage

Store files in
`/config/projects` to persist them.

Copy files from the local machine into the running pod

```shell
kubectl get pods -n opencode

kubectl cp <local-path> <namespace>/<pod-name>:<remote-path>

kubectl cp ~/src/chromadb-photo-organizer opencode/opencode-docker-vscode-customized-59658fdd69-s9k7j:/config/projects/chromadb-photo-organizer
```

## Sandbox

Most egress traffic is blocked out of the pod.  Ingress traffic through the Traefik
ingress controller is the only way in.  Pod security standards are enforced.
The only way to get data in and out is via `kubectl cp`.

## Links

* [https://opencode.ai/docs/web/](https://opencode.ai/docs/web/)
* [https://github.com/anomalyco/opencode](https://github.com/anomalyco/opencode)
