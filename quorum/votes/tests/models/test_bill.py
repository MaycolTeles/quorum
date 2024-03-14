
from django.test import TestCase

from votes.models import Bill, Person, Vote, VoteResult, VoteTypeChoices


class BillTestCase(TestCase):

    def test_should_return_correct_supporters_amount(self):
        person = Person.objects.create(name='Person 1')
        bill = Bill.objects.create(title='Bill 1', primary_sponsor=person)

        self.assertEqual(bill.supporters_amount, 0)
        self.assertEqual(bill.opposers_amount, 0)

        vote = Vote.objects.create(bill=bill)
        VoteResult.objects.create(vote=vote, legislator=person, vote_type=VoteTypeChoices.YEA)

        self.assertEqual(bill.supporters_amount, 1)
        self.assertEqual(bill.opposers_amount, 0)

    def test_should_return_correct_opposers_amount(self):
        person = Person.objects.create(name='Person 1')
        bill = Bill.objects.create(title='Bill 1', primary_sponsor=person)

        self.assertEqual(bill.supporters_amount, 0)
        self.assertEqual(bill.opposers_amount, 0)

        vote = Vote.objects.create(bill=bill)
        VoteResult.objects.create(vote=vote, legislator=person, vote_type=VoteTypeChoices.NAY)

        self.assertEqual(bill.supporters_amount, 0)
        self.assertEqual(bill.opposers_amount, 1)