marks = [90, 25, 67, 45, 80]
number = 0
for score in marks:
    if(score >= 60):
        print("%d student is pass" % number)
        number = number + 1
    else:
        print("%d student is fail" % number)
        number = number + 1

# a = range(0, 10)

# print(a)


def vartest(a):
    a = a + 1
    return a


base = range(2, 10)
num = range(1, 10)

for i in base:
    for j in num:
        result = i * j
        print("%d * %d = %d" % (i, j,  result))
    print("***********************")
