
#2 https://pythontutor.com/visualize.html#code='''%0AThis%20method%20should%20print%20the%20sum%20of%20squares%20from%201%20to%20n%0AFor%20example%20sumOfSquares%284%29%20%3D%2030%0A1%5E2%20%2B%202%5E2%20%2B%203%5E2%20%2B%204%5E2%20%3D%2030%0A'''%0Adef%20sumOfSquares%28n%29%3A%0A%20%20%20%20if%20n%20%3D%3D%201%3A%0A%20%20%20%20%20%20%20%20return%201%0A%20%20%20%20%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20return%20%28n*n%29%20%2B%20sumOfSquares%28n%20-%201%29%0A%0A%0Aprint%20sumOfSquares%284%29&cumulative=false&curInstr=19&heapPrimitives=false&mode=display&origin=opt-frontend.js&py=2&rawInputLstJSON=%5B%5D&textReferences=false

# 3
list = [1,2,3,4,5,6]

def Q3(l):
    if len(l) <= 0:
        return 0
    return l[0] + Q3(l[1:])

print(Q3(list))

#4
s = 15866321
def Q4(s):
    s = str(s)
    if len(s) <= 3:
        return s
    else:
        return Q4(s[:-3]) + "," + s[-3:]
print(Q4(s))

#5
m = 'hello world'
def Q5(s):
    if len(s) == 0:
        return s
    else:
        return Q5(s[1:]) + s[0]

print(Q5(m))

#6

list = []
def Q6(some_list, item):
    if len(some_list) == 0:
        return -1
    elif some_list[-1] == item:
        return len(some_list)-1
    else:
        return Q6(some_list[:-1], item)
print(Q6([3, 6, 7, 8, 9], 2))

#Q7
# nothing like this would be on the test
def flattenList(m):
    if type(m[0]) == list and len(m) > 1:
        return flattenList(m[0]) + " " + flattenList(m[1: ])
    elif type(m[0]) == list and len(m) == 1:
        return flattenList(m[0])
    elif len(m) == 1:
        return str(m[0])
    else:
        return str(m[0]) + " " + flattenList(m[1:])

print(flattenList([1, 2, 3, [[0, 7], 9, 8], 5, 6]))
print(flattenList([1, 2, 3, [[0, 7], 9, [8, 8], 5, 6]]))
print(flattenList(['a', 'b', ['c', 'd']]))