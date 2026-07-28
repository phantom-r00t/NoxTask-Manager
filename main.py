import json
from pathlib import Path


file_path = Path("tasks.json")

print("================================================")
print("   NoxTask Manager      ")
print("================================================")

task = []

def load_tasks():
    with open(file_path,"r") as file:
        return json.load(file)

def add():
    global task

    task = load_tasks()

    print("================================================")

    new_task = input("- Add Task : ")
    task.append(new_task)
    tasks = json.dumps(task)
    

    with open(file_path,"w") as file:
        json.dump(task, file, indent=4)

    print("================================================")

    print("Task added: ")
    for index, item in  enumerate(task, start=1) :
        print(index,"-", item)

    print("================================================\n")
def remove():

    task = load_tasks()

    print("================================================")

    while True :
        del_task = input("- Remove Task : ")
        if del_task not in task :
            print("\nThe task does not exist\n")

        elif del_task in task :
            task.remove(del_task)
            tasks = json.dumps(task)

            with open(file_path,"w") as file:
                json.dump(task, file, indent=4)
            
            print("================================================")

            print("Task removed : ")
            for index, item in  enumerate(task, start=1) :
                print(index,"-", item) 

            print("================================================\n")

            break
def show():

        task = load_tasks()

        print("================================================")

        print("Your Task:")

        for index, item in  enumerate(task, start=1) :
            print(index,"-", item)
        
        print("================================================\n")
def search():

    task = load_tasks()

    print("================================================")

    find_task = input("Find Task : ")

    print("================================================")

    if find_task in task :
        print("The Task exists : ",find_task)
        print("================================================\n")
    else:
        print("The task does not exist")
        print("================================================\n")
def count():

    task = load_tasks()

    print("================================================")
    print("Total Tasks : ",len(task))
    print("================================================\n")
def clear():

    task = load_tasks()

    task.clear()
    tasks = json.dumps(task)

    with open(file_path,"w") as file: 
        json.dump(task, file, indent=4)

    print("================================================")
    print("Task is Cleared : ")
    for index, item in  enumerate(task, start=1) :
        print(index,"-", item) 
    print("================================================\n")

def run():
    print("\n1) Add Task")
    print("2) Remove Task")
    print("3) Show Tasks")
    print("4) Search Task")
    print("5) Count Tasks")
    print("6) Clear Tasks")
    print("7) Exit")
    print("\n================================================")

    while True:
        try:
            choose = int(input("To choose : "))

            if choose == 1:
                add()
                break
            elif choose == 2:
                remove()
                break
            elif choose == 3:
                show()
                break
            elif choose == 4:
                search()
                break 
            elif choose == 5:
                count()
                break
            elif choose == 6:
                clear()
                break
            elif choose == 7:
                break
            else:
                print("Please select an available option")
                
        except ValueError:
            print("Please Enter The Number Choose")
        except KeyboardInterrupt:
            break
            

run()