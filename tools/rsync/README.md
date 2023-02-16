# Launchpad: tools/rsync
Remotely sync directories

## Installation
### Linux
```
sudo apt install rsync
```

## Examples
  * Local directory sync: `rsync -r source-directory/ destination-directory/`
  * Verbose local directory sync: `rsync -a -v --stats source-directory/ destination-directory/`
  * Remote directory sync: `rsync -r 192.168.50.202:/path/to/the/files/on/remote/server .`

## Resources
  * [Installing rsync on Windows](https://alanbarber.com/post/installing-rsync-on-windows/)

