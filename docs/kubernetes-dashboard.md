# Kubernetes Dashboard

This is the official dashboard of Kubernetes.

To get the generated Kubernetes Dashboard token to login:

```shell
kubectl get secret admin-user-token -n kubernetes-dashboard -o jsonpath="{.data.token}" | base64 --decode
```

## Links

* [https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard/](https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard/)
