
from django.test import TestCase

from votes.models import Bill, Person


class ViewsTestCase(TestCase):

    def test_should_render_index_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_should_render_bill_list_page(self):
        response = self.client.get(f'/bills/')
        self.assertEqual(response.status_code, 200)

    def test_should_render_bill_detail_page(self):
        person = Person.objects.create(name='Person 1')
        bill = Bill.objects.create(title='Bill 1', primary_sponsor=person)

        response = self.client.get(f'/bills/{bill.id}/')
        self.assertEqual(response.status_code, 200)

    def test_should_render_legislator_list_page(self):
        response = self.client.get(f'/legislators/')
        self.assertEqual(response.status_code, 200)

    def test_should_render_legislator_detail_page(self):
        person = Person.objects.create(name='Person 1')

        response = self.client.get(f'/legislators/{person.id}/')
        self.assertEqual(response.status_code, 200)
