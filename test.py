#!/usr/bin/env python
# -*- coding: euc-jp -*-

print("aaaaabbbbb")
import os
import sys

with open("test.txt", mode='w') as f:
    f.write(str(os.environ["PATH"]))
    f.write(str(sys.argv))


