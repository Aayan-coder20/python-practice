# tasks = ['Sleep','Getup','Brush']
# print("Original Tasks: ",tasks)

# tasks.append()
# new_task = input("Enter a new task to add: ")
# new_tasks = tasks + [new_task]
# print("Tasks after Adding: ",new_tasks)

# print("Tasks after Editing: ",tasks)
# edit_index = int(input("Enter the index of the task to edit: "))


 
# edit_task_name = input("Enter the new task: ")
# edit_tasks = new_tasks + [edit_task_name]
# print("Tasks after Editing: ",edit_tasks)
 
# tasks.pop(0)
# print("Tasks after Removing: ",tasks)

# tasks.sort()
# print("Tasks after Sorting: ",tasks)
tasks = ['Sleep', 'Getup', 'Brush']

print("Original Tasks:", tasks)

new_task = input("Enter a new task to add: ")
tasks.append(new_task)
print("Tasks after Adding:", tasks)

edit_index = int(input("Enter the index of the task to edit: "))
edit_task_name = input("Enter the new task: ")
tasks[edit_index] = edit_task_name
print("Tasks after Editing:", tasks)

remove_index = int(input("Enter the index of the task to remove: "))
tasks.pop(remove_index)
print("Tasks after Removing:", tasks)

tasks.sort()
print("Tasks after Sorting:", tasks)
