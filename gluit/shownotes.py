import os, sys, inspect, string
from gluit import file_to_open,readfilelist,opennotes,delnotes, cpnotes, mvnotes
from subprocess import Popen, PIPE


def editor():
   proc1 = Popen(["which emacs"], stdout=PIPE, stderr=PIPE, shell=True)
   (out1, err) = proc1.communicate()
   proc2 = Popen(["which pico"], stdout=PIPE, stderr=PIPE, shell=True)
   (out2, err) = proc2.communicate()
   proc3 = Popen(["which vi"], stdout=PIPE, stderr=PIPE, shell=True)
   (out3, err) = proc3.communicate()
   if len(out1) >   0: return 'emacs'
   elif len(out2) > 0: return 'pico'
   elif len(out3) > 0: return 'vi'
   else:
       print 'no editor found!'
       exit()

dir='HOME'

scriptdir=os.getenv(dir)+'/GluIt/gluit/' 
if len(sys.argv)!=2:
  print 'usage: shownotes filename'
  exit()
file=file_to_open(os.getcwd( )+'/'+sys.argv[1])
count=readfilelist(scriptdir,file)
opennotes(file, scriptdir, count, editor())

