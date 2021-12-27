# Over The Wire Wargames Bandit Solutions

_use www.explainshell.com_

install zshell
```console
sudo apt update
sudo apt upgrade
sudo apt install zsh
```

Redundant Logging in procedure as in Level 0
```console
ssh bandit0@bandit.labs.overthewire.org -p 2220
bandit0
exit
```

Bandit 0, Bandit Level 1 Walkthrough
```console
cat readme
exit
```

Bandit 1 Level 2 Walkthrough
```console
cat ./- tab to autofill
exit
```

Bandit 2 Level 3 Walkthrough
```console
cat s tab to autofill
exit
```

Bandit 3 Level 4 Walkthrough
```console
cd inhere
cat ./.hidden
exit
```

Bandit 4 Level 5 Walkthrough
```console
cd inhere
file ./-file* to find ascii file
cat ./-file07
exit
```

Bandit 5 Level 6 Walkthrough
```console
cd inhere
find -readable ! -executable -size 1033c
cat ./maybehere07/.file2
exit
```

Bandit 6 Level 7 Walkthrough
```console
find / -user bandit7 -group bandit6 -size 33c
cat /var/lib/dpkg/info/bandit7.password
exit
```

Bandit 7 Level 8 Walkthrough
```console
cat data.txt | grep millionth
exit
```

Bandit 8 Level 9 Walkthrough
```console
sort data.txt | uniq -u
exit
```

Bandit 9 Level 10 Walkthrough
```console
strings data.txt
exit
```

Bandit 10 Level 11 Walkthrough
```console
base64 -d data.txt
exit
```

Bandit 11 Level 12 Walkthrough
```console
data.txt | tr "A-Za-z" "N-ZA-Mn-za-m"
exit
```

Bandit 12 Level 13 Walkthrough
```console
xxd data.txt to analyse each compression method:
```
Zip starts with 0x50, 0x4b, 0x03, 0x04 (unless empty — then the last two are 0x05, 0x06 or 0x06, 0x06)
Gzip starts with 0x1f, 0x8b, 0x08
xz starts with 0xfd, 0x37, 0x7a, 0x58, 0x5a, 0x00
zlib starts with 0aaa1000 bbbccccc
Z starts with 0x1f, 0x9d
bzip2 starts with 0x42, 0x5a, 0x68

```console
xxd -r data.txt | gzip -d | bzip2 -d | gzip -d | tar -x | tar -x | bzip2 -d | tar -x | gzip -d
exit
```

Bandit 13 Level 14 Walkthrough
```console
ssh bandit14@localhost -i sshkey.private
cat /etc/bandit_pass/bandit14
exit
```

Bandit 14 Level 15 Walkthrough
```console
echo "4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e" | nc localhost 30000
```

Bandit 15 Level 16 Walkthrough
```console
ssh
```

Bandit 16 Level 17 Walkthrough
```console
ssh
```

Bandit 17 Level 18 Walkthrough
```console
ssh
```

Bandit 18 Level 19 Walkthrough
```console
ssh
```

Bandit 19 Level 20 Walkthrough
```console
ssh
```

Bandit 20 Level 21 Walkthrough
```console
ssh
```

Bandit 21 Level 22 Walkthrough
```console
ssh
```

Bandit 22 Level 23 Walkthrough
```console
ssh
```
Bandit 23 Level 24 Walkthrough
```console
ssh
```

Bandit 24 Level 25 Walkthrough
```console
ssh
```

Bandit 25 Level 26 Walkthrough
```console
ssh
```

Bandit 26 Level 27 Walkthrough
```console
ssh
```

Bandit 27 Level 28 Walkthrough
```console
ssh
```

Bandit 28 Level 29 Walkthrough
```console
ssh
```

Bandit 29 Level 30 Walkthrough
```console
ssh
```

Bandit 30 Level 31 Walkthrough
```console
ssh
```

Bandit 31 Level 32 Walkthrough
```console
ssh
```

Bandit 32 Level 33 Walkthrough
```console
ssh
```

Bandit 33 Level 34 Walkthrough
```console
ssh
```
