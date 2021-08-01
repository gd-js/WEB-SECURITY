# Webkit JavaScriptCore Ubuntu 20.4 Setup and Manual 

## Install Webkit and JSC

```console
sudo add-apt-repository ppa:webkit-team
sudo apt-get update
sudo apt install subversion

sudo apt-get install gtk-doc-tools autoconf automake libtool libgtk2.0-dev libpango1.0-dev libicu-dev libxslt-dev libsoup2.4-dev libsqlite3-dev gperf bison flex libjpeg62-dev libpng12-dev libxt-dev autotools-dev libgstreamer-plugins-base0.10-dev libenchant-dev libgail-dev

sudo svn checkout http://svn.webkit.org/repository/webkit/trunk ~/src/WebKit
cd ~/src/WebKit
make
sudo make install

svn update WebKit/Source --set-depth immediates
svn update WebKit/Source/JavaScriptCore --set-depth infinity
svn update WebKit/PerformanceTests
svn update WebKit/Tools
```

install lates npm
```console
sudo apt-get install python-software-properties python g++ make
sudo add-apt-repository ppa:chris-lea/node.js
sudo apt-get update
sudo apt-get install nodejs
```
