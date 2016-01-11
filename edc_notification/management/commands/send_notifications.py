import json

from datetime import datetime

from smtplib import SMTPException, SMTPRecipientsRefused, SMTPSenderRefused

from django.core.management.base import BaseCommand
from django.core.mail import send_mail


from edc_notification.models import Notification


class Command(BaseCommand):

    args = '<message_tag>'
    help = 'Export transactions for a given app_label.model_name.'
    option_list = BaseCommand.option_list

    def handle(self, *args, **options):
        for notification in Notification.objects.filter(status='new'):
            try:
                print(
                    'sending to {0}'.format(
                        ', '.join(json.loads(notification.recipient_list) + json.loads(notification.cc_list))))
                send_mail(notification.subject,
                          notification.body,
                          'edcdev@bhp.org.bw',
                          json.loads(notification.recipient_list) + json.loads(notification.cc_list),
                          fail_silently=False)
            except SMTPException as e:
                print('Error: Unable to send notification. {2}. See \'{0}\' pk={1}'.format(
                    notification.subject, notification.pk, e))
            except (SMTPRecipientsRefused, SMTPSenderRefused) as e:
                print('Error: Unable to send notification. {2}. See \'{0}\' pk={1}'.format(
                    notification.subject, notification.pk, e))
            else:
                notification.status = 'sent'
                notification.sent = True
                notification.sent_datetime = datetime.today()
                notification.save()
