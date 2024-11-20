import re

def show():
     try:
          with open('tasks.txt' , 'a+') as file:
               file.seek(0)
               content = file.read()
               if content == "":
                    print("You have no tasks in progress. Please add one.")
               else:
                    print(content, end="\n")
     except:
          print("You have no tasks in progress. Please add one.")

def add(task_name):
     with open('tasks.txt' , 'a') as file:
          file.write(task_name + '\n')

def delete(task_name):
     try:
          with open('tasks.txt', 'r') as file:
               lines = file.readlines()

          with open('tasks.txt', 'w') as file:
               for line in lines:
                    if not line == (task_name):
                         file.write(line)      
     except:
          print("You have no tasks in progress. Please add one.")
   

def mark(task_name):
     try:
          with open('tasks.txt' , 'a+') as file:
               file.seek(0)
               content = file.read()

          content = re.sub(task_name, f"{task_name} - Done", content)

          with open('tasks.txt' , 'w') as file:
               file.write(content)
     except:
          print("You have no tasks in progress. Please add one.")
