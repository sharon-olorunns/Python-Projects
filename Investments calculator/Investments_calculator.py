#!/usr/bin/env python
amount = float(raw_input("Enter an amount: "))
inrate = float(raw_input("Enter Interest rate: "))
timeFrame = int(raw_input("Enter time frame: "))
value = 0
year = 1  #min number of years
while year <= timeFrame:
  value = amount + (inrate * amount)
  print "Year %d Rs. %.2f" % (year, value)
  amount = value
  year = year + 1
