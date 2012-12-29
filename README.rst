=========
GluIt 

Author: Suman bhattacharya
=========
GluIt is a package  built using Python that help create and manage notes for  files. The notes are linked to that file and  thus the notes created can be found easily. The current version works on the terminal as a command line interface.

GluIt is released under the MIT software liscense (see LISCENSE).



Motivation
----------

Just like we can stick notes to files in physical world containing informations or instructions about that file, I wanted to create a similar utility for the files in our computers. Something that will allow us to create small notes about the files and that will stick to it.

Example
-------

shownotes (or sn) <filename>: opens the notes corresponding to the filename
delnotes (or dn) <filename> : delete the notes corresponding to the filename
cpnotes (or cn) <filename1> <filename2>: copy the notes of filename1 to filename 2
mvnotes (or mn) <filename1> <filename2>: move the notes of filename1 to filename 2

Prerequisites
=============

  Python
  terminal
  atleast one of the shell profiles (e.g., .bash, .csh*, .tcsh* etc)

Installation 
============

1. download the source and place the tar ball in your home directory and untar it.

2. open a terminal, if you don't know which shell the terminal is running on, you can find out by typing 
>find ~/.bash*
should print
/Users/Suman/.bash_history
/Users/Suman/.bash_profile
/Users/Suman/.bash_profile.ext
/Users/Suman/.bash_profile.ext~

etc..
Similarly  for csh shell type find ~/.csh* 

3. at the directory GluIt, run 'python set_up.py shell_profile_file'
where shell_profile_file is the .bash or .cshrc or .tchrc file that are typically placed in your home directory.( see step 2)
A typical example would be 
>python set_up.py ~/.bash_profile 

This step creates the alias for the shortcut commands that calls the python routines.

4. open a new terminal and start using GluIt (opening a terminal should automatically source the alias commands in file bash_aliases_gluit) 

Testing
=======
A good way to test this is to open a new terminal and type 
> shownotes (or sn)
which print on the terminal:
usage: shownotes filename
Similarly for other commands:
> delnotes (or dn)
usage: delnotes filename
>mvnotes (or mn)
usage: mvnotes file1 file2
>cpnotes (or cn)
usage: cpnotes file1 file2

Here file (s) are the name of the files for which you want to create the notes or delete the notes or mv/cp notes of one file to another.
