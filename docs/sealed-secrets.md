# Sealed Secrets

Sealed Secrets seems to be safe at least for now from the
[Bitnami reorganization and movement to private registries](https://github.com/bitnami/containers/issues/83267).

```quote
Sealed Secrets, charts-syncer and minideb remain unaffected by these changes. Container
images for those projects will continue to be released on docker.io/bitnami as usual without any modifications.
```

Sealed Secrets provides a controller for one-way encrypted secrets.  It lets us
create secrets, convert them to Sealed Secrets, and then commit and push those secrets
to public repos without fear of leaking the secret plaintext.

Secrets are managed using sealed secrets.  This way we can store the actual values
in Git and the values are decrypted upon deployment and usage.  To create new secrets:

```shell
kubectl create secret generic my-api-token \
  --namespace kube-system \
  --from-literal=api-token='MY_SECRET_TOKEN' \
  --dry-run=client -o yaml > secret.yaml
```

Unencrypted secrets can be encrypted using `kubeseal`:

```shell
kubeseal --controller-namespace kube-system --controller-name sealed-secrets < secret.yaml > sealed-secret.yaml --format=yaml
```

This `sealed-secret.yaml` file can then be safely added to Flux since the only
way to get to the plaintext value is by decrypting it with the sealed secrets private key.

The private key for ALL sealed secrets can be exported and backed up using:

```shell
kubectl get secret -n kube-system -l sealedsecrets.bitnami.com/sealed-secrets-key -o yaml > sealed-secrets-key-backup.yaml
```

This should be secured and saved in a password manager.

## Links

* [https://github.com/bitnami-labs/sealed-secrets](https://github.com/bitnami-labs/sealed-secrets)
