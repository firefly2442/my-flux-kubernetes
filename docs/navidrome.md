# Navidrome

Navidrome is an open source web-based music collection server and streamer.

Use `kubectl cp` to copy files from the local filesystem to a running pod
and thus the corresponding pvc.
For example:

```shell
kubectl cp ./ navidrome-7c6ff8dd99-25xg2:/music -n navidrome
```

Or alternatively, we can use NFS to mount our music from our backup
as a read-only share.  ZFS access is read-only to prevent any issues with writing
or renaming media records and files.  ZFS is accessed via NFS.

## Setup

Install NFS server on our node with the Navidrome media, in our case, `dellxps`.

```shell
sudo apt install nfs-kernel-server
```

Edit `/etc/exports` and setup the folder and access as ro - read-only:

```shell
/data/windowsbackup/Music 192.168.1.0/24(ro,sync,no_subtree_check,no_root_squash)
```

Save the file and then apply the changes:

```shell
sudo exportfs -ra
sudo systemctl enable --now nfs-kernel-server
```

## Links

* [https://www.navidrome.org/](https://www.navidrome.org/)
* [https://github.com/navidrome/navidrome/](https://github.com/navidrome/navidrome/)
* [https://truecharts.org/charts/stable/navidrome/](https://truecharts.org/charts/stable/navidrome/)
