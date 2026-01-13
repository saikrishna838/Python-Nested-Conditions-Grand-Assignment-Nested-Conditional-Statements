n = int(input())
a = n // 1000
result1 = a
b = (n - (1000 * result1))
b = b // 500
result2 = b
c = (n - (1000 * result1) - (500 * result2))
result3 = c // 100
d = (n - (1000 * result1) - (500 * result2) - (100 * result3))
result4 = d // 50
e = (n - (1000 * result1) - (500 * result2) - (100 * result3) - (50 * result4))
result5 = e // 20
f = (n - (1000 * result1) - (500 * result2) - (100 * result3) - (50 * result4) - (20 * result5))
result6 = f // 5
g = (n - (1000 * result1) - (500 * result2) - (100 * result3) - (50 * result4) - (20 * result5) - (5 * result6))
result7 = g // 1
print("1000:" + str(result1))
print("500:" + str(result2))
print("100:" + str(result3))
print("50:" + str(result4))
print("20:" + str(result5))
print("5:" + str(result6))
print("1:" + str(result7))