## Shell commands

`<command> man` to see help (the manual) for a command

`mv` move/rename a file or directory 

`cp` copy a file. Use -r to copy multiple files (recursion) e.g. `cp -r ./target_dir/* destination_dir/`

`rm` remove (delete) a file or `rmdir` to remove a directory -f to force (-v verbose?). A good habit is to do `rm ./some/path/* -rf` rather than `rm -rf./some/path/* ` to avoid disasterous path accidents!

`touch` creates a file at the supplied location

`history` previously run command

`clear` clear the terminal screen

`less` show the contents of a file in a paginated manner.

`tail` show the end of a supplied file.

`tree <dir>`

**globbing** is the name for referring to files with a regex e.g. using wildcard `*` or `/file.jp?g` (these are globbing expressions).

`diff` compares two files and gives the differences. `colordiff` for colour coded diff

### Setting Aliases

`alias <alias_name>="<command>"`

for example:

`alias ll="ls -lah"` 

Just doing in the shell will only keep the changes for that terminal session. To change permanently, update in config file.

### Permissions

![permissions diagram](http://linuxcommand.org/images/file_permissions.png)

when viewing full info for a file, see a string representing the permissions for that file.

#### Setting permissions

To change permissions, use `chmod`. 

##### Setting permissions with string 

Targets: **u**ser, **g**roup, **a**nyone 

Access type: r, w, x execute

e.g. `chmod a+rw file.py` gives everyone read/write permission for file.py

##### Octal

Can also set permissions numerically using octal 

| #    | Permission             | Str  | Bin  |
| ---- | ---------------------- | ---- | ---- |
| 7    | read, write, & execute | rwx  | 111  |
| 6    | read & write           | rw-  | 110  |
| 5    | read & execute         | r-x  | 101  |
| 4    | read only              | r--  | 100  |
| 3    | write & execute        | -wx  | 011  |
| 2    | write only             | -w-  | 010  |
| 1    | executable only        | --x  | 001  |

so read access to everyone would be 0 0 4

e.g. `chmod 777 file.py` gives all people permission to read, write, and execute file.py

e.g. `chmod 700 file.py` owner can do anything, no one else can access.

To view file permissions in octal, `stat -f '%A %a %N' <thefile> `

### Superuser

`su` allows you to log in as the super user. Probably please **don't**.

`sudo` allows a regular user to temporarily become the super user for a command, e.g. `sudo cp file.py /bin/`

### Passing information

`fortune > fortune.txt` writes the output of the commend fortune (imparts some random wisdom) into the file fortune.txt. Will create the file if it doesn't exist or overwrite the content of it if it does. 

#### Apppending to a file

`fortune >> fortune.txt`

Will append content of fortune to the end of fortune.txt file.

#### Piping

Can pass the output of one command as input to another command using the pipe operator `|`.

e.g. `cat long_file.txt | less` or  `history | tail`

Can chain these:

e.g. `cat long_file.txt | text_filter.py | less`

### Finding files

`grep` searches text files for a given string e.g. `grep "foo" ./dir/*.txt`. Useful flags are `-i` case insensitive, `-r` for recursive e.g. `grep -r "foo" ./dir/` 

Can find a file using `search`

sort results with `sort`

### Text editors

`nano` is one

`vim` can learn using `vimtutor`

### Shell config file is 

`.bashrc` which is loaded ever time you open a new terminal

/User/?

Can define variables (like aliases or environment variables) in the config. May need to close & reopen any open terminals to update.

$PATH is a list of all the places in your computer where executable are stored.

$HISTSIZE how many commands do you want the command history to remember?

`export EDITOR=vim`

`env` to see all environment variables.

## OOP

**Encapsulation** - hiding things for the sake of simplicity (and minimising cognitial load)

private and public code for objects. Private code usually for internal messiness a user wouldn't care about/shouldn't access. Python not great at this!

**Inheritance**

**Abstraction**

**Polymorphism**

## Working in a team

