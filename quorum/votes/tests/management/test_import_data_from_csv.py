
from django.test import TestCase

from votes.models import Bill, Person, Vote, VoteResult
from votes.management.commands.import_data_from_csv import import_data_from_csv


class ImportDataFromCSVTestCase(TestCase):

    def test_should_import_all_data_from_csv(self):

        self.assertEqual(Bill.objects.count(), 0)
        self.assertEqual(Person.objects.count(), 0)
        self.assertEqual(Vote.objects.count(), 0)
        self.assertEqual(VoteResult.objects.count(), 0)

        import_data_from_csv()

        self.assertEqual(Bill.objects.count(), 2)
        self.assertEqual(Person.objects.count(), 20)
        self.assertEqual(Vote.objects.count(), 2)
        self.assertEqual(VoteResult.objects.count(), 38)