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
        #print out
        #print reget.findall(out)
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

def NetPing(ip,PingTime):
    first = NetCheck(ip)
    Timelist = [first]
    if first < 0:
        #for i in range(PingTime-1):
        #    Timelist.append(first)
        return Timelist

    for i in range(PingTime-1):
        Timelist.append(NetCheck(ip))
    return Timelist

#print NetPing("59.78.20.232",10)
