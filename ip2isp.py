## ip2isp process

def ip2isp():
    i = j = 0
    last_isp = ''

    with open("ip2isp.txt","r") as fd:
        for line in fd.readlines():
            start_ip, end_ip, isp = line.strip().split('\t')
            if isp <> last_isp:
            	last_isp = isp
            	last_start = last_end = 0
            start_ip_parts = start_ip.split('.')
            end_ip_parts = end_ip.split('.')
            start = int(start_ip_parts[0]) << 24 \
                | int(start_ip_parts[1]) << 16 \
                | int(start_ip_parts[2]) << 8 \
                | int(start_ip_parts[3])
            end = int(end_ip_parts[0]) << 24 \
                | int(end_ip_parts[1]) << 16 \
                | int(end_ip_parts[2]) << 8 \
                | int(end_ip_parts[3])

            ##print "%d\t\t%x:%x:%s" % (i, start, end, isp)
            comb_arr = combin(last_start, last_end, start, end)
            ##print "len=%d" % len(comb_arr)
            if len(comb_arr) == 4:
                last_start = comb_arr[2]
                last_end = comb_arr[3]
                print "%d\t\t!!%x:%x:%s" % (i, comb_arr[0], comb_arr[1], isp)
                i = i + 1
            else:
                last_start = comb_arr[0]
                last_end = comb_arr[1]
##                print "##combined"
##            j = j + 1
##            if i > 50:
##                return 0


def combin(start1,end1,start2,end2):
    if start2 <= end1:
        if end2 <= end1:
            return start1, end1
        else:
            return start1, end2
    elif start2 == end1 + 1:
        return start1, end2
    else:
        return start1, end1, start2, end2


if __name__ == '__main__':
    ip2isp()            
