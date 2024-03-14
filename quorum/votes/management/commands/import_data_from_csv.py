import csv

import djclick as click

from votes.models import Bill, Person, Vote, VoteResult


@click.command()
def import_data_from_csv():
    _import_data_from_csv()


def _import_data_from_csv():
    _create_persons()
    _create_bills()
    _create_votes()
    _create_vote_results()


def _create_persons():
    legislators = []

    with open('legislators.csv', 'r') as file:
        reader = csv.DictReader(file)
        list_of_objects = list(reader)

        for legislator_data in list_of_objects:
            idx = legislator_data['id']
            name = legislator_data['name']

            person = Person(id=idx, name=name)
            legislators.append(person)

    Person.objects.bulk_create(legislators, ignore_conflicts=True)


def _create_bills():
    bills = []

    with open('bills.csv', 'r') as file:
        reader = csv.DictReader(file)
        list_of_objects = list(reader)

        for bill_data in list_of_objects:
            idx = bill_data['id']
            title = bill_data['title']
            sponsor_id = bill_data['sponsor_id']

            bill = Bill(id=idx, title=title, primary_sponsor_id=sponsor_id)
            bills.append(bill)

    Bill.objects.bulk_create(bills, ignore_conflicts=True)


def _create_votes():
    votes = []

    with open('votes.csv', 'r') as file:
        reader = csv.DictReader(file)
        list_of_objects = list(reader)

        for vote_data in list_of_objects:
            idx = vote_data['id']
            bill_id = vote_data['bill_id']

            vote = Vote(id=idx, bill_id=bill_id)
            votes.append(vote)

    Vote.objects.bulk_create(votes, ignore_conflicts=True)

    
def _create_vote_results():
    results = []

    with open('vote_results.csv', 'r') as file:
        reader = csv.DictReader(file)
        list_of_objects = list(reader)

        for result_data in list_of_objects:
            idx = result_data['id']
            legistalator_id = result_data['legislator_id']
            vote_id = result_data['vote_id']
            vote_type = result_data['vote_type']

            result = VoteResult(id=idx, legislator_id=legistalator_id, vote_id=vote_id, vote_type=vote_type)
            results.append(result)

    VoteResult.objects.bulk_create(results, ignore_conflicts=True)
