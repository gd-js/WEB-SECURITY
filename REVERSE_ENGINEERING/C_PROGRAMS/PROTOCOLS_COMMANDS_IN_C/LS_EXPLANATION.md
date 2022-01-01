- The code starts by declaring the variables that will be used.
- The first variable is a pointer to a struct dirent which is an entry in directory files.
- This struct dirent has three fields: d_name, d_type, and d_reclen.
- The second variable is a pointer to the DIR structure which can be used for reading directories.
- It also has three fields: dirh, opendir(), and readdir().

- The next function called _ls() will list all of the files in the current directory with their names and sizes on stdout (standard output).
- It starts by opening up the current directory using opendir() then it iterates through each file in this directory until it reaches one that isn't readable or doesn't exist.
- If there are any hidden files they are skipped over because they aren't listed on stdout so we continue onto printing out other entries from this directory's file list.
–
- The code is for a directory listing.

- The code starts by declaring the variables that will be used throughout the program.
- These include:

- -dirent *d;

- -DIR *dh = opendir(dir);

- -int errno;

- -int op_a,op_l;
