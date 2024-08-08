# Move WSL storage

In my scenario, I need to move WSL & Docker from default location(C:) to D.

## 1 Shutdown WSL

```
$ wsl --shutdown
```

If it does not work, reboot your PC.

## 2 Export WSL

```
$ wsl -l -v  # check WSL name and version

# my wsl list
Ubuntu-24.04
docker-desktop-data
docker-desktop

$ wsl --export Ubuntu-24.04 D:\tmp\Ubuntu2404.tar
$ wsl --export docker-desktop-data D:\tmp\docker-desktop-data.tar
$ wsl --export docker-desktop D:\tmp\docker-desktop.tar
```

## 3 Unregister

```
$ wsl --unregister Ubuntu-24.04
$ wsl --unregister docker-desktop-data
$ wsl --unregister docker-desktop
```

## 4 Import

```
$ wsl --import Ubuntu-24.04 D:\WSLsystem\Ubuntu-24.04 D:\tmp\Ubuntu2404.tar
$ wsl --import docker-desktop-data D:\WSLsystem\docker-desktop-data D:\tmp\docker-desktop-data.tar
$ wsl --import docker-desktop D:\WSLsystem\docker-desktop D:\tmp\docker-desktop.tar
```

## 5 Set default user

```
$ wsl  # Jump into wsl, default user would be `root`

$ vim /etc/wsl.conf
```

Add following content: 

```
[user]
default = xxx
```

## Done!