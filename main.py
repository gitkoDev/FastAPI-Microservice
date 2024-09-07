from fastapi import FastAPI, HTTPException
from typing import List

from uuid import UUID, uuid4
from models.task_models import Task


app = FastAPI()

tasks = []


@app.post("/tasks", response_model=Task)
def add_task(task: Task):
    task.id = uuid4()
    tasks.append(task)
    return task


@app.get("/tasks", response_model=List[Task])
async def get_tasks():
    return tasks


@app.get("/tasks/{task_id}", response_model=Task)
def get_task_by_id(task_id: UUID):
    for task in tasks:
        if task.id == task_id:
            return task

    raise HTTPException(status_code=404, detail="Task not found")


@app.put("/tasks/{task_id}")
def update_task(task_id: UUID, task_update: Task):
    for i, task in enumerate(tasks):
        if task.id == task_id:
            updated_task = task.copy(update=task_update.dict(exclude_unset=True))
            tasks[i] = updated_task
            return updated_task

    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks/{task_id}")
def delete_task(task_id: UUID):
    for i, task in enumerate(tasks):
        if task.id == task_id:
            tasks.pop(i)
            return {"ok": "task deleted successfully"}
        raise HTTPException(status_code=404, detail="Task not found")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
