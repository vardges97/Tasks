task_list = []


# def add_task():
#     task_id = input('please enter a task id: ')
#     description = input('enter the name of the task: ')
#     if not description:
#         print('task description cant be empty')
#         return
#     priority = input("enter a priority for the task(low,medium,high):").lower
#     if priority not in ('low','medium','high'):
#         print('invalid task must have priority')
#         return
#     statuss = "incomplet"
#     task = {
#         'id':task_id,
#         'description': description,
#         'compeletion': statuss,
#         'priority': priority
#     }
#     task_list.append(task)
#     print('task added successfully')

def add_task():
    task_id = input('please enter a task id: ')
    description = input("Enter task description: ")
    if not description:
        print("Task description cannot be empty.")
        return
    priority = input("Enter task priority (low, medium, high): ").lower()
    if priority not in ('low', 'medium', 'high'):
        print("Invalid priority. Task not added.")
        return
    status = "incompelete"
    task = {
        'id': task_id,
        'description': description,
        'compeletion': status,
        'priority': priority
    }
    task_list.append(task)
    print("Task added successfully.")

def remove_task():
    task_id = int(input('please enter the task id which you want removed: '))
    for task in task_list:
        task_id == task['id']
        task_list.remove(task)
        print('task removed')
        return
    else:
        print('task not found in task list')

def list_tasks():
    if not task_list:
        print('no such task found')
        return
    for task in task_list:
        print(f"ID: {task['id']},Description: {task['description']},Status: {task['compeletion']},Priority: {task['priority']}")

def list_compeleted():
    if not task_list:
        print('to tasks found')
    for task in task_list:
        if task['compeletion'] == 'compelete':
            print(f"ID: {task['id']},Description: {task['description']},"
                f"Status: {task["compeletion"]},{task['priority']}")
    print('task not in task list')


def task_status():
    task_id = input("please enter id of the task to change status: ")
    status = input("enter status of the task: ")
    for task in task_list:
        if task['id'] == task_id:
            task['compeletion'] = status
            print('task status updated')
            return

def task_priority():
    task_id = input('enter the if of the task to which you want to set priority: ')
    priority = input("please enter the priority of the task(low,medium,high)").lower()
    for task in task_list:
        if task['id'] == task_id:
            if priority in('low','medium','high'):
                task['priority'] = priority
                print("task priority updated")
            else:
                print("wrong priority please enter either low, medium or high")
            return
        print('task not foun in task list check id')

while True:
    print("Welcome to the task list menue.\nto add a task press 1\nto remove a task press 2\n"
          "to list all the tasks press 3\nto change task status press 4\nto list compeleted tasks press 5\n"
          "to change task priority press 6\nto exit press q")

    choice = input('please choose the desired operation: ')

    if choice == '1':
        add_task()
    if choice == '2':
        remove_task()
    if choice == '3':
        list_tasks()
    if choice == '4':
        task_status()
    if choice == '5':
        list_compeleted()
    if choice == '6':
        task_priority()
    if choice =='q':
        print('quitting')
        break

