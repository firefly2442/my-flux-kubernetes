# opencode

Opencode is setup with the integrated web server.

## Sandbox

All egress traffic is blocked out of the pod.  Ingress traffic through the Traefik
ingress controller is the only way in.  Pod security standards are enforced.
The only way to get data in and out is via `kubectl cp`.

## Links

* [https://opencode.ai/docs/web/](https://opencode.ai/docs/web/)
