from turtle import title
from django.db import models

# Create your models here.


class Tasks(models.Model):
    # ROLE_CHOICES = (
    #     ('mng', 'Manager'),
    #     ('emp', 'Employee'),
    #     ('cln', 'Client')
    # )

    STATUS = (
        ('pen', 'pending'),
        ('comp', 'complete')
    )

    title = models.CharField(max_length=126, blank=True)
    description = models.CharField(max_length=256, blank=True)
    task_created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # task_role = models.CharField(max_length=3,
    #                              choices=ROLE_CHOICES,
    #                              default=ROLE_CHOICES[1][0])
    status = models.CharField(max_length=4, 
                                choices=STATUS,
                                default=STATUS[0][0])
    client_user = models.ForeignKey('role.CustomUser', on_delete=models.CASCADE,limit_choices_to={'user_type': 'cln'},
        related_name="client_user",)
    employee_user = models.ForeignKey('role.CustomUser', on_delete=models.CASCADE,limit_choices_to={'user_type': 'emp'},
        related_name="employee_user",null=True,blank=True)