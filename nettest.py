#!/usr/bin/python
# coding: UTF-8
import os,sys,re
import subprocess

import string

def TraceCheck(ip,MaxTTL):
    try:
        p = subprocess.Popen(["traceroute -m "+ str(MaxTTL)+ " " + ip],stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
        out=p.stdout.readlines()
    #err=p.stderr.read()
        #regex=re.compile('100.0% packet loss')
    #print out
    #print regex
    #print err
        #print out
        Netlist = []
        for line in out:
            word = line.split('  ')
            Netlist.append(word[1])
        return Netlist
    except:
        #print 'NetCheck work error!'
        return []

print TraceCheck('59.78.20.254',20)
#print "traceroute -m "+ str(MaxTTL)+ " " + ip
