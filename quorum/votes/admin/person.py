from django.contrib import admin

from votes.models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):

    search_fields = [
        'name',
    ]

    list_display = [
        'id',
        'name',
    ]
