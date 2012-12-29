import os, sys, inspect, string
from gluit import file_to_open,readfilelist,opennotes,delnotes, cpnotes, mvnotes

#editor="emacs"  
dir='HOME'
if len(sys.argv)!=3:
  print 'usage: cpnotes file1 file2'
  exit()
scriptdir=os.getenv(dir)+'/GluIt/gluit/' 

file=file_to_open(os.getcwd( )+'/'+sys.argv[1])
count=readfilelist(scriptdir,file)
new_file= file_to_open(os.getcwd( )+'/'+sys.argv[2])  
new_count=readfilelist(scriptdir,new_file)
cpnotes(scriptdir, count, new_file, new_count)


