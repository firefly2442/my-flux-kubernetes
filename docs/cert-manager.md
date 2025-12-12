# Cert Manager

Cert manager, as the name suggests, can automatically create and manage
certificates for you.  It's tied into Let's Encrypt to allow
the automatic provisioning and management of TLS certs
to allow HTTPS connectivity to applications.  Let's Encrypt has
both a staging and production server for cert creation and management.
There are quotas and limits on cert creation, particularly for production
so make sure everything works properly first.  If you overload their servers,
you get blocked.

Cloudflare provides DNS management of the `*.homelab.rivetcode.com`
domain names.  DNS registration is provided by WestHost and DNS management
is provided by Cloudflare.

The API token for Cloudflare is allowed DNS edit permissions on
only the `rivetcode.com` domain name.

## Links

* [https://cert-manager.io/](https://cert-manager.io/)
* [Setting up Traefik and Cert Manager](https://www.youtube.com/watch?v=vJweuU6Qrgo)
* [TechnoTim Tutorial on cert-manager and Lets Encrypt](https://www.youtube.com/watch?v=G4CmbYL9UPg)
