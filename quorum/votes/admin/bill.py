from django.contrib import admin

from votes.models import Bill


@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):

    search_fields = [
        'title',
        'primary_sponsor',
    ]

    list_display = [
        'id',
        'title',
        'primary_sponsor',
    ]
