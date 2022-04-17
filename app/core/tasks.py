from celery import shared_task

@shared_task(name="sum")
def add(x, y):
    return x + y

