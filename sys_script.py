import re
from subprocess import Popen, PIPE

pwd = "Yaday@1991"
cmd = "ls".split()

proc1 = Popen(["sudo", "-S"] + cmd, stdin=PIPE, stdout=PIPE, universal_newlines=True)

extractor = proc1.communicate(pwd + "\n")[0]

m = re.findall(r"\w+", extractor)

print(m)