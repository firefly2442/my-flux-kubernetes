# Metallb

Metallb is a load-balancer for Kubernetes.  Cilium is another option.

However, Cilium requires a compatible BGP router and seems pretty complicated to setup.
Metallb seems a lot easier to setup and will assign IP addresses from an available
range specified which then are routable.

## Links

* [https://metallb.io/](https://metallb.io/)
* [metallb with flux tutorial](https://geek-cookbook.funkypenguin.co.nz/kubernetes/loadbalancer/metallb/)
* [metallb with flux discussion](https://forum.funkypenguin.co.nz/t/metallb/1546/9)
* [migrating from metallb to cilium](https://isovalent.com/blog/post/migrating-from-metallb-to-cilium/)
