# Ollama

Get up and running with large language models locally.

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

## Links

* [https://github.com/ollama/ollama](https://github.com/ollama/ollama)
* [https://truecharts.org/charts/stable/ollama/](https://truecharts.org/charts/stable/ollama/)
