pennies = 127
print(pennies/100)
print(pennies//100) #// floor division, takes the largest integer

print(f'{pennies:^13.2f} hi')

for i in range(1, 10+1, 3):
    print(i)

for i in range(10, -1, -1):
    print(f'{i:>10.2f}')

temp = "hello"
print(temp[-2:])

temp2 = temp.capitalize() #capitalizes the first letter
print(temp2)

temp3 = temp.strip("")
print(temp3)
temp+=" "
print(temp[:-1])

list = [1, 2,3,4,5,6]
list.reverse()
print(list)

colours = {'red': '123', 'blue': '32131'}
colours['red'] = '1222'
print(colours['red'])