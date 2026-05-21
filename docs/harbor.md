# Harbor

An open source trusted cloud native registry project that stores, signs, and scans content.

## Login

* Username: `admin`
* Password: our usual typical password

## Setup

Setup seaweedfs or an s3 compatible server like minio, garage,
rustfs, etc.  For this setup, we're using seaweedfs.

Install the [aws-cli](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html):

```shell
sudo snap install aws-cli --classic
```

Test that we can login using the credentials:

```shell
AWS_ACCESS_KEY_ID=admin \
AWS_SECRET_ACCESS_KEY=secret \
aws \
  --endpoint-url=http://192.168.1.140:8333 \
  s3 ls
```

Create a new bucket to save our images:

```shell
AWS_ACCESS_KEY_ID=admin \
AWS_SECRET_ACCESS_KEY=secret \
aws \
  --endpoint-url=http://192.168.1.140:8333 \
  s3 mb s3://harbor
```

After this, the above `aws s3 ls` command should show our new bucket.

After logging in to Harbor, go to "Registries" and add `dockerhub-proxy`.  Also make sure to test
the connection.  Created another registry called `ghcr-proxy`.

Then go to "Projects" and create a new project called `dockerhub-proxy`.
Set the access level to `public`.  Also check `Proxy Cache` and then
under the drop-down select the registry we just setup.
Create another project called `ghcr-proxy` for Github Container Registry
and do the same thing.

Then to test, try pulling an image:

```shell
docker pull harbor.homelab.rivetcode.com/dockerhub-proxy/alpine:latest
# OR
docker pull harbor.homelab.rivetcode.com/ghcr-proxy/firefly2442/jupyterlab-r-docker-stack-helm:latest
```

The backend storage for the images will be the s3 compatible object storage.

To confirm this:

```shell
AWS_ACCESS_KEY_ID=admin \
AWS_SECRET_ACCESS_KEY=secret \
aws \
  --endpoint-url=http://192.168.1.140:8333 \
  s3 ls s3://harbor
```

You should see files listed so we know it's working.

## Harbor as Registry

In addition to pull-through-cache as a registry, we can also push images
to Harbor and serve those up through the registry.

```shell
docker login harbor.homelab.rivetcode.com
# use username: admin and the password we setup
docker pull alpine:latest
docker tag alpine:latest harbor.homelab.rivetcode.com/library/alpine:latest
docker push harbor.homelab.rivetcode.com/library/alpine:latest
```

This will use the default `library` project.

## Usage

Anything that we need to bootstrap the k3s cluster services or Harbor itself should not
be setup to use Harbor.  However, other apps within the cluster or apps outside the cluster
can use it.  For anything that is not critical to the operation of the cluster and getting
it bootstrapped on first launch, those are good candidates for pointing to Harbor.

## Debugging

See what the configuration is setup as:

```shell
kubectl exec -n harbor deploy/harbor-registry -- cat /etc/registry/config.yml
```

## Links

* [https://goharbor.io](https://goharbor.io)
* [https://github.com/goharbor/harbor-helm](https://github.com/goharbor/harbor-helm)
* [https://github.com/goharbor/harbor](https://github.com/goharbor/harbor)
* [Youtube Tutorial on Harbor Install](https://www.youtube.com/watch?v=lf3bP7Cx-Xc)
