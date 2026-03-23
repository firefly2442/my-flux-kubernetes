# Cert Manager

Cert manager, as the name suggests, can automatically create and manage
certificates for you.  It's tied into Let's Encrypt to allow
the automatic provisioning and management of TLS certs
to allow HTTPS connectivity to applications.  Let's Encrypt has
both a staging and production server for cert creation and management.
There are quotas and limits on cert creation, particularly for production
so make sure everything works properly first.  If you overload their servers,
you get blocked.

Cloudflare provides DNS management of the `*.homelab.rivetcode.com`
domain names.  DNS registration is provided by WestHost and DNS management
is provided by Cloudflare.

The API token for Cloudflare is allowed DNS edit permissions on
only the `rivetcode.com` domain name.

## Debugging

Make sure cert-manager and sealed-secrets are working:

```shell
kubectl get sealedsecret -n cert-manager
```

Make sure the API is up and running:

```shell
cmctl check api
```

Check the cluster issuer:

```shell
kubectl describe clusterissuer cloudflare-clusterissuer
```

Check to make sure all the service secrets are available:

```shell
kubectl get secrets -n cert-manager
```

List all certificates the service is managing:

```shell
kubectl get certificate --all-namespaces
```

Describe a specific certificate from above:

```shell
kubectl describe certificate <certificate-name> -n <namespace>
```

## Links

* [https://cert-manager.io/](https://cert-manager.io/)
* [Setting up Traefik and Cert Manager](https://www.youtube.com/watch?v=vJweuU6Qrgo)
* [TechnoTim Tutorial on cert-manager and Lets Encrypt](https://www.youtube.com/watch?v=G4CmbYL9UPg)
