#coding=utf-8
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
import time


def main():
    ip_dir = "ip/"
    regions = {}
    # total_ips = 0
    results = {}
    for filename in listdir(ip_dir):
        if filename.endswith(".txt"):
            file_places = parse_file(join(ip_dir, filename))
            regions[filename[:-4]] = file_places
            results[filename[:-4]] = []
            # break
            # for i in file_places:
                # total_ips += i[2]
    # print total_ips

    cnt = 0

    threads = []


    lock = threading.Lock()
    tasks = []

#    for i in range(THREAD_NUMBER):
#        threads.append(threading.Thread(target = run, args=(tasks, lock, results)))


    for region in regions:
        cnt = 0
        for ip_entry in regions[region]:
            #tasks.append((ip_entry, region))
            cnt += ip_entry[2]
        print region,cnt
            # print ip_entry
            # ip = parse_ip(ip_entry[0])
            # for i in range(ip_entry[2]):
                # print NetPing(ip_list2str(ip), 3), cnt
                # next_ip(ip)
                # cnt += 1

main()
