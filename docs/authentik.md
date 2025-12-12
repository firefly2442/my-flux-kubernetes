# Authentik

Authentik is setup to protect pages with a common single-sign-on (SSO) experience.
For applications that don't have authentication, this can be a good way
to protect the application as well as provide a consistent login experience.

The configmap holds a Python script that sets up all the necessary applications
and pieces of Authentik.  There are both Authentik applications as well as providers.
Proxy providers just forward the request on to the application.  While OAuth2 providers
help with forwarding OAuth2 tokens and details to apps that support them.  This allows
the application to have more direct visibility into who logged in versus just a simple
proxy pass through.  All providers need to be added to the Authentik outpost.

The Authentik web-ui under the admin section has details and allows you to manually
adjust items if needed.  However, most of the work adding applications and configuring items
should be done through the Python script.  This allows for easier reproducibility upon
a full cluster reinstall.  Add applications and items to the Python script as
new applications and services are added.

If you make changes to the Python helper script, you may need to delete the job deployment
of that script to force it to re-run upon a Flux reconciliation.

The default admin user for Authentik is setup using a Sealed Secret.

Check on the Authentik setup:

```shell
kubectl get jobs -n authentik
```

When authentik updates, delete the setup job that authentik uses
and force it to re-create the outpost.  Otherwise, the outpost
will be at the old version and not match the new updated deployment.
Helm does not manage the outpost since that's created through our
setup automation script.

## Links

* [https://goauthentik.io/](https://goauthentik.io/)
* [Setting up Authentik Tutorial](https://www.youtube.com/watch?v=N5unsATNpJk)
* [Tutorial Combining Authentik and Traefik Middleware](https://www.youtube.com/watch?v=_I3hUI1JQP4)
* [Tutorial on Authentik and Traefik](https://github.com/brokenscripts/authentik_traefik)
