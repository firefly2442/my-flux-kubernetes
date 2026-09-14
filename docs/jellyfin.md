# Jellyfin

The free media server and backend.

This is setup to only run on the node with our media stored
in ZFS.  ZFS access is read-only to prevent any issues with writing
or renaming media records and files.  ZFS is accessed via NFS.

## Setup

Install NFS server on our node with Jellyfin media, in our case, `alienware`.

```shell
sudo apt install nfs-kernel-server
```

Edit `/etc/exports` and setup the folder and access as ro - read-only:

```shell
/twotbmirror/media 192.168.1.0/24(ro,sync,no_subtree_check,no_root_squash)
```

Save the file and then apply the changes:

```shell
sudo exportfs -ra
sudo systemctl enable --now nfs-kernel-server
```

## Links

* [https://github.com/jellyfin/jellyfin](https://github.com/jellyfin/jellyfin)
* [https://truecharts.org/charts/stable/jellyfin/](https://truecharts.org/charts/stable/jellyfin/)
