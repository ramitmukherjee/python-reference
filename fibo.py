a, b = 0, 1
ans = []
while a < 10:
    ans.append(a)
    a, b = b, a+b
print(ans)