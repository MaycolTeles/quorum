from django.db import models


class Person(models.Model):

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    @property
    def supported_bills(self):
        """
        Property to return the bills the person has supported.
        """
        from votes.models.vote_result import VoteResult, VoteTypeChoices

        result = VoteResult.objects.filter(legislator=self, vote_type=VoteTypeChoices.YEA)
        return result

    @property
    def supported_bills_amount(self) -> int:
        """
        Property to return the amount of bills the person has supported.
        """
        return self.supported_bills.count()

    @property
    def opposed_bills(self):
        """
        Property to return the amount of bills the person has opposed.
        """
        from votes.models.vote_result import VoteResult, VoteTypeChoices

        result = VoteResult.objects.filter(legislator=self, vote_type=VoteTypeChoices.NAY)
        return result

    @property
    def opposed_bills_amount(self) -> int:
        """
        Property to return the amount of bills the person has opposed.
        """
        return self.opposed_bills.count()
