# Disk Image Analysis Cheat Sheet
```
sudo apt install autopsy
sudo apt install fdisk
sudo apt install testdisk
```
autopsy
```
usage: /usr/bin/autopsy [-c] [-C] [-d evid_locker] [-i device filesystem mnt] [-p port] [remoteaddr]
  -c: force a cookie in the URL
  -C: force NO cookie in the URL
  -d dir: specify the evidence locker directory
  -i device filesystem mnt: Specify info for live analysis
  -p port: specify the server port (default: 9999)
  remoteaddr: specify the host with the browser (default: localhost)
```
fdisk
```
Usage:
 fdisk [options] <disk>         change partition table
 fdisk [options] -l [<disk>...] list partition table(s)

Display or manipulate a disk partition table.

Options:
 -b, --sector-size <size>      physical and logical sector size
 -B, --protect-boot            don't erase bootbits when creating a new label
 -c, --compatibility[=<mode>]  mode is 'dos' or 'nondos' (default)
 -L, --color[=<when>]          colorize output (auto, always or never)
                                 colors are enabled by default
 -l, --list                    display partitions and exit
 -x, --list-details            like --list but with more details
 -n, --noauto-pt               don't create default partition table on empty devices
 -o, --output <list>           output columns
 -t, --type <type>             recognize specified partition table type only
 -u, --units[=<unit>]          display units: 'cylinders' or 'sectors' (default)
 -s, --getsz                   display device size in 512-byte sectors [DEPRECATED]
     --bytes                   print SIZE in bytes rather than in human readable format
     --lock[=<mode>]           use exclusive device lock (yes, no or nonblock)
 -w, --wipe <mode>             wipe signatures (auto, always or never)
 -W, --wipe-partitions <mode>  wipe signatures from new partitions (auto, always or never)

 -C, --cylinders <number>      specify the number of cylinders
 -H, --heads <number>          specify the number of heads
 -S, --sectors <number>        specify the number of sectors per track

 -h, --help                    display this help
 -V, --version                 display version

Available output columns:
 gpt: Device Start End Sectors Size Type Type-UUID Attrs Name UUID
 dos: Device Start End Sectors Cylinders Size Type Id Attrs Boot End-C/H/S
      Start-C/H/S
 bsd: Slice Start End Sectors Cylinders Size Type Bsize Cpg Fsize
 sgi: Device Start End Sectors Cylinders Size Type Id Attrs
 sun: Device Start End Sectors Cylinders Size Type Id Flags
```
testdisk
```
testdisk [/log] [/debug] [file.dd|file.e01|device]
       testdisk /list  [/log]   [file.dd|file.e01|device]
       testdisk /version

/log          : create a testdisk.log file
/debug        : add debug information
/list         : display current partitions

TestDisk checks and recovers lost partitions
It works with :
- BeFS (BeOS)                           - BSD disklabel (Free/Open/Net BSD)
- CramFS, Compressed File System        - DOS/Windows FAT12, FAT16 and FAT32
- XBox FATX                             - Windows exFAT
- HFS, HFS+, Hierarchical File System   - JFS, IBM's Journaled File System
- Linux btrfs                           - Linux ext2, ext3 and ext4
- Linux GFS2                            - Linux LUKS
- Linux Raid                            - Linux Swap
- LVM, LVM2, Logical Volume Manager     - Netware NSS
- Windows NTFS                          - ReiserFS 3.5, 3.6 and 4
- Sun Solaris i386 disklabel            - UFS and UFS2 (Sun/BSD/...)
- XFS, SGI's Journaled File System      - Wii WBFS
- Sun ZFS

```
