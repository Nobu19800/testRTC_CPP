#!/usr/bin/env python
# -*- coding: euc-jp -*-

print("aaaaabbbbb")
import os


with open("test.txt", mode='w') as f:
    f.write(str(os.environ))