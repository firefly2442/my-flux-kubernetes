# llmkube

Kubernetes operator for self-hosted LLM inference.

## Overview

For Strix Halo, FP16 is generally preferred as there is hardware support for it.
The ROCm library is also generally more performant than Vulkan.  In the early days,
Vulkan was preferred, it perhaps is a bit more stable.  These days though, ROCm
should be the go-to.

## Setup

Primarily setup to run on the Gmktec Strix Halo Evo X-2 device with
64 GB of unified memory.

This will install a set of [Custom Resource Definitions](https://llmkube.com/docs/concepts/crds)
and an Operator.
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

## Image Generation

Image generation via Qwen Image 2.1 works well.  There is a custom version of Comfy-UI and model
weights via `Comfy-Org` made specifically for Comfy-UI.  Use one of the provided
[workflow templates provided](https://huggingface.co/Comfy-Org/Qwen-Image-2.1).  Save
the JSON file and drag-and-drop it into the Comfy-UI to load it.  Various settings
can be tuned.  For the models, use the following:

* `unet_name` - use the `bf16` safetensors or `turbo_bf16` version.  Turbo can be faster but have less quality.
* `clip_name` - use the `qwen3vl_8b_int8_convrot.safetensors` file or the `bf16` variant.  `bf16` will take longer.
* `vae_name` - use the file with `vae` in the name.
* `PE_model` - use the `int8` file either `t2i` for text-to-image or `i2i` for image-to-image depending on the generation.

The prompt enhancement via `refine_prompt` and `thinking_mode` I wasn't able to get working reliably.  It seemed
to just spit back out the same input image after processing.  Maybe I did something wrong though.

There are various settings like the `bit_depth` of the output image.  I set this to `16-bit`.
`megapixels` can also go from `1-4`.  `resolution` can go from `1024-2048`.  There are various
other settings I didn't change.

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
* [https://github.com/gufo-org/toolboxes](https://github.com/gufo-org/toolboxes)
* [https://llmkube.com/docs/labs/qwen38-flash-next-gufo-on-strix-halo](https://llmkube.com/docs/labs/qwen38-flash-next-gufo-on-strix-halo)
* [https://github.com/defilantech/llmkube-runtimes/pkgs/container/llmkube-gufo-rocm-gfx1151](https://github.com/defilantech/llmkube-runtimes/pkgs/container/llmkube-gufo-rocm-gfx1151)
* [https://llmkube.com/blog/qwen38-flash-next-gufo-strix-halo](https://llmkube.com/blog/qwen38-flash-next-gufo-strix-halo)
* [https://github.com/halo-box/strix-llama.cpp](https://github.com/halo-box/strix-llama.cpp)
* [https://github.com/lemonade-sdk/llamacpp-rocm](https://github.com/lemonade-sdk/llamacpp-rocm)
* [https://github.com/defilantech/llmkube-runtimes](https://github.com/defilantech/llmkube-runtimes)
* [https://github.com/kyuz0/amd-strix-halo-comfyui-toolboxes](https://github.com/kyuz0/amd-strix-halo-comfyui-toolboxes)
* [https://github.com/Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI)
* [https://github.com/squat/generic-device-plugin](https://github.com/squat/generic-device-plugin)
* [https://strixhalo.wiki/](https://strixhalo.wiki/)
* [https://strix-halo-toolboxes.com/](https://strix-halo-toolboxes.com/)
* [https://github.com/ROCm/TheRock](https://github.com/ROCm/TheRock)

## Videos and Tutorials

* [https://www.youtube.com/@donatocapitella/videos](https://www.youtube.com/@donatocapitella/videos)

## Official AMD Materials

* [https://github.com/amd-enterprise-ai/aim-build](https://github.com/amd-enterprise-ai/aim-build)
* [https://enterprise-ai.docs.amd.com/en/latest/aims/catalog/models.html](https://enterprise-ai.docs.amd.com/en/latest/aims/catalog/models.html)
* [https://enterprise-ai.docs.amd.com/en/latest/aims/guides/deployment-guide.html](https://enterprise-ai.docs.amd.com/en/latest/aims/guides/deployment-guide.html)
* [https://github.com/amd-enterprise-ai/aim-deploy](https://github.com/amd-enterprise-ai/aim-deploy)
* [https://www.youtube.com/watch?v=eOhfJ0YeYh0](https://www.youtube.com/watch?v=eOhfJ0YeYh0)

### Model Specific Links

* Qwen-Image-2.1
  * [https://github.com/QwenLM/Qwen-Image-2.1](https://github.com/QwenLM/Qwen-Image-2.1)
  * [https://huggingface.co/Qwen/Qwen-Image-2.1](https://huggingface.co/Qwen/Qwen-Image-2.1)
  * [https://huggingface.co/unsloth/Qwen-Image-2.1-GGUF](https://huggingface.co/unsloth/Qwen-Image-2.1-GGUF)
  * [https://github.com/gufo-org/gufo/tree/main/docs/models/qwen-image-2.1](https://github.com/gufo-org/gufo/tree/main/docs/models/qwen-image-2.1)
  * [https://huggingface.co/Comfy-Org/Qwen-Image-2.1](https://huggingface.co/Comfy-Org/Qwen-Image-2.1)
  * [https://www.youtube.com/watch?v=7je-SidZYjE](https://www.youtube.com/watch?v=7je-SidZYjE)
* MiniMax-H3
  * [https://huggingface.co/MiniMaxAI/MiniMax-H3](https://huggingface.co/MiniMaxAI/MiniMax-H3)
  * [https://github.com/gufo-org/gufo/blob/main/docs/models/minimax-h3/README.md](https://github.com/gufo-org/gufo/blob/main/docs/models/minimax-h3/README.md)
* Gemma-4
  * [https://huggingface.co/unsloth/gemma-4-26B-A4B-it-GGUF](https://huggingface.co/unsloth/gemma-4-26B-A4B-it-GGUF)
* MiniMax-H3
  * [https://huggingface.co/MiniMaxAI/MiniMax-H3](https://huggingface.co/MiniMaxAI/MiniMax-H3)
