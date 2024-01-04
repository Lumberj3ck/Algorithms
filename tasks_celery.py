from celery import Celery
from typing import Union, Optional


app = Celery(
    "tasks_celery",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0",
)


# x : Anotated[type, 'additional info']
# x : Optional[str]
# x : Union[int, str]
@app.task
def mull(x: str | int):
    return [1 for i in range(50_000_000)]
