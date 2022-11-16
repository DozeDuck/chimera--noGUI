import os
from chimera import runCommand as rc
from chimera import replyobj

# os.chdir("")

fn1 = "0_af.pdb"
fn2 = "0_ab.pdb"

rc("open " + fn2)
rc("open " + fn1)
rc("mm #0 #1")

