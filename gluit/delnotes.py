import os, sys, inspect, string
from gluit import file_to_open,readfilelist,opennotes,delnotes, cpnotes, mvnotes

dir='HOME'
if len(sys.argv)!=2:
  print 'usage: delnotes filename'
  exit()
file=file_to_open(os.getcwd( )+'/'+sys.argv[1])
scriptdir=os.getenv(dir)+'/GluIt/gluit/' 
#editor="emacs"
count=readfilelist(scriptdir,file)
delnotes(scriptdir, count)

