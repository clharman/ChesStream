#TO DO
#	make engine an argument of init_engine

from subprocess import *

engine = Popen(
	'stockfish-dd-64-modern.exe',
    universal_newlines=True,
	stdin=PIPE,
	stdout=PIPE,
)

def put(command):
    engine.stdin.write(command+'\n')

def get():
    # using the 'isready' command (engine has to answer 'readyok')
    # to indicate current last line of stdout
    engine.stdin.write('isready\n')
    output = ''
    while True:
        text = engine.stdout.readline()
        if 'readyok' in text:
            return output
        if text.strip() !='':
            output += text