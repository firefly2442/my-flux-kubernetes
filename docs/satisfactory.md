# Satisfactory

Satisfactory game dedicated server.

## Setup

Networking is setup using a `LoadBalancer`.  Make sure to check
if double-NAT is setup to ensure proper port forwarding from
the external internet to the game server.

Check services

```shell
kubectl get svc -n satisfactory
```

## Links

* [https://truecharts.org/charts/stable/satisfactory/](https://truecharts.org/charts/stable/satisfactory/)
