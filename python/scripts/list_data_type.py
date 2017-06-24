#!/usr/bin/python

#index
family = ['mon', 'dad', 'bro', 'sis', 'dog']		
family[0]		
family[-1]		
'bucky'[2]		
	

print "family list:"
print family	

#slicing is to get a section of a list
example=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]		
example[0:8:2]		
example[10:0:-2]		
example[:7]		
example[0:]		
example[4:8]		
example[-5:-1]		
		
		
[7,4,5]+[3,5,7]		
'bucky'+'roboerts'		
'bucky'*10		
		
name='rosebeef'		
'f' in name		
		
family=['mon', 'dad', 'bro', 'sis', 'dog']		
'mom' in family		
		
family[:]		
family[3]='par'		
del family[3]		
print "family list:"
print family[:]	

#list methods
len(family)		
len('bucky')		
min(family)		
max(family)		
		
example=list('asdfasdf')		
example[4:]=list('baby')		
		
face=[21,18,30]		
face.append(40)		
		
apples=['i','love','apples','apples','now']		
apples.count('apples')		
		
one=[1,2,3]		
two=[4,5,6]		
one.extend(two)		
		
say=['hey','now','brown','cow']		
say.index('brown')		
say.insert(2,'hoss')		
say.pop(1)		
say.remove('brown')		
say.reverse()		
		
new=[32,54,22,7,98,1]		
new.sort		

