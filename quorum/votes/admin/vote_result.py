from django.contrib import admin

from votes.models import VoteResult


@admin.register(VoteResult)
class VoteResultAdmin(admin.ModelAdmin):

    search_fields = [
        'legislator__name',
        'vote__bill__title',
    ]

    list_display = [
        'id',
        'legislator',
        'vote',
        'vote_type',
    ]
