from django.db import models

from votes.models.person import Person


class Bill(models.Model):

    title = models.CharField(max_length=255)
    primary_sponsor = models.ForeignKey(Person, related_name='bill', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
