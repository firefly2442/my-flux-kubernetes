# LiteLLM

Python SDK, Proxy Server (AI Gateway) to call 100+ LLM APIs in OpenAI (or native)
format, with cost tracking, guardrails, loadbalancing and logging. [Bedrock, Azure,
OpenAI, VertexAI, Cohere, Anthropic, Sagemaker, HuggingFace, VLLM, NVIDIA NIM]

There is [no telemetry](https://docs.litellm.ai/docs/observability/telemetry) enabled
by default.

## Models

LiteLLM is configured with the following model providers:

* [Google Gemini](https://aistudio.google.com)
* [Gemma4 from Google](https://aistudio.google.com)
* [Cerebras AI](https://cloud.cerebras.ai)

[This page from Google](https://aistudio.google.com/rate-limit) in particular
is helpful to show all the different models and what is available and deprecated.
Models are substantially rate-limited depending on the model.

[And this is for Cerebras AI](https://inference-docs.cerebras.ai/support/rate-limits)
and their rate-limits.

Terminology:

* `RPM` - peak requests per minute
* `TPM` - peak input tokens per minute
* `RPD` - max requests per day

List available models:

```shell
curl -X 'GET' \
  'https://litellm.homelab.rivetcode.com/models?return_wildcard_routes=false&include_model_access_groups=false&only_model_access_groups=false&include_metadata=false' \
  -H 'accept: application/json' \
  -H 'x-litellm-api-key: API_KEY'
```

Test the model:

```shell
curl https://litellm.homelab.rivetcode.com/v1/chat/completions \
  -H "Authorization: Bearer API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemma-4-31b-it",
    "messages": [
      {
        "role": "user",
        "content": "Hello"
      }
    ]
  }'
```

## Virtual Keys

Virtual keys are a way of generating an API key that is unique and can be used for applications
or other needs.  Multiple models can be tied to a Virtual Key.  In addition, you can have
failover in the settings/setup of the key so one model will be primary, but then if it runs
out of tokens for the day you can have other models as backups.

## Links

* [https://github.com/BerriAI/litellm](https://github.com/BerriAI/litellm)
* [https://docs.litellm.ai/docs/](https://docs.litellm.ai/docs/)
* [https://github.com/BerriAI/litellm/tree/litellm_internal_staging/deploy/charts/litellm-helm](https://github.com/BerriAI/litellm/tree/litellm_internal_staging/deploy/charts/litellm-helm)
