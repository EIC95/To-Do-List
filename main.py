import os
import platform
import functions

while True:
     if platform.system() == 'Windows':
          os.system('cls')
     else:
          os.system('clear')
          
     print("========== To-Do List ==========")
     print("\n1. Show all tasks")
     print("2. Add a task")
     print("3. Delete a task")
     print("4. Mark a task as done")
     print("5. Exit the app")

     while True:
          try:
               choice = int(input("\nEnter your choice: "))
               if choice in range(1, 6):
                    break
               print("Wrong entry. Please enter a valid number (1 to 5)")
          except ValueError:
               print("Wrong entry. Please enter a valid number (1 to 5)")

     if platform.system() == 'Windows':
          os.system('cls')
     else:
          os.system('clear')

     match choice:
          case 1:
               print("\n========== Task List ==========\n")

               functions.show()

               choice = input("\nEnter 'r' to return to the main menu: ")
               while choice.lower() != 'r':
                    print("Wrong entry. Please enter a valid letter(r-R).")
                    choice = input("\nEnter 'r' to return to the main menu: ")
               continue

          case 2:
               print("\n========== Add a task ==========\n")

               task_name = input("\nEnter the name of the task: ")

               functions.add(task_name)

               print("\nTask added successfully.")

               choice = input("\nEnter 'r' to return to the main menu: ")
               while choice != 'r'and choice != 'R' :
                    print("Wrong entry. Please enter a valid letter(r-R).")
                    choice = input("\nEnter 'r' to return to the main menu: ")
               continue

          case 3:
               print("\n========== Delete a task ==========\n")

               print("\n===== Task List =====\n")

               functions.show()

               with open('tasks.txt' , 'r') as file:
                    content = file.read()

               if content != "":
                    while True:
                         task_name = input("\nEnter the name of the task you want to delete: ")

                         with open('tasks.txt', 'r') as file:
                              lines = file.readlines()

                              if any(task_name in line for line in lines):
                                   break
                              else:
                                   print(f"\nThe task does not exist. Please try again.")

                    functions.delete(task_name)
                    print("Task deleted successfully.")

               choice = input("\nEnter 'r' to return to the main menu: ")
               while choice != 'r'and choice != 'R' :
                    print("Wrong entry. Please enter a valid letter(r-R).")
                    choice = input("\nEnter 'r' to return to the main menu: ")
               continue

          case 4:
               print("\n========== Mark a task as done ==========\n")

               print("\n===== Task List =====\n")

               functions.show()

               with open('tasks.txt' , 'r') as file:
                    content = file.read()

               if content != "":
                    while True:
                         task_name = input("\nEnter the name of the task you want to mark: ")

                         with open('tasks.txt', 'r') as file:
                              lines = file.readlines()

                              if any(task_name in line for line in lines):
                                   break
                              else:
                                   print(f"\nThe task does not exist. Please try again.")

                    functions.mark(task_name)
                    print("Task marked successfully.")

               choice = input("\nEnter 'r' to return to the main menu: ")
               while choice != 'r'and choice != 'R' :
                    print("Wrong entry. Please enter a valid letter(r-R).")
                    choice = input("\nEnter 'r' to return to the main menu: ")
               continue

          case 5:
              exit()            