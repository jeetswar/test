# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 19:14:45 2021

@author: bijee
"""
inp_list = [0, 1, 3, 50, 75]
out_lst = []
up = 99
low = 0
for i in range(low,up + 1):
    if i not in inp_list:
        out_lst.append(i)
        
print(out_lst)