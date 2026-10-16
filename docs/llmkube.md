# llmkube

Kubernetes operator for self-hosted LLM inference.

## Setup

Primarily setup to run on the Gmktec Strix Halo Evo X-2 device with
64 GB of unified memory.

This will install a set of Custom Resource Definitions and an Operator.
To list them and make sure it's all running properly:

```shell
kubectl get crds -A | grep llmkube
```

Install NFS server on our node where we will save our models, in our case, `evo-x2`.

```shell
sudo apt install nfs-kernel-server
```

Edit `/etc/exports` and setup the folder and access as ro - read-only:

```shell
/models 192.168.1.0/24(ro,sync,no_subtree_check,no_root_squash)
```

Save the file and then apply the changes:

```shell
sudo exportfs -ra
sudo systemctl enable --now nfs-kernel-server
```

## Links

* [https://llmkube.com/docs/getting-started](https://llmkube.com/docs/getting-started)
* [https://github.com/defilantech/LLMKube](https://github.com/defilantech/LLMKube)
