# steam-analysis

Downloads Steam and other videogame data and saves it in a Mongo database.

The Mongo database is accessible through the LoadBalancer IP address and port

```shell
kubectl get svc -n steam-analysis
```

Use a tool like MongoDB Compass and connect to the "192." address with TLS disabled.

## Debugging

To force a restart of the deployment

```shell
kubectl rollout restart deployment/steam-analysis-mongodb -n steam-analysis
kubectl rollout restart deployment/steam-analysis-steam-analysis-chart -n steam-analysis
```

## Links

* [https://github.com/carlsonp/steam-analysis](https://github.com/carlsonp/steam-analysis)
