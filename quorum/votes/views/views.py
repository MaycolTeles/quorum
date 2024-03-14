from django.shortcuts import render

from votes.models import Bill, Person


def index(request):
    return render(request, 'votes/index.html')


def bills(request):
    bills = Bill.objects.all()
    return render(request, 'votes/bills.html', {'bills': bills})


def bill(request, bill_id):
    bill = Bill.objects.get(pk=bill_id)
    return render(request, 'votes/bill.html', {'bill': bill})


def legislators(request):
    legislators = Person.objects.all()
    return render(request, 'votes/legislators.html', {'legislators': legislators})


def legislator(request, legislator_id):
    legislator = Person.objects.get(pk=legislator_id)
    return render(request, 'votes/legislator.html', {'legislator': legislator})
