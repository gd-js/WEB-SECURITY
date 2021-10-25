# NMAP and net tools cheat sheet linux

_use www.explainshell.com_  

install zshell
```console
sudo apt update
sudo apt upgrade
sudo apt install zsh
```
install net-tools
```console
sudo apt update
sudo apt upgrade
sudo apt install net-tools
```
install iptables
```console
sudo apt update
sudo apt upgrade
sudo apt install iptables
```
install nmap
```console
sudo apt update
sudo apt upgrade
sudo apt install nmap
```
check ip
```console
ifconfig
ip address
```
check public ip
```console
ifconfig
curl https://ipinfo.io/ip
```
iptables status
```console
sudo iptables -L -v
```
netstat check ports
```console
netstat -anutp
```
nmap scan localhost
```
nmap 127.0.0.1
```
nmap scan target
```console
nmap 142.250.181.228
```
nmap scan host
```console
nmap www.google.com
```
nmap scan range
```console
nmap 142.250.181.1-24
```
nmap scan subnet
```console
nmap 142.250.181.228/13
```
nmap scan from txt
```console
nmap –iL textlist.txt
```
nmap scan/fast/all scan port/range/more target
```console
nmap –p/-F/-p- 80/1-200/-sV --version-intensity 0 to 9 142.250.181.228
```
nmap scan tcp/syn/udp ports/fastping/os target
```console
nmap -sT/-sS/-sU -p 80,130,255/sP -F/-A 142.250.181.228
```
iptables enable localhost traffic
```console
sudo iptables -A INPUT -i lo -j ACCEPT
```
enable http, ssh, ssl ports
```console
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 443 -j ACCEPT
```
iptables complex commands
```console
sudo iptables -A 
-i <interface> -p <protocol> -s <source> --scource-range --dport  -j <target> --line-numbers
```
iptables packets from ip
```console
sudo iptables -A INPUT -s 192.168.1.3 -j ACCEPT
sudo iptables -A INPUT -s 192.168.1.3 -j DROP
```
iptables clear rules
```console
sudo iptables -F
```
iptables delete specific rule
```console
sudo iptables -L --line-numbers
sudo ip tables -D INPUT 3
```
iptables persist/override startup rules
```console
sudo /sbin/iptables-save
```
iptables block all ports except declared
```console
sudo iptables -F
sudo iptables -P INPUT DROP
sudo iptables -A INPUT -i lo -p all -j ACCEPT
sudo iptables -A INPUT -m state --state RELATED,ESTABLISHED -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 443 -j ACCEPT
sudo iptables -A INPUT -j DROP
```
