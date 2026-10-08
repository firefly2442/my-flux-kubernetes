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

## Sandbox

All egress traffic is blocked out of the pod.  Ingress traffic through the Traefik
ingress controller is the only way in.  Pod security standards are enforced.
The only way to get data in and out is via `kubectl cp`.

## Debugging

Exec/shell into the running pod using `k9s`.

## Links

* [https://github.com/firefly2442/docker-vscode-customized](https://github.com/firefly2442/docker-vscode-customized)
