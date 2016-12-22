from os import listdir
from os.path import join
from ip_parse import parse_file, parse_ip, next_ip, ip_list2str
from test import NetPing

if __name__ == "__main__":
    ip_dir = "ip/"
    regions = {}
    total_ips = 0

    for filename in listdir(ip_dir):
        if filename.endswith(".txt"):
            file_places = parse_file(join(ip_dir, filename))
            regions[filename[:-4]] = file_places
            for i in file_places:
                total_ips += i[2]
    print total_ips
    cnt = 0
    for region in regions:
        for ip_entry in regions[region]:
            print ip_entry
            ip = parse_ip(ip_entry[0])
            for i in range(ip_entry[2]):
                print NetPing(ip_list2str(ip), 3), cnt
                next_ip(ip)
                cnt += 1

