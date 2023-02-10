import os
from chimera import runCommand as rc
from chimera import replyobj

for i in range(500, 93000, 500):
    fn1 = "forward_" + str(i) + ".pdb"
    rc("open " +  fn1)
    rc("del element.H")
    rc("write #0 " + fn1 + "_delH.pdb")
