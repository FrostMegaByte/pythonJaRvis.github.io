# @Time : 2022/9/13 10:15
# @Author : yixuanYan
# from insider import A , B,C,D,E
from insider import *

if True:
    a = A
    a()
else:
    if True:
        a = B
    else:
        if True:
            a = C
            a()
        else:
            if True:
                a = D
                a()
            else:
                a = E
