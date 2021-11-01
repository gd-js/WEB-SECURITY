# File Analysis Cheat Sheet Linux
```
#xxd
#strings
sudo apt install binwalk
sudo apt install file
sudo apt install exiftool
sudo apt install foremost
sudo apt install pngcheck
sudo apt install ffmpeg
```
xxd
```
Usage:
       xxd [options] [infile [outfile]]
    or
       xxd -r [-s [-]offset] [-c cols] [-ps] [infile [outfile]]
Options:
    -a          toggle autoskip: A single '*' replaces nul-lines. Default off.
    -b          binary digit dump (incompatible with -ps,-i,-r). Default hex.
    -C          capitalize variable names in C include file style (-i).
    -c cols     format <cols> octets per line. Default 16 (-i: v12, -ps: 30).
    -E          show characters in EBCDIC. Default ASCII.
    -e          little-endian dump (incompatible with -ps,-i,-r).
    -g          number of octets per group in normal output. Default 2 (-e: 4).
    -h          print this summary.
    -i          output in C include file style.
    -l len      stop after <len> octets.
    -o off      add <off> to the displayed file position.
    -ps         output in postscript plain hexdump style.
    -r          reverse operation: convert (or patch) hexdump into binary.
    -r -s off   revert with <off> added to file positions found in hexdump.
    -d          show offset in decimal instead of hex.
    -s [+][-]seek  start at <seek> bytes abs. (or +: rel.) infile offset.
    -u          use upper case hex letters.
    -v          show version: "xxd V1.10 27oct98 by Juergen Weigert".
```
strings
```
Usage: strings [option(s)] [file(s)]
 Display printable strings in [file(s)] (stdin by default)
 The options are:
  -a - --all                Scan the entire file, not just the data section [default]
  -d --data                 Only scan the data sections in the file
  -f --print-file-name      Print the name of the file before each string
  -n --bytes=[number]       Locate & print any NUL-terminated sequence of at
  -<number>                   least [number] characters (default 4).
  -t --radix={o,d,x}        Print the location of the string in base 8, 10 or 16
  -w --include-all-whitespace Include all whitespace as valid string characters
  -o                        An alias for --radix=o
  -T --target=<BFDNAME>     Specify the binary file format
  -e --encoding={s,S,b,l,B,L} Select character size and endianness:
                            s = 7-bit, S = 8-bit, {b,l} = 16-bit, {B,L} = 32-bit
  -s --output-separator=<string> String used to separate strings in output.
  @<file>                   Read options from <file>
  -h --help                 Display this information
  -v -V --version           Print the program's version number
strings: supported targets: elf64-x86-64 elf32-i386 elf32-iamcu elf32-x86-64 pei-i386 pe-x86-64 pei-x86-64 elf64-l1om elf64-k1om elf64-little elf64-big elf32-little elf32-big pe-bigobj-x86-64 pe-i386 srec symbolsrec verilog tekhex binary ihex plugin
```
file
```
Usage: file [OPTION...] [FILE...]
Determine type of FILEs.

      --help                 display this help and exit
  -v, --version              output version information and exit
  -m, --magic-file LIST      use LIST as a colon-separated list of magic
                               number files
  -z, --uncompress           try to look inside compressed files
  -Z, --uncompress-noreport  only print the contents of compressed files
  -b, --brief                do not prepend filenames to output lines
  -c, --checking-printout    print the parsed form of the magic file, use in
                               conjunction with -m to debug a new magic file
                               before installing it
  -e, --exclude TEST         exclude TEST from the list of test to be
                               performed for file. Valid tests are:
                               apptype, ascii, cdf, compress, csv, elf,
                               encoding, soft, tar, json, text,
                               tokens
      --exclude-quiet TEST         like exclude, but ignore unknown tests
  -f, --files-from FILE      read the filenames to be examined from FILE
  -F, --separator STRING     use string as separator instead of `:'
  -i, --mime                 output MIME type strings (--mime-type and
                               --mime-encoding)
      --apple                output the Apple CREATOR/TYPE
      --extension            output a slash-separated list of extensions
      --mime-type            output the MIME type
      --mime-encoding        output the MIME encoding
  -k, --keep-going           don't stop at the first match
  -l, --list                 list magic strength
  -L, --dereference          follow symlinks (default if POSIXLY_CORRECT is set)
  -h, --no-dereference       don't follow symlinks (default if POSIXLY_CORRECT is not set) (default)
  -n, --no-buffer            do not buffer output
  -N, --no-pad               do not pad output
  -0, --print0               terminate filenames with ASCII NUL
  -p, --preserve-date        preserve access times on files
  -P, --parameter            set file engine parameter limits
                                   bytes 1048576 max bytes to look inside file
                               elf_notes     256 max ELF notes processed
                               elf_phnum    2048 max ELF prog sections processed
                               elf_shnum   32768 max ELF sections processed
                                   indir      50 recursion limit for indirection
                                    name      50 use limit for name/use magic
                                   regex    8192 length limit for REGEX searches
  -r, --raw                  don't translate unprintable chars to \ooo
  -s, --special-files        treat special (block/char devices) files as
                             ordinary ones
  -S, --no-sandbox           disable system call sandboxing
  -C, --compile              compile file specified by -m
  -d, --debug                print debugging messages
