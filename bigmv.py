import os.path as op
import os

#files faut qu'il soit sous la forme /my/file
#path faut qu'il soit sous la forme /my/path
def bigmv(file,path):
	a=op.exists(path)
	if a==True:
		os.system(f"mv {file} {path} ")
	if a==False:
		os.system(f"mkdir {path} ") 
		os.system(f" mv {file} {path} ")
