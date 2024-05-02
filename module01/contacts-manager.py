# TODO - optional python project

def validate_index(array_task_index, tasks):
  if array_task_index >= 0 and array_task_index < len(tasks):
    return True
  else:
    print("Invalid task index :(")
    return False

def add_task(tasks, task_name):
  task = { "name": task_name, "completed": False }
  tasks.append(task)
  print(f"\nTask {task_name} has been added successfully!")
  return

def list_Tasks(tasks):
  print("\nTasks List:")
  for index, task in enumerate(tasks, start=1):
    task_name = task["name"]
    status = "✓" if task["completed"] else " "
    print(f"{index}. [{status}] {task_name}")
  return

def update_task(tasks, task_index, new_task_name):
  array_task_index = int(task_index) - 1

  if validate_index(array_task_index, tasks):
    tasks[array_task_index]["name"] = new_task_name
    print(f"Task {task_index} updated to {new_task_name}")
  return

def complete_task(tasks, task_index):
  array_task_index = int(task_index) - 1

  if validate_index(array_task_index, tasks):
    tasks[array_task_index]["completed"] = True
    print(f"Task {task_index} completed!")
  return

def delete_completed_tasks(tasks):
  for task in tasks:
    if task["completed"]:
      tasks.remove(task)
  print("Deleted completed tasks successfully!")
  return