```
binwalk
```
binwalk -eBEW -raw="\string\"
Usage: binwalk [OPTIONS] [FILE1] [FILE2] [FILE3] ...

Signature Scan Options:
-B, --signature              Scan target file(s) for common file signatures
-R, --raw=<str>              Scan target file(s) for the specified sequence of bytes
-A, --opcodes                Scan target file(s) for common executable opcode signatures
-m, --magic=<file>           Specify a custom magic file to use
-b, --dumb                   Disable smart signature keywords
-I, --invalid                Show results marked as invalid
-x, --exclude=<str>          Exclude results that match <str>
-y, --include=<str>          Only show results that match <str>

Extraction Options:
-e, --extract                Automatically extract known file types
-D, --dd=<type[:ext[:cmd]]>  Extract <type> signatures (regular expression), give the files an extension of <ext>, and execute <cmd>
-M, --matryoshka             Recursively scan extracted files
-d, --depth=<int>            Limit matryoshka recursion depth (default: 8 levels deep)
-C, --directory=<str>        Extract files/folders to a custom directory (default: current working directory)
-j, --size=<int>             Limit the size of each extracted file
-n, --count=<int>            Limit the number of extracted files
-r, --rm                     Delete carved files after extraction
-z, --carve                  Carve data from files, but don't execute extraction utilities
-V, --subdirs                Extract into sub-directories named by the offset

Entropy Options:
-E, --entropy                Calculate file entropy
-F, --fast                   Use faster, but less detailed, entropy analysis
-J, --save                   Save plot as a PNG
-Q, --nlegend                Omit the legend from the entropy plot graph
-N, --nplot                  Do not generate an entropy plot graph
-H, --high=<float>           Set the rising edge entropy trigger threshold (default: 0.95)
-L, --low=<float>            Set the falling edge entropy trigger threshold (default: 0.85)

Binary Diffing Options:
-W, --hexdump                Perform a hexdump / diff of a file or files
-G, --green                  Only show lines containing bytes that are the same among all files
-i, --red                    Only show lines containing bytes that are different among all files
-U, --blue                   Only show lines containing bytes that are different among some files
-u, --similar                Only display lines that are the same between all files
-w, --terse                  Diff all files, but only display a hex dump of the first file

Raw Compression Options:
-X, --deflate                Scan for raw deflate compression streams
-Z, --lzma                   Scan for raw LZMA compression streams
-P, --partial                Perform a superficial, but faster, scan
-S, --stop                   Stop after the first result

