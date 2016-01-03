# -*- coding: utf-8 -*-

import numpy as np

Z=np.zeros(10)
print Z

Z[4]=1
print Z

M=np.arange(10,99)#生成一个从10到99左闭右开的数组
print M

x=np.matrix(np.arange(9).reshape(3,3))
print x