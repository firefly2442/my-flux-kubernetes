# Frigate

Frigate is a video recording and detection management system for hooking
into cameras.

It is setup with Helm and uses local USB storage available on a specific
node to store the recordings.  This helps prevent writing large amounts
of data to the SSDs which can be bad for endurance and lifespan.

The configuration is embedded in the YAML.  MQTT integration leverages
the RabbitMQ service running on the cluster.

The `/config` directory stores the backend Sqlite database and other
state information.  Keep an eye on this storage to make sure it
doesn't grow beyond the size of the mounted PVC.

## Links

* [https://frigate.video/](https://frigate.video/)
