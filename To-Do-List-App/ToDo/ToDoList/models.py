from django.db import models


# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Task(models.Model):
    text = models.CharField(max_length=200)
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    # task_num = models.IntegerField()
    #
    # def __str__(self):
    #     return str(self.task_num)
