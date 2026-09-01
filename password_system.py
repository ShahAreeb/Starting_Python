current_password="python123"
count=0
while count<4:
 password=input("Enter the password : ")
 if password==current_password:
  print("Access granted")
  break
 else:
  print("Password incorrect\nTry again")
 count=count+1