from django.db import models

from votes.models.person import Person
from votes.models.vote import Vote


class VoteResult(models.Model):
    class VoteTypeChoices(models.IntegerChoices):
        YEA = 1
        NAY = 2

    legislator = models.ForeignKey(Person, related_name='vote_result', on_delete=models.CASCADE)
    vote = models.ForeignKey(Vote, related_name='vote_result', on_delete=models.CASCADE)
    vote_type = models.IntegerField(choices=VoteTypeChoices) # type: ignore
