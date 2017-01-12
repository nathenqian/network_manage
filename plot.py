#coding=utf-8
from json import loads, dumps

import numpy as np
import matplotlib.pyplot as plt
#plt.figure(1) # 创建图表1

answer = {}
with open("res.txt", "r") as f:
        a = loads(f.read())
        #print a
        tot = 0
        X = np.zeros(24)
        Y = np.zeros(24)
        Z = np.zeros(24)
        #pltlist = []
        plt.figure(0)
        for i in range(24):
            X[i] = 19 + i * 1.4
        #for i in range(4):
        #    plt.figure(i)

        for region in a:
            if region == 'qita':
                continue
            tot += 1
            #plt.figure(tot)
            for j in range(24):
                Y[j] = a[region][j][0] * 100
                Z[j] = a[region][j][1]
            plt.plot(X,Y,'-*',label=region+" time")
            plt.plot(X,Z,'-*',label=region+" hit")
            if(tot % 1 == 0):

                plt.xlim(16,70)
                plt.legend(loc='upper right')
            #plt.plot(X,Z)
                plt.show()
                #plt.savefig("./hint"+str(tot/5)+".png")
                plt.figure(tot)
        plt.legend(loc='upper right')
        plt.show()
        plt.figure(20)
        #plt.savefig("./hint4.png")
