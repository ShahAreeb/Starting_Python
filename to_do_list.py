task=[]
while True:
 print("Welcome to ToDo List")
 op=int(input("Choose an option\n 1.Add Task\n 2.View Task\n 3.Delete task\n 4.Exit"))
 if op==1:
  task.append(input("Enter The Task: "))
 elif op==2:
  print(task)
 elif op==3:
  d=int(input("Which Task number to delete"))
  task.pop(d-1)
 elif op==4:
  break
 else:
  print("Invalid Option")
