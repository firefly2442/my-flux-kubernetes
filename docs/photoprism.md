# Photoprism

Photoprism is a photo management application.

## Setup

For the initial setup, I copied the origin files over from my existing install.
I shelled into the Kubernetes deployed Photoprism container.  I then copied
the files over.

```shell
apt update
apt-get install openssh-client
rsync -avzP carlsonp@192.168.1.226:/home/carlsonp/src/photoprism/originals /photoprism/originals
```

Then check the folder and move files around if needed.

Then go into the Library page and do a complete re-scan of the index.  This will not move
or delete any of the existing files but re-index them and add them to the database.

## Usage

The photo review feature is turned on, this helps to flag blurry photos.  Go into Search -> Review to
check the photos and approve or delete.

To delete photos, archive them first, then go into the archive page and delete them.

## Backups

Every so often, manually take a backup synchronization of the original photos.  Shell into the
Kubernetes deployed Photoprism container.

```shell
apt update
apt-get install openssh-client
rsync -avzP --delete /photoprism/originals/ carlsonp@192.168.1.114:/data/photosbackup/
```

## Links

* [https://www.photoprism.app/](https://www.photoprism.app/)
* [https://truecharts.org/charts/stable/photoprism/](https://truecharts.org/charts/stable/photoprism/)
