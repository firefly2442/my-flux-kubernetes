# Data Science

This provides an environment to do Data Science work with all the appropriate packages
and software available around Python, R, etc.  It's a Jupyter IDE and environment.  It uses
a customized version of a Data Science stack with additional packages installed.

Enter your username at the credentials prompt and don't enter a password.  Make sure
to use the same username each time as it spins up a persistent volume claim (PVC) and storage
for you that is tied to that username.  This gets mounted when the environment is used
and unmounts when it's not in use.  This allows for persistence of code, data, etc.

## Links

* [https://github.com/firefly2442/jupyterlab-r-docker-stack-custom](https://github.com/firefly2442/jupyterlab-r-docker-stack-custom)
