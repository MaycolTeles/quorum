from django.contrib import admin

from votes.models import Vote


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):

    search_fields = [
        'bill__title',
    ]
    
    list_display = [
        'id',
        'bill',
    ]
