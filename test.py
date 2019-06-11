#!/usr/bin/env python
# -*- coding: euc-jp -*-

import subprocess
import os


#subprocess.check_call("C:\\Users\\TyouK\\Documents\\GitHub\\build\\test\\src\\Release\\XXXTest.exe")
try:
    ret = subprocess.check_call("C:\\workspace\\build\\test\\src\\Release\\XXXTest.exe")
except subprocess.CalledProcessError as e:
    print(e.returncode)
    print(e.cmd)
    print(e.output)
except:
    print("error")