#!/usr/bin/python

#working on dictionary
print "\nWorking on dictionary"
hosts = {}

hosts['h1'] = '1.2.3.4'
hosts['h2'] = '2.3.4.5'
hosts['h3'] = '3.4.5.6'

for server,ip in hosts.items():
  print server, ip

for server,ip in hosts.items():
	print ('serer: {} ip: {}'.format(server, ip))

hosts2 = {'h1':'1.2.3.4','h2':'2,3,4,5', 'h3':'3.4.5.6'}
for server,ip in hosts2.items():
  print "server: %s" % ip

mylist = []  

mytuple = ()

mydictionary = {}


book={'Dad':'Bob','Mom':'Lisa','Bro':'Joe'}		
book['Dad']		
p=book.clear()		
print "Dictionary clear() function: %s" % p
		
ages={'Dad':'42','Mom':'87'}		
tuna=ages.copy()		
p = 'Mom' in tuna		
print "Dictionary in function: %s" % p

#working on string
print "\nWorking on string:"
seperator='hoss'		
sequence=['hey','there', 'bessie','hoss']		
glue='hoss'		
p=glue.join(sequence)		
print "string join() function: %s" % p
		
randstr="I wich I Had No Sausage"		
randstr		
p = randstr.lower()		
print "string lower() function: %s" % p
		
truth="I love old women"		
p = truth.replace('women', 'men')		
print "String replace() function: %s" % p

example="Hey now bessie nice chops"		
p = example.find('bessie')		
print "String find() function: %s" % p

ratio = '68%'
amt = int(ratio.rstrip('%'))
print "String rstrip() function: %s" % amt
