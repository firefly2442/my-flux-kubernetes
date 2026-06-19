# Twingate

Twingate is a modern, cloud-based remote access solution that replaces traditional Virtual Private Networks (VPNs).

## Setup

The secret contains the values of both the `TWINGATE_ACCESS_TOKEN` and `TWINGATE_REFRESH_TOKEN`.

## Usage

The Twingate Connector is installed on our Kubernetes cluster which then allows Twingate Clients to connect
through the Connector after setup in their web-ui.

Install the Twingate Client, for example, on my laptop using the automated Ansible script for setup.

Then leverage the client through the following commands:

```shell
twingate help
twingate start
twingate status
twingate resources
twingate stop
```

## Links

* [https://www.twingate.com/](https://www.twingate.com/)
* [https://github.com/Twingate/helm-charts](https://github.com/Twingate/helm-charts)
