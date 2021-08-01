# Install Virtualbox on Ubuntu 20.4 plus Guest Additions

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

### Install VMs, eg. Kali Linux or more Ubuntu, as OVF files
https://kali.org/get-kali/  
https://www.linuxvmimages.com/images/ubuntu-2004
