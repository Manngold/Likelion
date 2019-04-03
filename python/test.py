a = "Life is too short, you need python"

print(type(a))
print(len(a))
print(type(a[0: 4]))

today = "20190331Rainy"

year = today[:4]
day = today[4:8]
weather = today[8:]

print(year)
print(day)
print(weather)

num = [1, 2, 3, [4, 5, 6]]
print(num[3])
print(num)

strlist = ["c", "a", "d", "b"]
strlist.sort(reverse=True)
print(strlist)
