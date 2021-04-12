import sys
from tempfile import NamedTemporaryFile
from athenaCL.libATH import athenaObj

'''
Executes a single athenaCL command and returns the result as a string.
'''
def process_command(command):
    # Non-interactive interpretation.
    interpreter = athenaObj.Interpreter('cgi')
    return interpreter.cmd(command)

'''
Executes a list of one or more athenaCL commands and returns the results as a 
string.
'''
def process_commands(commands):
    interpreter = athenaObj.Interpreter()
    result = []
    for command in commands:
        result.append(interpreter.cmd(command))
    return result

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
	print("Error: Input Script Filename must be given")
else:
	process(args[1])
