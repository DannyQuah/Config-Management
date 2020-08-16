---
fileName: README.md
# Last-edited: Sat 2020.08.15.1629 -- Danny Quah (me@DannyQuah.com)
Type: Notes
Tags: Software
# Created: Sat 2020.08.15.1518 -- Danny Quah (me@DannyQuah.com)

output: pdf_document
---

# Config-Management

My shell scripts, dotfiles, Linux installations, editor configurations, templates, stylesheets

On new Linux machine, hardware setup is as in Linux-2014.07 // Linux-Machine-New (including filesystem loading). Then as needed might still run the following:

```sh
$ source ./Linux/src/linux-new-setup
# OR
$ wget -O - https://raw.githubusercontent.com/DannyQuah/Config-Management/master/machines/Linux/src/linux-new-setup | sudo bash
```

(which will take a while, depending on how fast the machine and Internet connection are). If the hardware setup works, though, since the filesystem there includes these scripts, I typically just run `linux-new-setup` from there.

<!---
   Invisible section
-->

