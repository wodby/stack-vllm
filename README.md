# vLLM stack

Deploy one vLLM inference service on a GPU-ready Kubernetes cluster. The service
starts with a pinned Qwen3-0.6B model for testing. Qwen is a model selection,
not a separate service or image.

Status: initial implementation, not released or deployed.

## Before deploying

Use a Wodby environment supporting GPU resource requests and make the
[vLLM service](https://github.com/wodby/service-vllm) available before importing
this stack. Read that service's GPU, driver and device-plugin prerequisites.
This stack does not install an operator or create GPU capacity.

Configure private-network access for the entire app. A vLLM API key alone does
not protect every management and metrics route; this stack deliberately does
not expose a public inference server.

## Configure and call the model

1. Select the model and its revision together in the vLLM service settings.
   Leave the Qwen preset for the first smoke test. Add a secret Hugging Face
   token only if your chosen model needs one.
2. Choose GPU count and replicas. If using more than one GPU per replica,
   set tensor parallelism to the same GPU count. Check available VRAM and node
   capacity; Kubernetes device counts do not prove a model fits.
3. Deploy after confirming the prerequisites. Use the app's private HTTPS
   endpoint address with `/v1` appended, the generated `api_key` secret, and the served
   model name (`model` by default).
4. Use the [Python inference examples](https://github.com/wodby/llm-inference-boilerplate)
   from a machine that can reach the private endpoint.

Each replica has an ephemeral model cache. Pod replacement downloads the model
again. Updates of a singleton interrupt availability; replicas do not share GPU
memory. See the service README for limits and operational settings.

This initial stack is direct vLLM serving. KServe, external GPU providers,
Wodby Cloud GPU billing and token-aware scaling are not enabled by it.
Application Access suppresses the ordinary public route from app creation;
use the endpoint reported by Application Access.

<!-- wodby:generated:start -->
<!-- wodby:generated:end -->
