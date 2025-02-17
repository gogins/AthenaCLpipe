import sys
from tempfile import NamedTemporaryFile
from athenaCL.libATH import athenaObj

'''
Processes a user-specified file of athenaCL commands, to print a 
Csound score file.
'''
def process(infile):
	fin = open(infile, "r")
	cmd = []	

	for line in fin:
		cmd.append(line.split('#')[0].strip())

	a = NamedTemporaryFile()	
	foutName = a.name
	a.close()

	cmd.append("ELn %s.xml"%foutName)

	ai = athenaObj.Interpreter('cgi')
	for c in cmd:
		ai.cmd(c)

	a = open(foutName + ".sco", "r")

	for line in a.readlines():
		print(line)


args = sys.argv

if len(args) != 2:
	print("Error: Input script filename must be given")
else:
	process(args[1])
