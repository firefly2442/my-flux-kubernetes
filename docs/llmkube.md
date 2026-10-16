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

## Links

* [https://llmkube.com/docs/getting-started](https://llmkube.com/docs/getting-started)
* [https://github.com/defilantech/LLMKube](https://github.com/defilantech/LLMKube)
