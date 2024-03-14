from django.db import models

from votes.models.person import Person


class Bill(models.Model):

    title = models.CharField(max_length=255)
    primary_sponsor = models.ForeignKey(Person, related_name='bill', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    @property
    def supporters_result(self):
        """
        Property to return the supporters for the bill.
        """
        from votes.models.vote import Vote
        from votes.models.vote_result import VoteResult, VoteTypeChoices

        vote = Vote.objects.filter(bill=self).first()
        result = VoteResult.objects.filter(vote=vote, vote_type=VoteTypeChoices.YEA)
        return result

    @property
    def supporters_amount(self) -> int:
        """
        Property to return the amount of supporters for the bill.
        """
        return self.supporters_result.count()

    @property
    def opposers_result(self):
        """
        Property to return the opposers for the bill.
        """
        from votes.models.vote import Vote
        from votes.models.vote_result import VoteResult, VoteTypeChoices

        vote = Vote.objects.filter(bill=self).first()
        result = VoteResult.objects.filter(vote=vote, vote_type=VoteTypeChoices.NAY)
        return result
    
    @property
    def opposers_amount(self) -> int:
        """
        Property to return the amount of opposers for the bill.
        """
        return self.opposers_result.count()