General Options:
-l, --length=<int>           Number of bytes to scan
-o, --offset=<int>           Start scan at this file offset
-O, --base=<int>             Add a base address to all printed offsets
-K, --block=<int>            Set file block size
-g, --swap=<int>             Reverse every n bytes before scanning
-f, --log=<file>             Log results to file
-c, --csv                    Log results to file in CSV format
-t, --term                   Format output to fit the terminal window
-q, --quiet                  Suppress output to stdout
-v, --verbose                Enable verbose output
-h, --help                   Show help output
-a, --finclude=<str>         Only scan files whose names match this regex
-p, --fexclude=<str>         Do not scan files whose names match this regex
-s, --status=<int>           Enable the status server on the specified port
```
exiftool
```
exiftool [OPTIONS] FILE
-args       (-argFormat)         Format metadata as exiftool arguments
 -b          (-binary)            Output metadata in binary format
 -c FMT      (-coordFormat)       Set format for GPS coordinates
 -charset [[TYPE=]CHARSET]        Specify encoding for special characters
 -csv[[+]=CSVFILE]                Export/import tags in CSV format
 -csvDelim STR                    Set delimiter for CSV file
 -d FMT      (-dateFormat)        Set format for date/time values
 -D          (-decimal)           Show tag ID numbers in decimal
 -E,-ex,-ec  (-escape(HTML|XML|C))Escape tag values for HTML, XML or C
 -f          (-forcePrint)        Force printing of all specified tags
 -g[NUM...]  (-groupHeadings)     Organize output by tag group
 -G[NUM...]  (-groupNames)        Print group name for each tag
 -h          (-htmlFormat)        Use HTML formatting for output
 -H          (-hex)               Show tag ID numbers in hexadecimal
 -htmlDump[OFFSET]                Generate HTML-format binary dump
 -j[[+]=JSONFILE] (-json)         Export/import tags in JSON format
 -l          (-long)              Use long 2-line output format
 -L          (-latin)             Use Windows Latin1 encoding
 -lang [LANG]                     Set current language
 -listItem INDEX                  Extract specific item from a list
 -n          (--printConv)        No print conversion
 -p FMTFILE  (-printFormat)       Print output in specified format
 -php                             Export tags as a PHP Array
 -s[NUM]     (-short)             Short output format
 -S          (-veryShort)         Very short output format
 -sep STR    (-separator)         Set separator string for list items
 -sort                            Sort output alphabetically
 -struct                          Enable output of structured information
 -t          (-tab)               Output in tab-delimited list format
 -T          (-table)             Output in tabular format
 -v[NUM]     (-verbose)           Print verbose messages
 -w[+|!] EXT (-textOut)           Write (or overwrite!) output text files
 -W[+|!] FMT (-tagOut)            Write output text file for each tag
 -Wext EXT   (-tagOutExt)         Write only specified file types with -W
 -X          (-xmlFormat)         Use RDF/XML output format

Processing control

 -a          (-duplicates)        Allow duplicate tags to be extracted
 -e          (--composite)        Do not generate composite tags
 -ee[NUM]    (-extractEmbedded)   Extract information from embedded files
 -ext[+] EXT (-extension)         Process files with specified extension
 -F[OFFSET]  (-fixBase)           Fix the base for maker notes offsets
 -fast[NUM]                       Increase speed when extracting metadata
 -fileOrder[NUM] [-]TAG           Set file processing order
 -i DIR      (-ignore)            Ignore specified directory name
 -if[NUM] EXPR                    Conditionally process files
 -m          (-ignoreMinorErrors) Ignore minor errors and warnings
 -o OUTFILE  (-out)               Set output file or directory name
 -overwrite_original              Overwrite original by renaming tmp file
 -overwrite_original_in_place     Overwrite original by copying tmp file
 -P          (-preserve)          Preserve file modification date/time
 -password PASSWD                 Password for processing protected files
 -progress[:[TITLE]]              Show file progress count
 -q          (-quiet)             Quiet processing
 -r[.]       (-recurse)           Recursively process subdirectories
 -scanForXMP                      Brute force XMP scan
 -u          (-unknown)           Extract unknown tags
 -U          (-unknown2)          Extract unknown binary tags too
 -wm MODE    (-writeMode)         Set mode for writing/creating tags
 -z          (-zip)               Read/write compressed information
Other options

 -@ ARGFILE                       Read command-line arguments from file
 -k          (-pause)             Pause before terminating
 -list[w|f|wf|g[NUM]|d|x]         List various exiftool capabilities
 -ver                             Print exiftool version number

Special features

 -geotag TRKFILE                  Geotag images from specified GPS log
 -globalTimeShift SHIFT           Shift all formatted date/time values
 -use MODULE                      Add features from plug-in module

Utilities

 -delete_original[!]              Delete "_original" backups
 -restore_original                Restore from "_original" backups

Advanced options

 -api OPT[[^]=[VAL]]              Set ExifTool API option
 -common_args                     Define common arguments
 -config CFGFILE                  Specify configuration file name
 -echo[NUM] TEXT                  Echo text to stdout or stderr
 -efile[NUM][!] ERRFILE           Save names of files with errors
 -execute[NUM]                    Execute multiple commands on one line
 -list_dir                        List directories, not their contents
 -srcfile FMT                     Process a different source file
 -stay_open FLAG                  Keep reading -@ argfile even after EOF
 -userParam PARAM[[^]=[VAL]]      Set user parameter (API UserParam opt)
