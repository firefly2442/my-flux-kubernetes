# Headlamp

Headlamp is a Kubernetes web-ui similar to Rancher Dashboard, the official
Kubernetes Dashboard, and others.

Headlamp require some manual tweaks in the provider in Authentik.
Go into the provider itself, `headlamp-oauth2` and set the Signing Key
to be the self-signed Authentik certificate.

## Links

* [https://headlamp.dev/](https://headlamp.dev/)
