from django.utils.timezone import now
from django.db import models
from office.models import Office
from accounts.models import User
from notifications.models import Messages
from django.db.models import DO_NOTHING


class Task(models.Model):
    task_force = models.ForeignKey(User, on_delete=DO_NOTHING, default=None, db_index=True)
    task_title = models.CharField(max_length=65)
    task_description = models.CharField(max_length=400)
    dead_line = models.DateTimeField(auto_now_add=now(), blank=False)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return "up to %s" % self.dead_line

