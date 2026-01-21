import django_setup

from manager.models import Task, User
from django.core.exceptions import ObjectDoesNotExist

def create_task_owner():
    name = input("\nEnter user(future task owner) name: ")
    user = User.objects.create(
        name = name
    )
    print(f"\nUser, {user.name}, was succesfully created!")

def create_task():
    task_name = input("\nEnter task name: ")
    task_desc = input("\nEnter task description: ")
    task_status = input("\nEnter task status (в процесі, виконано, відкладено): ")
    try:
        task_owner = int(input("\nEnter task owner id: "))
        task_owner = User.objects.get(id = task_owner)
        task = Task.objects.create(
            name = task_name,
            description = task_desc,
            task_status = task_status,
            task_owner = task_owner

        )
        print(f"\nTask was succesfully created!")
    except ObjectDoesNotExist:
        print(f"Task owner doesn't exists. Try again!")
    except Exception as e:
        print(f"Error: {e}")

def list_tasks():
    tasks = Task.objects.all()
    if tasks:
        for task in tasks:
            print(f"\nID - {task.id}. \nName - {task.name}. \nDescription - {task.description}. \nUser (task owner) - {task.task_owner.all()}")
    else:
        print("No users found!")

def update_task_status():
    try:
        task_id = int(input("\nEnter task id: "))
        new_status = input("\nEnter new task status (в процесі, виконано, відкладено): ")
        task = Task.objects.get(id = task_id)
        task.status = new_status
        task.save()
    except ObjectDoesNotExist:
        print(f"Task doesn't exists. Try again!")
    except Exception as e:
        print(f"Error: {e}")

def delete_task():
    try:
        task_id = int(input("\nEnter task id: "))
        task = Task.objects.get(id = task_id)
        task.delete()
    except ObjectDoesNotExist:
        print(f"Task doesn't exists. Try again!")
    except Exception as e:
        print(f"Error: {e}")

def edit_task_owner():
    try:
        task_id = int(input("\nEnter task id: "))
        task_owner = int(input("\nEnter new task owner id: "))
        task = Task.objects.get(id = task_id)
        task_owner = User.objects.get(id = task_owner)
        task.task_owner = task_owner
    except ObjectDoesNotExist:
        print(f"Task or user(task owner) doesn't exists. Try again!")
    except Exception as e:
        print(f"Error: {e}")

while True:
    print("""
Options:
1. Create task owner
2. Create task
3. List all tasks
4. Update task's status
5. Delete task
6. Edit task onwer
7. Exit""")
    
    try:
        choice = int(input("\nEnter your choice: "))
    except Exception as e:
        print(f"Error: {e}")
    
    if choice == 7:
        break
    
    elif choice == 1:
        create_task_owner()

    elif choice == 2:
        create_task()
    
    elif choice == 3:
        list_tasks()
    
    elif choice == 4:
        update_task_status()
    
    elif choice == 5:
        delete_task()

    elif choice == 6:
        edit_task_owner()

    else:
        print("Invalid choice, try again!")