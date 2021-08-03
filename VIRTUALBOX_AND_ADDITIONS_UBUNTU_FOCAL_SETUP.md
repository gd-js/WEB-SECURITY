# Install Virtualbox on Ubuntu 20.4 plus Guest Additions

always update to latest Virtualbox version and reboot liberally

### Dependencies
```console
sudo apt update && sudo apt upgrade
sudo apt-get install virtualbox-dkms
```
## Install Virtualbox

add oracle repo gpg key and download virtualbox
```console
wget -q https://www.virtualbox.org/download/oracle_vbox_2016.asc -O- | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] http://download.virtualbox.org/virtualbox/debian $(lsb_release -cs) contrib"
sudo apt update && sudo apt install virtualbox-6.0

```
remove virtualbox
```console
sudo apt remove virtualbox virtualbox-*
```

### Install Guest Additions

run comands in VM
```console
sudo apt install build-essential dkms linux-headers-generic 
sudo rcvboxadd setup
```

### Debugging
```console
rm -r /etc/init.d/vboxdrv
rm -r /var/lib/update-rc.d/vboxdrv 
apt-get install virtualbox virtualbox-dkms virtualbox-guest-utils virtualbox-guest-additions virtualbox-qt
sudo /etc/init.d/vboxdrv setup
```

### Install VMs like Kali Linux or Ubuntu as OVA files
https://kali.org/get-kali/  
https://www.linuxvmimages.com/images/ubuntu-2004
