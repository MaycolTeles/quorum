from django.db import models

from votes.models.bill import Bill


class Vote(models.Model):

    bill = models.ForeignKey(Bill, related_name='vote', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.bill.title} - {self.id}'
