#!/usr/bin/env python
N = int(raw_input("Enter your list number: "))
sum = 0
count = 0
while count < N:
  number = float(raw_input(""))
  sum = sum + number
  count = count + 1
average = float(sum)/N
print "N = %d, Sum = %f" % (N, sum)
print "Average = %f" % average
