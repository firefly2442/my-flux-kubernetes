# Traefik

Traefik is a cloud-native application proxy.  It is the default
proxy installed and use by k3s.

DNS and Fully Qualified Domain Names (FQDN):

`homelab.rivetcode.com` and `*.homelab.rivetcode.com` point to the k3s Traefik
ingress controller at `192.168.1.10`.  HAProxy on the Raspberry Pi routes traffic for the Kubernetes
control plane so that we can use `kubectl` on any machine.
This is a split-DNS setup where the DNS for rivetcode only resolves when we're on our local
network.

CloudFlare provides the DNS nameservers.  These are setup in Westhost for the `rivetcode.com`
domain name.  This way Cloudflare handles DNS, not Westhost.
We use dns01 and an API token from Cloudflare to leverage cert-manager
to request certificates and have them be properly signed.  Otherwise, we would have to
use self-signed certs which would be annoying in the web-browser.

The only service that should be setup as `LoadBalancer` is the Traefik service.  This handles
all inbound access into the cluster.  All other services should be `ClusterIP` type.

DNS on Windows can be a little annoying.  It seems to sometimes use IPv6 as the default DNS
which we're not using through OpenWRT and PiHole.  Disable IPv6 DNS through
OpenWRT -> Network -> Interfaces -> LAN -> DHCP Server -> IPv6 Settings -> Uncheck "Local IPv6 DNS server"
This seems to fix things and then allow us to use split-DNS properly and resolve our services.

## Links

* [https://traefik.io/traefik](https://traefik.io/traefik)
* [https://github.com/traefik/traefik](https://github.com/traefik/traefik)
