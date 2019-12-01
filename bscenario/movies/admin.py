from django.contrib import admin
from .models import Movie, Person, Session, Cinema


class SessionInline(admin.TabularInline):
    model = Session


class MovieAdmin(admin.ModelAdmin):
    inlines = [
        SessionInline,
    ]


admin.site.register(Movie, MovieAdmin)
admin.site.register(Person)
admin.site.register(Cinema)
