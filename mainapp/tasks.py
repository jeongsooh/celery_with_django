from celery import shared_task

# app = Celery('tasks', backend='redis://127.0.0.1', broker='redis://127.0.0.1')

# @app.task
# def test_func():
#     # Operations
#     for i in range(10):
#         print(i)
#     return "Done from tasks"

@shared_task(bind=True)
def test_func(self):
    for i in range(10):
        print(i)
    return  "Done from tasks"