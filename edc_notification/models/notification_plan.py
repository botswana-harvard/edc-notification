from django.db import models

from edc_base.model.models import BaseUuidModel


class NotificationPlan(BaseUuidModel):

    name = models.CharField(max_length=50, unique=True)

    friendly_name = models.CharField(max_length=50)

    subject_format = models.TextField()

    body_format = models.TextField()

    recipient_list = models.TextField()

    cc_list = models.TextField()

    objects = models.Manager()

    class Meta:
        app_label = 'edc_notification'
