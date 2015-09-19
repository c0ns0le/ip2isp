## ip2isp process

def clear(x):
    if x == '0\xe3\x80\x80':
        return '0'
    else:
        return x

class IPAddress(object):

    def __init__(self, addr="0.0.0.0"):
        if isinstance(addr, str):
            if addr == '0\xe3\x80\x80':
                addr = '0'
            ips = [int(clear(x)) for x in addr.split('.')]
            self.ip = ips[0] << 24 \
                | ips[1] << 16 \
                | ips[2] << 8 \
                | ips[3]
        if isinstance(addr, int):
            self.ip = addr

    def __str__(self):
        return "%d.%d.%d.%d" % (self.ip >> 24, (self.ip & 0xff0000) >> 16, (self.ip & 0xff00) >> 8, self.ip & 0xff)

    def __cmp__(self, other):
        return self.ip - other.ip

    def nextip(self):
        return IPAddress(self.ip + 1)


class IPRange(object):

    def __init__(self, start_ip, end_ip, isp):
        self.isp = isp
        if isinstance(start_ip, IPAddress):
            self.start = start_ip
        else:
            self.start = IPAddress(start_ip)

        if isinstance(end_ip, IPAddress):
            self.end = end_ip
        else:
            self.end = IPAddress(end_ip)

    def __str__(self):
        return str(self.start) + "~" + str(self.end) + "@" + self.isp

    def combin(self, other):
        if self.isp != other.isp:
            return None

        if other.start <= self.end:
            if other.end <= self.end:
                return IPRange(self.start, self.end, self.isp)
            else:
                return IPRange(self.start, other.end, self.isp)
        elif other.start == self.end.nextip():
            return IPRange(self.start, other.end, self.isp)
        else:
            return None


def main():
    i = j = 0

    with open("ip2.csv", "r") as fd:
        for line in fd.readlines():
            i = i + 1
            start_ip, end_ip, isp = line.strip().split(',')
            isp = isp.decode("gb2312")

            this_range = IPRange(int(start_ip), int(end_ip), isp)
            if i == 1:
                last_range = this_range
                continue

            r = last_range.combin(this_range)
            if r == None:
                j = j + 1
                print "%d:%d:%s" % (j, i, last_range)
                last_range = this_range
            else:
                last_range = r


if __name__ == '__main__':
    main()
