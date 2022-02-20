# 1

w = 40
x = 30
y = 20
z = 10
temp = 0
while (w >= x) or (x >= y) or (y >= z):
    if w >= x:
        temp = x
        x = w
        w = temp
    if x >= y:
        temp = y
        y = x
        x = temp
    if y >= z:
        temp = z
        z = y
        y = temp
print(f'{w} {x} {y} {z}')

# 2
# Binary search method
left = 0
right = 100
ans = 0
while left < right:
    mid = left + (right - left) // 2
    c = pow(2, mid)
    if c >= 100:
        right = mid - 1
    elif c < 100:
        ans = mid
        left = mid + 1
print(f'The highest power of 2 is {ans}')

# For loop method
target = 100
ans = 1
for exponent in range(0, 10):
    ans *= 2
    if ans >= target:
        print(f'The highest power of 2 is {exponent}')
        break


# 3
def windchill(v, t):
    return 13.12 + (0.6215 * t) - 11.37 * (pow(v, 0.16)) + 0.4275 * t * (pow(v, 0.16))


for windspeed in range(0, 40, 5):
    line = f'{windspeed:>10.1f}| '
    for temperature in range(40, -45, -5):
        w = windchill(windspeed, temperature)
        line += f'{w:>6.1f}'
    print(line)

# 4
n = 27
pathlength = 0
maxval = 0
while n != 1:
    if n % 2 == 0:
        n /= 2
    else:
        n *= 3
        n += 1
    maxval = max(maxval, n)
    pathlength += 1
print(f'Maximum value {maxval}, Path length {pathlength}')
