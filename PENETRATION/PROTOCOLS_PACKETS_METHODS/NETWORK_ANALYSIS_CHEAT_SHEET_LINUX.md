# Network Analysis Cheat Sheet Linux
```
#tcpdump
#dig
#ping
#ifconfig
sudo apt install curl
sudo apt install zsh
sudo apt install net-tools
sudo apt install nmap
```
basic analysis
```console
ping
dig
ifconfig
tcpdump
```
check public ip
```console
ifconfig
curl https://ipinfo.io/ip
```
```
netstat check ports
```console
netstat -anutp
```
scan localhost
```
nmap 127.0.0.1
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
