# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 00:23:58 2020
Project Blue Notebook!
@author: A F Forughi
"""
import os
import random
import string

def file_secure_delete(opath, passes=1):
    if os.path.exists(opath):
        with open(opath, "ba+", buffering=0) as delfile:
            length = delfile.tell()
        delfile.close()
        with open(opath, "br+", buffering=0) as delfile:
            for i in range(passes):
                delfile.seek(0,0)
                delfile.write(os.urandom(length))
            
            # delfile.seek(0)
            # for x in range(length):
            #     delfile.write(b'\x00')
        delfile.close()
        
        name_length=len(opath)-opath.rfind('\\')-1+random.randint(0,5)
        rndname=''.join(random.choices(string.ascii_uppercase+string.ascii_lowercase + string.digits, k=name_length))
        newpath=opath[:opath.rfind('\\')+1]+rndname
        os.rename(opath,newpath)
        os.remove(newpath) # Delete must be done manually if your AV blocks this command.

def dir_secure_delete(opath):
    name_length=len(opath)-opath.rfind('\\')-1+random.randint(0,5)
    rndname=''.join(random.choices(string.ascii_uppercase+string.ascii_lowercase + string.digits, k=name_length))
    newpath=opath[:opath.rfind('\\')+1]+rndname
    os.rename(opath,newpath)
    os.rmdir(newpath) # Delete must be done manually if your AV blocks this command.

        
def wiper(head):
    ask=" "
    ask=input('Are you sure you want to wipe everything inside:\n'+head+"\nYes[YYY]: ")
    if ask=="YYY":
        err_files=[]
        err_dirs=[]
        n_file=0
        n_dir=0
        for root, dirs, files in os.walk(head, topdown=False): #For files
            root=root.replace("/","\\")
            for name in files:
                ofile=os.path.join(root, name)
                # ofile=ofile.replace("\\","\\\\")
                # print(ofile)
                try:
                    file_secure_delete(ofile)
                except:
                    err_files.append(ofile)
                else:
                    n_file+=1
        
        for root, dirs, files in os.walk(head, topdown=False): #For dirs
            for name in dirs:
                odir=os.path.join(root, name)
                # odir=dum.replace("\\","\\\\")
                # print(odir)
                try:
                    dir_secure_delete(odir)
                except:
                    err_dirs.append(odir)
                else:
                    n_dir+=1
                    
        print(n_file," files and ",n_dir," folders annihilated!")
        if len(err_dirs)+len(err_files)>0:
            print("Errors:\n",err_files,err_dirs)

wiper(r'C:\Users\f\Desktop\testfolder') # The target folder!



