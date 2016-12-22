from os import listdir
from os.path import join
from ip_parse import parse_file, parse_ip, next_ip, ip_list2str
from test import NetPing
import threading
import random
import randomSize
from json import dumps
THREAD_NUMBER = 50
CNT = 0

def run(tasks, lock, results):
    global CNT
    while True:
        lock.acquire()
        task_cnt = len(tasks)
        if task_cnt > 0:
            task = tasks.pop()
        lock.release()
        if task_cnt == 0:
            return
        if task_cnt % 100 == 0:
            print "tasks size %d" % (task_cnt)
        ip_entry = task[0]
        ip = parse_ip(ip_entry[0])
        chooseList = []

        for i in range(ip_entry[2]):
            #NetPing(ip_list2str(ip), 3)
            #CNT += 1
            #next_ip(ip)
            #if CNT % 100 == 0:
            #    print CNT
            chooseList.append(ip_list2str(ip))
            next_ip(ip)

        random.shuffle(chooseList)
        chooseLen = randomSize.getSize(ip_entry[2])
        for i in range(chooseLen):
            result = NetPing(chooseList[i], 5)
            CNT += 1
            if CNT % 1000 == 0:
                print "have run %d task" % (CNT)
            lock.acquire()
            results[task[1]].append(result)
            lock.release()

def main(output_file_name):
    ip_dir = "ip/"
    regions = {}
    # total_ips = 0
    results = {}
    for filename in listdir(ip_dir):
        if filename.endswith(".txt"):
            file_places = parse_file(join(ip_dir, filename))
            regions[filename[:-4]] = file_places
            results[filename[:-4]] = []
            break
            # for i in file_places:
                # total_ips += i[2]
    # print total_ips

    cnt = 0

    threads = []


    lock = threading.Lock()
    tasks = []
    
    for i in range(THREAD_NUMBER):
        threads.append(threading.Thread(target = run, args=(tasks, lock, results)))

    for region in regions:
        for ip_entry in regions[region]:
            tasks.append((ip_entry, region))
            # print ip_entry
            # ip = parse_ip(ip_entry[0])
            # for i in range(ip_entry[2]):
                # print NetPing(ip_list2str(ip), 3), cnt
                # next_ip(ip)
                # cnt += 1
    for i in threads:
        i.setDaemon(True)
        i.start()

    for i in threads:
        i.join()

    with open(output_file_name, "w") as f:
        f.write(dumps(results, indent = 4))



if __name__ == "__main__":
    main("result.json")