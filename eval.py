#coding=utf-8
from json import loads, dumps

answer = {}
for i in range(24):
    with open("result" + str(i) + ".json", "r") as f:
        a = loads(f.read())
        #print a
        for i in a:
            hint = 0
            all = 0
            sum = 0.0
            for j in a[i]:
                for k in j:
                    all += 1
                    if k > 0:
                        hint += 1
                        sum += k
            # print i,hint,all,
            # print "%.3f" % (float(hint)/float(all)),
            # print "%.4f" % (sum/float(hint))
            if i not in answer:
                answer[i] = []
            answer[i].append((hint * 1.0 / all, sum * 1.0 / hint))
with open("res.txt", "w") as f:
    f.write(dumps(answer, indent = 4))
