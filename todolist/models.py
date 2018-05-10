from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
from django.db.models.signals import post_save
import datetime


@python_2_unicode_compatible
class TodoList(models.Model):
    class Meta:
        verbose_name = 'Task'
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'user_todo_list')
    name = models.CharField('Task Name', max_length=40, default='')
    description = models.CharField('Description', max_length=240, default='')
    # duration = models.
    created = models.DateTimeField('Created On', auto_now_add=True, editable=False)
    expire = models.DateTimeField('Ending On', blank=True, null=True, default=datetime.datetime.now())
    status = models.BooleanField('Task Status', default=False)
    def __str__(self):
        return self.name

# def create_everything(sender, **kwargs):
#     if kwargs['created']:
#         user_todo_list = TodoList.objects.create(user=kwargs['instance'])
#
# post_save.connect(create_everything, sender=User)
