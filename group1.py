'''
question 1:
difference between Python 2 and Python 3:
1)Division operator: integer division
2)print function: use () in python 3
3)unicode:in Python 2, implicit str type is ASCII. But in Python 3.x implicit str type is Unicode
4)xrange: xrange() of Python 2.x doesn’t exist in Python 3.x.
5)error handling: as is needed in Python 3

'''

#question 2:
Firstname='Aihua'
Lastname='Zhu'

print(Firstname,Lastname)
print(Firstname[::-1],Lastname[::-1])
print(len(Firstname),len(Lastname))
aaa=int(input('enter any integer'))
bbb=int(input('enter any integer'))
print('sum of aaa and bbb is',aaa+bbb)

#question 3:
str = input ("enter anything sentence")
digit = 0
letters = 0
for i in str:
 if i.isalpha():
  letters += 1
 elif i.isdigit():
  digit += 1
print (letters, digit)

