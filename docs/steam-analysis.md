# steam-analysis

Downloads Steam and other videogame data and saves it in a Mongo database.

The Mongo database is accessible through the LoadBalancer IP address and port

```shell
kubectl get svc -n steam-analysis
```

Use a tool like MongoDB Compass and connect to the "192." address with TLS disabled.

## Links

* [https://github.com/carlsonp/steam-analysis](https://github.com/carlsonp/steam-analysis)
