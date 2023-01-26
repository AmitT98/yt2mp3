import os
cmd1 = "mv *.mp3 music/"
cmd2 = "mv *.txt logs/"
for i in range(1,3):
	os.system(locals()["cmd"+str(i)])