```
```
foremost
```
$ foremost [-v|-V|-h|-T|-Q|-q|-a|-w-d] [-t <type>] [-s <blocks>] [-k <size>]
	[-b <size>] [-c <file>] [-o <dir>] [-i <file]

-V  - display copyright information and exit
-t  - specify file type.  (-t jpeg,pdf ...)
-d  - turn on indirect block detection (for UNIX file-systems)
-i  - specify input file (default is stdin)
-a  - Write all headers, perform no error detection (corrupted files)
-w  - Only write the audit file, do not write any detected files to the disk
-o  - set output directory (defaults to output)
-c  - set configuration file to use (defaults to foremost.conf)
-q  - enables quick mode. Search are performed on 512 byte boundaries.
-Q  - enables quiet mode. Suppress output messages.
-v  - verbose mode. Logs all messages to screen
```
pngcheck
```
Usage:  pngcheck [-7cfpqtv] file.{png|jng|mng} [file2.{png|jng|mng} [...]]
   or:  ... | pngcheck [-7cfpqstvx]
   or:  pngcheck [-7cfpqstvx] file-containing-PNGs...

Options:
   -7  print contents of tEXt chunks, escape chars >=128 (for 7-bit terminals)
   -c  colorize output (for ANSI terminals)
   -f  force continuation even after major errors
   -p  print contents of PLTE, tRNS, hIST, sPLT and PPLT (can be used with -q)
   -q  test quietly (output only errors)
   -s  search for PNGs within another file
   -t  print contents of tEXt chunks (can be used with -q)
   -v  test verbosely (print most chunk data)
   -vv test very verbosely (decode & print line filters)
   -w  suppress windowBits test (more-stringent compression check)
   -x  search for PNGs within another file and extract them when found
```
ffmpeg
```
Global options (affect whole program instead of just one file):
-loglevel loglevel  set logging level
-v loglevel         set logging level
-report             generate a report
-max_alloc bytes    set maximum size of a single allocated block
-y                  overwrite output files
-n                  never overwrite output files
-ignore_unknown     Ignore unknown stream types
-filter_threads     number of non-complex filter threads
-filter_complex_threads  number of threads for -filter_complex
-stats              print progress report during encoding
-max_error_rate maximum error rate  ratio of errors (0.0: no errors, 1.0: 100% errors) above which ffmpeg returns an error instead of success.
-bits_per_raw_sample number  set the number of bits per raw sample
-vol volume         change audio volume (256=normal)

Per-file main options:
-f fmt              force format
-c codec            codec name
-codec codec        codec name
-pre preset         preset name
-map_metadata outfile[,metadata]:infile[,metadata]  set metadata information of outfile from infile
-t duration         record or transcode "duration" seconds of audio/video
-to time_stop       record or transcode stop time
-fs limit_size      set the limit file size in bytes
-ss time_off        set the start time offset
-sseof time_off     set the start time offset relative to EOF
-seek_timestamp     enable/disable seeking by timestamp with -ss
-timestamp time     set the recording timestamp ('now' to set the current time)
-metadata string=string  add metadata
-program title=string:st=number...  add program with specified streams
-target type        specify target file type ("vcd", "svcd", "dvd", "dv" or "dv50" with optional prefixes "pal-", "ntsc-" or "film-")
-apad               audio pad
-frames number      set the number of frames to output
-filter filter_graph  set stream filtergraph
-filter_script filename  read stream filtergraph description from a file
-reinit_filter      reinit filtergraph on input parameter changes
-discard            discard
-disposition        disposition

Video options:
-vframes number     set the number of video frames to output
-r rate             set frame rate (Hz value, fraction or abbreviation)
-s size             set frame size (WxH or abbreviation)
-aspect aspect      set aspect ratio (4:3, 16:9 or 1.3333, 1.7777)
-bits_per_raw_sample number  set the number of bits per raw sample
-vn                 disable video
-vcodec codec       force video codec ('copy' to copy stream)
-timecode hh:mm:ss[:;.]ff  set initial TimeCode value.
-pass n             select the pass number (1 to 3)
-vf filter_graph    set video filters
-ab bitrate         audio bitrate (please use -b:a)
-b bitrate          video bitrate (please use -b:v)
-dn                 disable data

Audio options:
-aframes number     set the number of audio frames to output
-aq quality         set audio quality (codec-specific)
-ar rate            set audio sampling rate (in Hz)
-ac channels        set number of audio channels
-an                 disable audio
-acodec codec       force audio codec ('copy' to copy stream)
-vol volume         change audio volume (256=normal)
-af filter_graph    set audio filters

Subtitle options:
-s size             set frame size (WxH or abbreviation)
-sn                 disable subtitle
-scodec codec       force subtitle codec ('copy' to copy stream)
-stag fourcc/tag    force subtitle tag/fourcc
-fix_sub_duration   fix subtitles duration
-canvas_size size   set canvas size (WxH or abbreviation)
-spre preset        set the subtitle options to the indicated preset
```
