# Ollama

Get up and running with large language models locally.

## Text Generation Models

Exec into the running container and run:

```shell
ollama pull qwen3.5:4b
```

To list available models:

```shell
curl https://ollama.homelab.rivetcode.com/api/tags
```

To test if ollama is running properly:

```shell
curl https://ollama.homelab.rivetcode.com/api/generate \
  -d '{
    "model": "qwen3.5:4b",
    "prompt": "Why is the sky blue?",
    "stream": false
  }'
```

## MiniCPM5-2B

Pull [the model](https://huggingface.co/openbmb/MiniCPM5-2B) from
[Ollama](https://ollama.com/openbmb/minicpm5-2b).  There is also
a 1B parameter size model from the same company.

```shell
ollama pull openbmb/minicpm5-2b:2b
```

To test the running model:

```shell
curl https://ollama.homelab.rivetcode.com/api/generate \
  -d '{
    "model": "openbmb/minicpm5-2b:2b",
    "prompt": "Why is the sky blue?",
    "stream": false
  }'
```

## System One Decision Models

```shell
ollama pull clef-flash:9b
```

To test the deployed model:

```shell
curl -X POST https://ollama.homelab.rivetcode.com/v1/systemone \
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

## Links

* [https://github.com/ollama/ollama](https://github.com/ollama/ollama)
* [https://truecharts.org/charts/stable/ollama/](https://truecharts.org/charts/stable/ollama/)
