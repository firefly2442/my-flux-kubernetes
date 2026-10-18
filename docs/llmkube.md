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

Models can also be added to `litellm`.

## Additional Model Testing via Curl

Gemma-4

```shell
curl https://gemma-4.homelab.rivetcode.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemma-4",
    "messages": [
      {
        "role": "user",
        "content": "Write me a poem about the blue sky."
      }
    ]
  }'
```

## System One and Decision Models

Clef (full model, not flash)

```shell
curl https://clef.homelab.rivetcode.com/v1/systemone \
  -H "Content-Type: application/json" \
  -d '{
    "model": "clef-flash:9b",
    "state": "Checkout has been failing for every customer for the last hour.",
    "questions": {
      "urgent": {"type": "noul", "instructions": "Is this support request urgent?"},
      "team": {
        "type": "choice",
        "instructions": "Which team should handle this request?",
        "criteria": {
          "billing": "Payments, invoices, and refunds",
          "technical": "Outages, errors, and configuration",
          "sales": "Plans and upgrades"
        }
      },
      "severity": {
        "type": "score",
        "instructions": "How severe is the customer impact?",
        "criteria": ["No impact", "Minor", "Major", "Critical"]
      }
    }
  }'
```

See more details [in this blog post](https://huggingface.co/blog/ggml-org/decision-models-in-llamacpp).

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
* [https://llmkube.com/docs/labs/qwen38-flash-next-gufo-on-strix-halo](https://llmkube.com/docs/labs/qwen38-flash-next-gufo-on-strix-halo)
* [https://github.com/defilantech/llmkube-runtimes/pkgs/container/llmkube-gufo-rocm-gfx1151](https://github.com/defilantech/llmkube-runtimes/pkgs/container/llmkube-gufo-rocm-gfx1151)
* [https://llmkube.com/blog/qwen38-flash-next-gufo-strix-halo](https://llmkube.com/blog/qwen38-flash-next-gufo-strix-halo)
* [https://github.com/halo-box/strix-llama.cpp](https://github.com/halo-box/strix-llama.cpp)
* [https://github.com/lemonade-sdk/llamacpp-rocm](https://github.com/lemonade-sdk/llamacpp-rocm)

### Model Specific Links

* Qwen-Image-2.1
  * [https://github.com/QwenLM/Qwen-Image-2.1](https://github.com/QwenLM/Qwen-Image-2.1)
  * [https://huggingface.co/Qwen/Qwen-Image-2.1](https://huggingface.co/Qwen/Qwen-Image-2.1)
  * [https://huggingface.co/unsloth/Qwen-Image-2.1-GGUF](https://huggingface.co/unsloth/Qwen-Image-2.1-GGUF)
  * [https://github.com/gufo-org/gufo/tree/main/docs/models/qwen-image-2.1](https://github.com/gufo-org/gufo/tree/main/docs/models/qwen-image-2.1)
* MiniMax-H3
  * [https://huggingface.co/MiniMaxAI/MiniMax-H3](https://huggingface.co/MiniMaxAI/MiniMax-H3)
  * [https://github.com/gufo-org/gufo/blob/main/docs/models/minimax-h3/README.md](https://github.com/gufo-org/gufo/blob/main/docs/models/minimax-h3/README.md)
* Gemma-4
  * [https://huggingface.co/unsloth/gemma-4-26B-A4B-it-GGUF](https://huggingface.co/unsloth/gemma-4-26B-A4B-it-GGUF)
