import os, sys, inspect, string
def file_to_open(filename):
    frame = sys._getframe(1)
    if hasattr(frame, "_frame"):
        frame = frame._frame
    filetoopen= os.path.abspath(os.path.join(os.path.dirname(inspect.getfile(frame)), filename))
    return filetoopen

def readfilelist(scriptdir,fileopen):
    dirfile= scriptdir+"dirfile.txt"
    if os.path.exists(dirfile) == True:
       fout = open(dirfile,"r")
       line=fout.readlines()  
       fout.close()   
       linecount=0
       case=False       

       for data in line:
         ctr=0
         if(len(data) >=len(fileopen)): length=len(fileopen)
         else: length=len(data)
         for i in range(0,length):
           if data[i]==fileopen[i]:
             ctr=ctr+1
         if(ctr==len(fileopen)):
            case==True
            return linecount
         linecount=linecount+1
         
       if case== False:
            with open(dirfile, "a") as myfile:
              myfile.write("%s\n"% fileopen)
       return linecount

def opennotes(filetoopen, scriptdir, line_count, editor):
    outfile= scriptdir+"Notes/"+str(line_count)+"_notes"
    if os.path.exists(outfile) == False:
      fout= open(outfile,"w")
      print>>fout,"# this file contain notes for ",filetoopen
      fout.close()    
    os.system(editor + ' ' + outfile)

def delnotes(scriptdir, line_count):
    outfile= scriptdir+"Notes/"+str(line_count)+"_notes"
    os.system('rm -f  ' + outfile)

def cpnotes(scriptdir, line_count, new_file, new_count):
    outfile= scriptdir+"Notes/"+str(line_count)+"_notes"
    new_outfile= scriptdir+"Notes/"+str(new_count)+"_notes"
    os.system('cp -f  ' + outfile+' '+new_outfile)
    fout= open(new_outfile,"a")
    print>>fout,"\n \n\n# Now this file contain notes for ",new_file
    fout.close() 
#    opennotes(new_outfile, scriptdir, new_count, editor)

def mvnotes(scriptdir,line_count):
    new_file= file_to_open(os.getcwd( )+'/'+sys.argv[2])  
    dirfile= scriptdir+"dirfile.txt"
    fout = open(dirfile,"r")
    line=fout.readlines()  
    fout.close()  
    os.system('cp -f  ' + dirfile+' '+dirfile+'.bkp')
    with open(dirfile, "w") as myfile:
      ctr=0
      for data in line:
        if(ctr!=line_count): myfile.write("%s"% data)    
        else: myfile.write("%s\n"% new_file) 
        ctr=ctr+1  
    myfile.close()  
    outfile= scriptdir+"Notes/"+str(line_count)+"_notes"
    new_outfile= scriptdir+"Notes/"+str(len(line)-1)+"_notes"
    os.system('mv -f  ' + outfile+' '+new_outfile)

   
