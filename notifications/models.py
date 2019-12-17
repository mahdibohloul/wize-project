from django.db import models
from django.conf import settings
from django.db.models import DO_NOTHING
from office.models import Office


class Messages(models.Model):
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=DO_NOTHING, default=None, db_index=True)
    request_for_work = 'request for work'
    upgarde_job = 'upgrade job post'
    OBJECT = (
        (request_for_work, 'apply'),
        (upgarde_job, 'upgrade'),
    )
    message = models.CharField(max_length=45, choices=OBJECT, default=None)
    office = models.ForeignKey(Office, on_delete=DO_NOTHING, default=None, db_index=True, null=True)

    def __str__(self):
        return "%s is object of messages from %s", self.message
