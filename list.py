n=int(input("how many numbers do you want to enter"))
num=[]
for i in range (1,n+1):
    num.append(int(input("Enter a Number")))
print("List : ",num)

num.sort()
print("The Smallest Number is : ",num[0])

num.sort(reverse=True)
print("The Largest Number is : ",num[0])

add=sum(num)
print("The Total is : ",add)

avg=add/n
print("The average is : ",avg)