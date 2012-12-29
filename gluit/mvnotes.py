import os, sys, inspect, string
from gluit import file_to_open,readfilelist,opennotes,delnotes, cpnotes, mvnotes

dir='HOME'
if len(sys.argv)!=3:
  print 'usage: mvnotes file1 file2'
  exit()
file=file_to_open(os.getcwd( )+'/'+sys.argv[1])
scriptdir=os.getenv(dir)+'/GluIt/gluit/'
count=readfilelist(scriptdir,file)
mvnotes(scriptdir, count)

