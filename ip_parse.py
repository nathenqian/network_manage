def parse_file(file):
    places = []
    with open(file, "r") as f:
        contents = f.readlines()
        lines = []
        for line in contents:
            origin = line 
            while origin.replace("  ", " ") != origin:
                origin = origin.replace("  ", " ")
            lines.append(origin)

        for line in lines:
            words = line.split(" ")
            if len(words) == 4:
                places.append((words[0], words[0], 1, words[2], words[3]))
                # ip 1 place company
            else:
                print words[3]
                places.append((words[0], words[2], int(words[3]), words[4], words[5]))
                # ip - ip size place company
    return places


def parse_ip(ip_str):
    ips = ip_str.split(".")
    return [int(i) for i in ips]

def next_ip(ip_list):
    index = 3
    while ip_list[index] == 255:
        ip_list[index] = 0
        index -= 1
    ip_list[index] += 1
