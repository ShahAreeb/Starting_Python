num=74
t=0
count=1
while count<=6:
    t=int(input("Guess the number : "))
    if t>num:
        print("Number is lower than this")
    elif t<num:
        print("Number is higher than this")
    else:
        print(f"Correct Guess You took {count} attempts")
        break
    count+=1
    if count==6:
        print(f"You lost The number was {num}")
        break
