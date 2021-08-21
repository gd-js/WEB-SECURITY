# Webkit JavaScriptCore Ubuntu 20.4 Setup and Manual 

### Install nodejs and npm
```console
sudo apt update && sudo apt upgrade
sudo apt install nodejs npm
```
### Install ruby
```console
sudo apt update && sudo apt upgrade
sudo apt install ruby
```


## Install Webkit JavascriptCore

```console
sudo add-apt-repository ppa:webkit-team
sudo apt update && sudo apt upgrade
sudo apt install subversion

sudo apt-get install gtk-doc-tools autoconf automake libtool libwebkit2gtk-4.0-37 ibwebkit2gtk-4.0-dev libgtk4.0-dev libpango1.0-dev libicu-dev libxslt-dev libsoup2.4-dev libsqlite3-dev gperf bison flex libjpeg62-dev libpng12-dev libxt-dev autotools-dev libgstreamer-plugins-base0.10-dev libenchant-dev libgail-dev gir1.2-webkit2-4.0
```

```console
sudo svn checkout http://svn.webkit.org/repository/webkit/trunk ~/src/WebKit
cd ~/src/WebKit
./Tools/Scripts/build-webkit --jsc-only --debug

svn update WebKit/Source --set-depth immediates
svn update WebKit/Source/JavaScriptCore --set-depth infinity
svn update WebKit/PerformanceTests
svn update WebKit/Tools
```
