
import os, glob,sys
i = 0
search_extensions = ['txt','php','js','css','py','html','htm','ejs','ini','conf']
def find_text_in_files(word,path):
	global i
	if path == "":
		search = "*"
	else:
		search = "/*"	
	for f in glob.glob(path+search):
		if os.path.isdir(f):
			find_text_in_files(word,f)
		else:
			if f.split(".")[-1] not in search_extensions:
				continue
			i = i+1
			print i	
			d = open(f,'r').read()
			if word in d:
				print f
def main():				
	try:
		directory = sys.argv[2]
	except:
		directory = ""
	try:
		word  = sys.argv[1]
	except:
		print 'Please use like  find.py  "word to be search" "path to folder"'
		print "Now app going to intractive mode"
		word = False
		while not word:
			print "Enter word to be search"
			word = raw_input()							
	find_text_in_files(word,directory)
if __name__ == '__main__':
		main()	