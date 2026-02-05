tasks = []
task_id_counter = 1

def add_task(task):
    global task_id_counter
    task.id = task_id_counter
    tasks.append(task)
    task_id_counter += 1
    return task

def get_all_task():
    return tasks

def get_task(task_id: int):
    return next((t for t in tasks if t.id == task_id), None)

def delete_task(task_id: int):
    global tasks
    tasks = [t for t in tasks if t.id != tasks.id]
