# Postgresql

Postgresql is a popular relational database.

To get the postgresql password:

```shell
kubectl get secret postgresql -n postgresql -o jsonpath="{.data.postgres-password}" | base64 -d; echo
```

Then connect via:

```shell
psql -h postgresql.homelab.rivetcode.com -U postgres
# then enter the password from above
```

## Links

* [https://www.postgresql.org/](https://www.postgresql.org/)
