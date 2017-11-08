#!/usr/bin/env python
N = int(raw_input("Enter a number: "))
a = int(raw_input("Enter a number: "))
while a < N:
  print "%d" % a
  a *= a
  
print 23 < 67
print 25 == 25
print 34 >= 67
print 12 != 10
print 4.0 // 3
print 4.0 / 3
data = ("Sharon Olorunniwo", "Ireland", "Python")
name, country, language = data
print name
print country
print language
a = 2 + 3
print a
b = 14 % 3
print b
c = 22.0 / 12
print c
print 2 ** 3   # this is 2^3
x = True
y = False
print 1 and 4
print 4 and 4
print 12 and 3
print 22 and 67
print 3 and 1
print 1 and 0.1
print x and x
print x and y
print x or x
print x or y

