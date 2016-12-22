#!/usr/bin/env python
#-*- coding: utf-8 -*-
import os,sys,re
import subprocess

def NetCheck(ip):
    try:
        p = subprocess.Popen(["ping -c 1 -W 1 "+ ip],stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
        out=p.stdout.read()
    #err=p.stderr.read()
        regex=re.compile('100.0% packet loss')
    #print out
    #print regex
    #print err
        if len(regex.findall(out)) == 0:
            #print ip + ': host up'
            lines = out.split('\n')
            #print lines[-2]
            nums = lines[-2].split('/')
            num = nums[-2]
            #print num
            return float(num)
        else:
            #print ip + ': host down'
            return -1
    except:
        #print 'NetCheck work error!'
        return -2



print NetCheck("114.80.68.233")
