import os, sys

dir='HOME'
glushellfile= os.getenv(dir)+'/GluIt/bash_aliases_gluit'
os.system("chmod +x "+glushellfile)
os.system("chmod +x gluit/*")
bashfile=sys.argv[1]
os.system("echo 'source '"+glushellfile+ ">>"+bashfile)

