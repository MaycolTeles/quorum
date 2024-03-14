
from django.test import TestCase

from votes.models import Bill, Person, Vote, VoteResult, VoteTypeChoices


class PersonTestCase(TestCase):

    def test_should_return_correct_supported_bills_amount(self):
        person = Person.objects.create(name='Person 1')
        bill = Bill.objects.create(title='Bill 1', primary_sponsor=person)

        self.assertEqual(person.supported_bills_amount, 0)
        self.assertEqual(person.opposed_bills_amount, 0)

        vote = Vote.objects.create(bill=bill)
        VoteResult.objects.create(vote=vote, legislator=person, vote_type=VoteTypeChoices.YEA)

        self.assertEqual(person.supported_bills_amount, 1)
        self.assertEqual(person.opposed_bills_amount, 0)

    def test_should_return_correct_opposed_bills_amount(self):
        person = Person.objects.create(name='Person 1')
        bill = Bill.objects.create(title='Bill 1', primary_sponsor=person)

        self.assertEqual(person.supported_bills_amount, 0)
        self.assertEqual(person.opposed_bills_amount, 0)

        vote = Vote.objects.create(bill=bill)
        VoteResult.objects.create(vote=vote, legislator=person, vote_type=VoteTypeChoices.NAY)

        self.assertEqual(person.supported_bills_amount, 0)
        self.assertEqual(person.opposed_bills_amount, 1)