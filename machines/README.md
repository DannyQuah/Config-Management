Machines-Management

Last edited: Mon 2020.05.25.1947h -- Danny Quah
Created: Sat 2020.05.23.1232h -- Danny Quah

My shell scripts, dotfiles, Linux installations

On new Linux machine, hardware setup is as in Linux-2014.07 // Linux-Machine-New (including filesystem loading). Then as needed might still run the following:

```sh
$ source ./Linux/src/linux-new-setup
# OR
$ wget -O - https://raw.githubusercontent.com/DannyQuah/Machines-Management/master/Linux/src/linux-new-setup | sudo bash
```

(which will take a while, depending on how fast the machine and Internet connection are). If the hardware setup works, though, since the filesystem there includes these scripts, I typically just run `linux-new-setup` from there.
