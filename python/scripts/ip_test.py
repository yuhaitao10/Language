#!/usr/bin/python
import ipaddress

net = ipaddress.ip_network(u'10.0.0.16/28')
for ip in net:
  print (ip)

