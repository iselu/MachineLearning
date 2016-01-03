# -*- coding:utf-8 -*-
__author__ = 'Administrator'

from recommendations import critics
from bs4 import BeautifulSoup
import requests
import os
import string
import re
import fileinput

print(critics['Lisa Rose']['Lady in the Water'])

f=open("D:\profile_f.txt")
i=0;
line=f.readline()
lines=f.readlines()

while i<10 and f:
    print(line)
    i=i+1
    line=f.readline()

f.close()
print(len(lines))



