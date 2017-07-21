from subprocess import Popen
import glob

tests = glob.glob('selenium*.py')
processes = []
for test in tests:
	processes.append(Popen('python %s' % test, shell=True))

for process in processes:
	process.wait()