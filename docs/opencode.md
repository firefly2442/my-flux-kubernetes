# opencode

Opencode is setup with the integrated web server.
See also the `vscode` namespace and deployment
which uses the same base image.

## Setup

`opencode` configuration is setup via a `ConfigMap`.  When making changes to this
configuration, make the same changes to the `vscode` version.

## Usage

Store files in
`/config/projects` to persist them.

Copy files from the local machine into the running pod

```shell
kubectl get pods -n opencode

kubectl cp <local-path> <namespace>/<pod-name>:<remote-path>

kubectl cp ~/src/chromadb-photo-organizer opencode/opencode-docker-vscode-customized-59658fdd69-s9k7j:/config/projects/chromadb-photo-organizer
```

And copy files back out

```shell
kubectl cp opencode/opencode-docker-vscode-customized-59658fdd69-s9k7j:/config/projects/chromadb-photo-organizer/README.md ~/src/chromadb-photo-organizer/README.md
```

To leverage Git commits and bundles to get changes into the pod

```shell
# workstation
cd ~/src/<project-name>
git fetch origin
git bundle create /tmp/repo.bundle --all
kubectl -n opencode cp /tmp/repo.bundle <pod>:/tmp/repo.bundle

# in the pod
cd /config/projects/<project-name>
git fetch /tmp/repo.bundle 'refs/heads/*:refs/remotes/origin/*'
git merge origin/main
```

And to get changes out of the pod using Git commits and bundles

```shell
# in the pod
git commit -a # create commit as usual
git bundle create /tmp/repo.bundle --all

# workstation
cd ~/src/<project-name>
kubectl -n opencode cp <pod>:/tmp/repo.bundle /tmp/repo.bundle
git fetch /tmp/repo.bundle 'refs/heads/*:refs/remotes/origin/*'
git merge origin/main
```

And there is an even better integration with `gogs` for HTTPS git support.
Go into `gogs` and add the repository.  Then setup the remote url
and leverage git as usual.

```shell
cd /config/projects/yourproject
git remote add gogs http://gogs.gogs.svc.cluster.local:3000/carlsonp/yourproject.git
git remote update gogs
git push gogs master
```

This makes it easier to synchronize changes between a local laptop development
environment and the opencode container.

## Sandbox

Most egress traffic is blocked out of the pod.  Ingress traffic through the Traefik
ingress controller is the only way in.  Pod security standards are enforced.
The only way to get data in and out is via `kubectl cp`.

## Links

* [https://opencode.ai/docs/web/](https://opencode.ai/docs/web/)
* [https://github.com/anomalyco/opencode](https://github.com/anomalyco/opencode)
