from fastapi import FastAPI, HTTPException
from app.src.models import Task
import app.src.database as db

app = FastAPI(title="Simple Task Manager API")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/tasks")
def create_task(task: Task):
    created = db.add_task(task)
    return created

@app.get("/tasks")
def list_tasks():
    return db.get_all_tasks()

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    task = db.get_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    task = db.get_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete_task(task_id)
    return {"message": "Task deleted"}