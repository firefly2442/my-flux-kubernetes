# Volcano

Volcano is a cloud-native batch system for distributing workloads.  It has
an accompanying dashboard to show jobs and workloads.

## Usage

Create a YAML file outlining the work you want to run.  For example:

```shell
# vcjob-quickstart.yaml
apiVersion: batch.volcano.sh/v1alpha1
kind: Job
metadata:
  name: quickstart-job
spec:
  minAvailable: 3
  schedulerName: volcano
  # If you omit the 'queue' field, the 'default' queue will be used.
  # queue: default
  policies:
    # If a pod fails (e.g., due to an application error), restart the entire job.
    - event: PodFailed
      action: RestartJob
  tasks:
    - replicas: 3
      name: completion-task
      policies:
      # When this specific task completes successfully, mark the entire job as Complete.
      - event: TaskCompleted
        action: CompleteJob
      template:
        spec:
          containers:
            - command:
              - sh
              - -c
              - 'echo "Job is running and will complete!"; sleep 100; echo "Job done!"'
              image: busybox:latest
              name: busybox-container
              resources:
                requests:
                  cpu: 1
                limits:
                  cpu: 1
          restartPolicy: Never
```

Now launch the job:

```shell
kubectl apply -f quickstart-volcano-test.yaml -n volcano-system
```

Go into the Volcano dashboard and look at the jobs page.  Also looking at the pods
will show you details on the completed items:

```shell
kubectl get pods -n volcano-system
```

## Debugging

To force a restart of the dashboard deployment

```shell
kubectl rollout restart deployment/volcano-dashboard -n volcano-system
```

The web-ui dashboard does not yet have a Helm chart.
[This Github issue](https://github.com/volcano-sh/dashboard/issues/176) outlines
the request and a potential implementation.
See [this folder](https://github.com/volcano-sh/dashboard/tree/main/deployment)
for manually deploying the pieces needed in Kubernetes.

## Links

* [https://github.com/volcano-sh/volcano](https://github.com/volcano-sh/volcano)
* [https://github.com/volcano-sh/dashboard](https://github.com/volcano-sh/dashboard)
