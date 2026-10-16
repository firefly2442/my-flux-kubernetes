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
/models 192.168.1.0/24(rw,sync,no_subtree_check,no_root_squash)
```

Save the file and then apply the changes:

```shell
sudo exportfs -ra
sudo systemctl enable --now nfs-kernel-server
```

The `generic-device-plugin` provides a way of passing the GPU device to the inference service
so that it can use the GPU.

## Usage

`llmkube` adds two new CRDs: `Models` and `InferenceServices`.

To list all the models and describe one

```shell
kubectl get models -A
kubectl describe model qwen3.8-27b-uncensored -n llmkube-system
```

Following [this tutorial](https://llmkube.com/docs/labs/qwen38-flash-next-gufo-on-strix-halo),
we want to combine `llmkube` and `gufo` together.  `gofu` will provide the container
image and `llmkube` will orchestrate everything.

To list all the inference services and describe one

```shell
kubectl get inferenceservices -A
kubectl describe inferenceservice qwen3.8-27b-uncensored-strix -n llmkube-system
```

Look at the services to setup networking

```shell
kubectl get svc -n llmkube-system
```

Look at the ingress routes for network routing

```shell
kubectl get ingressroutes -n llmkube-system
```

Test the deployed model

```shell
curl https://qwen3-8-27b-uncensored.homelab.rivetcode.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "qwen3.8-27b-uncensored",
    "messages": [
      {
        "role": "user",
        "content": "Hello"
      }
    ]
  }'
```

Remember to add internal and external networking checks to `gatus` for new models.

## Debugging

To check the AMD details or other characteristics of the GPU, leverage the
following commands

```shell
sudo amd-smi
sudo amdgpu_top
```

## Links

* [https://llmkube.com/docs/getting-started](https://llmkube.com/docs/getting-started)
* [https://github.com/defilantech/LLMKube](https://github.com/defilantech/LLMKube)
* [https://github.com/gufo-org/gufo](https://github.com/gufo-org/gufo)
