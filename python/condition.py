money = 2000
card = 1

if(money >= 3000 or card):
    print("taxi")
else:
    print("walk")

pocket = ['pocket', 'cellphone', 'card']

if("money" in pocket):
    print("taxi")
elif(not "money" in pocket and "card" in pocket):
    print("taxi")
else:
    print("walk")

prompt = """
    1. Add
    2. Del
    3. List
    4. Quit
    
    Enter number: """
number = 0
while number != 4:
    print(prompt)
    number = int(input())

coffee = 10
while coffee:
    money = int(input("insert money : "))
    if(money > 300):
        rest = money - 300
        coffee = coffee - 1
        print("change %d and give coffee" % rest)
        print("rest coffee amount is %d" % coffee)
    elif(money == 300):
        coffee = coffee - 1
        print("rest coffee amount is %d" % coffee)
    else:
        print("back money")
        print(coffee)
