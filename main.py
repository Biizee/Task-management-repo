import django_setup

from manager.models import Task, User

#!--Creating users
#first_user = User.objects.create(name = "Сергій")
#second_user = User.objects.create(name = "Олена")
#third_user = User.objects.create(name = "Олексій")

#!--Creating tasks
#first_task = Task.objects.create(name = "Зробити оформлення сайту", description = "Треба зробити красиве та інтерактивне оформлення сайту.", status = "В процесі")
#second_task = Task.objects.create(name = "Підключити CSS", description = "Потрібно підключити CSS та оформити сайт", status = "Відкладено")
#third_task = Task.objects.create(name = "Зробити головну сторінку сайту", description = "Потрібно зробити головну сторінку сайту.", status = "Виконано")

#!--Getting data about task and user by their id
first_user = User.objects.get(id = 1)
second_user = User.objects.get(id = 2)
third_user = User.objects.get(id = 3)

first_task = Task.objects.get(id = 1)
second_task = Task.objects.get(id = 2)
third_task = Task.objects.get(id = 3)

#!--Tie a person to a task
first_task.task_owner.add(second_user)
second_task.task_owner.add(third_user)
third_task.task_owner.add(first_user)
first_task.task_owner.add(third_user)

#!--Printing tasks owners
print(first_task.task_owner.all())