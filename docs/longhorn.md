# Longhorn

Longhorn provides distributed storage and is the default storage class
for the cluster.  Data is replicated across 3 nodes by default.  Snapshots
can also be created.

Engine images on volumes can be manually upgraded through the UI.
In the drop-down for the volume, select "Upgrade Engine"
and then select the newer image.  Volumes that can be upgraded
will have a green up arrow denoting which ones need upgrading.

## Snapshots

Snapshots are local point-in-time saves of data in a volume
at that point in time.  Think of it like git version control
but for data.  They are stored within the cluster itself.
It can be good to take snapshots of volumes before important
needs like large application upgrades, moving computers around,
that type of thing.

Manually taken snapshots in the UI are never cleaned up and deleted
so delete these old snapshots if they're no longer needed.

## Backups

Backups by comparison to snapshots are a full state (assuming you select `Full Backup`)
of a volume at a point in time.  The historical changes are also saved
as delta diffs if you also have other backups done to that server.
This backup of the volume can be sent
outside the cluster to storage systems that support
a variety of types.  We will use s3 compatible storage.

Setup seaweedfs or an s3 compatible server like minio, garage,
rustfs, etc.  For this setup, we're using seaweedfs.

Install the [aws-cli](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html):

```shell
sudo snap install aws-cli --classic
```

Test that we can login using the credentials:

```shell
AWS_ACCESS_KEY_ID=admin \
AWS_SECRET_ACCESS_KEY=secret \
aws \
  --endpoint-url=http://192.168.1.140:8333 \
  s3 ls
```

Create a new bucket to save our backups:

```shell
AWS_ACCESS_KEY_ID=admin \
AWS_SECRET_ACCESS_KEY=secret \
aws \
  --endpoint-url=http://192.168.1.140:8333 \
  s3 mb s3://longhorn
```

After this, the above `aws s3 ls` command should show our new bucket.

A sealed secret contains the connection details for longhorn to
connect to seaweedfs:

```shell
AWS_ACCESS_KEY_ID: admin
AWS_SECRET_ACCESS_KEY: secret
AWS_ENDPOINTS: http://192.168.1.140:8333
AWS_FORCE_PATH_STYLE: "true"
AWS_SSL: "false"
AWS_REGION: seaweedfs
```

In the longhorn web-ui, create a new backup.  This will automatically
transfer it over to seaweedfs.  Use the restore ability to
download the backup and add it as a detached pvc in longhorn.

To restore, we need to first scale down anything using the pvc.

```shell
kubectl scale deployment <app> --replicas=0 -n <namespace>
kubectl scale statefulset <app> --replicas=0 -n <namespace>
```

Describe the existing PVC and write down any details:

```shell
kubectl describe pvc <name> -n <namespace>
```

Wait for the old volume status to become
`Detached`. Once detached, delete the old volume in the Longhorn UI and
delete the old PVC in Kubernetes.

Delete the old volume & PVC:

```shell
kubectl delete pvc <name> -n <namespace>
```

Restore the backup: In the Longhorn UI, go to the Backup tab, find your target
backup, click the three dots, and select `Restore Latest Backup` (or choose a
specific backup point).

Name the restored volume: When prompted to name the restored volume, use the
exact same name as the original PVC/PV (e.g., `pvc-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`).
This ensures Kubernetes seamlessly recognizes the resource.

Create the PV/PVC: Wait for the restore to complete and for the new volume to become
`Detached`. From the dropdown next to your new volume, click `Create PV/PVC`.

Finalize binding: In the creation wizard, check both `Create PVC` and `Use Previous PVC`.
Select the correct file system type (e.g., `ext4` or `xfs`) and click OK.

Scale the workload back up: Wait for the PVC to show as `Bound` in Kubernetes, then scale
your pods back up to the desired replica count.

Lastly, scale back up:

```shell
kubectl scale deployment <app> --replicas=1 -n <namespace>
```

For full [System Backups](https://longhorn.io/docs/1.12.0/advanced-resources/system-backup-restore/backup-longhorn-system/)
these can be done via the web-UI.  This captures all the settings and details and can be used
to restore should something go wrong.  It uses the default backup target.

## Recurring Jobs

See details in the [longhorn documentation on recurring jobs](https://longhorn.io/docs/1.11.2/snapshots-and-backups/scheduling-backups-and-snapshots/).

The jobs are setup as `RecurringJob` defined in YAML and managed
by Flux.

Snapshots and backups are setup to be automated using recurring jobs.
Hourly snapshots are taken as well as daily and weekly backups.
Labels are used to define which pvcs will be available for these
snapshot and backup recurring jobs.  Add the following to the pvc
for the items we wish to snapshot + backup:

```shell
# PVC definition:

metadata:
  labels:
    recurring-job.longhorn.io/source: enabled
    recurring-job-group.longhorn.io/backup: enabled

# or via values.yaml:

persistence:
    data:
        enabled: true
        size: 1Gi
        labels:
            recurring-job.longhorn.io/source: enabled
            recurring-job-group.longhorn.io/backup: enabled
```

When adding these labels in code, Flux will not retroactively
apply the label.  In some cases, the Helm charts also don't fully
support the labels so they have to be applied manually.
You will need to manually add it to existing
pvcs.  For example:

```shell
kubectl label pvc navidrome-music -n navidrome recurring-job.longhorn.io/source=enabled
kubectl label pvc navidrome-music -n navidrome recurring-job-group.longhorn.io/backup=enabled
```

The recurring job on the source applies the pvc labels down to the volume labels as well.

Describe the pvc to make sure the labels get applied properly:

```shell
kubectl describe pvc navidrome-music -n navidrome
```

List the recurring jobs with:

```shell
kubectl get recurringjobs -n longhorn-system
```

## Applications Requiring Backups

At a minimum, these applications should be fully backed up and tested to ensure
no data is lost.

* Gitea
* Home Assistant
* Memos
* Navidrome
* Photoprism
* Paperlessngx
* Linkding
* Karakeep

## Links

* [https://longhorn.io/](https://longhorn.io/)
* [https://github.com/longhorn/longhorn](https://github.com/longhorn/longhorn)
* [Longhorn Video Tutorial By Christian Lempa](https://www.youtube.com/watch?v=-ImtLXcEna8)
