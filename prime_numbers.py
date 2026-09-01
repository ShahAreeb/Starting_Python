#first n prime numbers ( / check whether a no is prime or not / if yes the print / if no then continue)
n = int(input("How many prime numbers do you want: "))

count = 0
num = 2

while count < n:
    is_prime = True

    for i in range(2, num):

        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num)
        count = count + 1

    num = num + 1