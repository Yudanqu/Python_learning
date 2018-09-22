a = 24
b =36
count = 0
for var in range(min(a,b)):
    if a%var == 0 and b%var == 0:
        count += 1
print(count)