math = list()
total = 0
avg=0
n=int(input('How many people in this classs?'))
n = int(n)
for i in range(n):
    name = input('Name:')
    score = int(input('please input the score:'))
    oneperson = list()
    oneperson.append(name)
    oneperson.append(score)
    math.append(oneperson)
for item in math:
    total = total+item[1]
    average = total / n
    print('平均：',average)
high=0
person=''
for iten in math:
    if item[1]>high:
        high=item[1]
        person=item[0]
print(person,'got the highest score',high)
low=100
person=''
for iten in math:
    if item[1]<low:
        low=item[1]
        person=item[0]
print(person,'got the lowest score',low)