from django.db import models

from edc_base.model.models import BaseUuidModel
from edc_sync.models import SyncModelMixin


class Notification(SyncModelMixin, BaseUuidModel):

    notification_plan_name = models.CharField(max_length=200)

    notification_datetime = models.DateTimeField()

    subject = models.CharField(max_length=200)

    recipient_list = models.TextField(null=True)

    cc_list = models.TextField(null=True)

    body = models.TextField(null=True)

    status = models.CharField(
        max_length=15,
        default='new',
        choices=(
            ('new', 'New'),
            ('sent', 'Sent'),
            ('cancelled', 'Cancelled')))

    sent = models.BooleanField(default=False)

    sent_datetime = models.DateTimeField(null=True)

    class Meta:
        app_label = 'edc_notification'
        ordering = ('notification_datetime', )
