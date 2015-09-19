#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ip2isp import IPAddress

__author__ = 'fengted'


with open("ip_isp.csv") as fd:
    fd.read(3)
    for line in fd.readlines():
        start, end, isp = line.strip().split(',')
        s = IPAddress(start)
        e = IPAddress(end)
        print "%d,%d,%s" % (s.ip, e.ip, isp)