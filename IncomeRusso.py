# income tax commintment generator
import time

print ('welcome to Johnnys tax generator' ) # intro

name=input  ('What is your name? ') #asking for name

print ('Ok, nice to meet you ' +name)# repeating name back 

print (' ')

gross=input  ('What was your annual gross income this year? ' ) #asking for gross income
print ('')
if float (gross) >= 45000 : #working out  a number range if statement for comdic humor
    print ('You must of worked hard this year ' +name)
    print (' ')
elif float (gross) < 45000 :
    print ('')
    print ('Hmm, well at least you will not owe that much in taxes this year ' +name) # possibly making fun of poverty, not sure its walking a line
    print (' ')
dep =input ('How many dependents are you claming this tax year? ')#asking number of dependents 
print (' ')
if float (dep) >= 3 :
    print ('')
    print ('You must be half rabbit ' +name)# a low brow joke about procreation
    print (' ')
else:
    print(' You do know where babies come from, right? ' +name) # agian another not really that funny joke,  will try to think of something better
    print ('')

gross =float(gross) #introduction of float string mutations,  this is one of the wierdest and coolest things about python, probably a couple of other languages too I would imagine
print ('')
taxIncome =float (gross-10000) # I mean the whole class system and changing anythings class is kind of cool.

deduct = float(dep) * 3000 # start of mutating floats to  strings and  back agian

print ('Your taxable gross income is $' + str(taxIncome)) # a few youtube videos and websites later
print ('')
minDep = float(taxIncome) - float(deduct) # trying to keep these variables straight

print ('Your taxable income after deductions is $' + str(minDep)) #:start of tax bracket by taxable income
print ('')
if (minDep) >=165001:
    taxBurden = (minDep)*0.32
    print ('Pay Uncle Sam $' + str(taxBurden))
    print ('')
elif float(minDep) >= 86501:
    taxBurden = (minDep) *0.24
    print ('Pay that dirty Uncle $' +str(taxBurden))
    print ('')
elif float(minDep) >=40001:
    taxBurden = (minDep)*0.22
    print ('Pay Sammy Boy$' +str(taxBurden))
    print ('')
elif float(minDep) >= 10001:
    taxBurden = float(minDep) *0.12
    print ('Pay uncle you know who $' + str(taxBurden))
    print ('')
elif float(minDep) >=1:
    taxBurden = (minDep) * 0.1
    print ('Pay that slimy Uncle $' +str(taxBurden))
    print('')
elif float(minDep) <= 0:
    print ('Congrats you Cheated the system!! IRS agents are on the way! remain calm and stay put') #added one more tax bracket
    print ('')


import os
import sys 

while (res := input("Do you want caculate agian? [1] or exit[2]?\n").lower()) not in {"1", "2"}:# totaly grabbed  this restart /exitcode off stack overflow dont take  off points:)
    pass
if res == "1":
    time.sleep (5)
    python = sys.executable
    os.execl(python, python, * sys.argv)
else:
    end_game = True  # Stops the loop, 
    print("good bye")
    sys.exit(0)

