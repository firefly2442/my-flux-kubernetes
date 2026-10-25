# squid-proxy

Squid Proxy routes requests only for approved domains.  This allows
for sandboxing of environments such as for agents.

## Usage

Add domain names to the `ConfigMap` file for resources that should be allowed.
Everything else by default will be blocked.  Then in the pod that needs access

```shell
export HTTPS_PROXY="http://squid-proxy-service.squid-proxy.svc.cluster.local:3128"
export HTTP_PROXY="http://squid-proxy-service.squid-proxy.svc.cluster.local:3128"
```

## Links

* [https://www.squid-cache.org](https://www.squid-cache.org)
* [https://hub.docker.com/r/ubuntu/squid](https://hub.docker.com/r/ubuntu/squid)
