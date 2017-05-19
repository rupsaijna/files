import csv
import os 
import argparse

parser = argparse.ArgumentParser(description='argParse')

parser.add_argument('-input',action="store", dest='inputfilename')
parser.add_argument('-output',action="store", dest='outputfilename')

args = parser.parse_args()
#inputfilename = sys.argv[1]
#outputfilename= sys.argv[2]
if os.path.exists(args.inputfilename):
	#inputfilename="../output/output_2203_project3.txt"
	#outputfilename="../output/output_final_2203_project3.txt"


	fp = open(args.inputfilename,'r')
	fo = open(args.outputfilename,'a+')

	write=[]
	sen=''
	cause=''
	effect=''
	connective=''
	cause_proc=''
	effect_proc=''
	conn_proc=''
	cause_proc_extended=''
	effect_proc_extended=''
	conn_proc_extended=''
	for line in fp:
		if line=='\n':
			write=[sen,cause,effect,connective,cause_proc,effect_proc,conn_proc,cause_proc_extended,effect_proc_extended, conn_proc_extended]
			fo.write(sen+','+cause+','+effect+','+connective+','+cause_proc+','+effect_proc+','+conn_proc+','+cause_proc_extended+','+effect_proc_extended+','+conn_proc_extended)
			fo.write('\n')
			print "write:",write
			write=[]
			sen=''
			cause=''
			effect=''
			connective=''
			cause_proc=''
			effect_proc=''
			conn_proc=''
			cause_proc_extended=''
			effect_proc_extended=''
			conn_proc_extended=''
		else:
			tokens=line.split()
			sen+=' '+tokens[0]
			if tokens[14]=='effect':
				effect+=' '+tokens[0]
				if 'V' in tokens[1] or 'NN' in tokens[1]:
					effect_proc+=' '+tokens[0]
				if 'V' in tokens[1] or 'N' in tokens[1] :
					effect_proc_extended+=' '+tokens[0]
			elif tokens[14]=='cause':
				cause+=' '+tokens[0]
				if 'V' in tokens[1] or 'NN' in tokens[1]:
					cause_proc+=' '+tokens[0]
				if 'V' in tokens[1] or 'N' in tokens[1]:
					cause_proc_extended+=' '+tokens[0]
			elif tokens[14]=='connective':
				connective+=' '+tokens[0]
				if 'V' in tokens[1] or 'NN' in tokens[1]:
					conn_proc+=' '+tokens[0]
				if 'V' in tokens[1] or 'N' in tokens[1]:
					conn_proc_extended+=' '+tokens[0]
else:
	print "input file not found"
