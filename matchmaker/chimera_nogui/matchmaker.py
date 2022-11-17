import os
from chimera import runCommand as rc
from chimera import replyobj

# os.chdir("")

fn1 = "af.pdb"
fn2 = "ab.pdb"

rc("open " + fn2)
rc("open " + fn1)
rc("del :1-217")
rc("del :293-395")

rc("mm #0 #1")
 
