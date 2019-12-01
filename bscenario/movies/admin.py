from django.contrib import admin
<<<<<<< HEAD
from .models import Movie, Person, Session, Cinema
=======
<<<<<<< HEAD
from .models import Movie, Person, Session, Cinema
=======
from .models import Movie, Person, Session
>>>>>>> 9e597fcfa65022848a2577d8cb93fd7fb9f9f705
>>>>>>> 6a246fab5a70703ca261e8ccae458db63a17ccde


class SessionInline(admin.TabularInline):
    model = Session


class MovieAdmin(admin.ModelAdmin):
    inlines = [
        SessionInline,
    ]


admin.site.register(Movie, MovieAdmin)
admin.site.register(Person)
<<<<<<< HEAD
admin.site.register(Cinema)
=======
<<<<<<< HEAD
admin.site.register(Cinema)
=======
>>>>>>> 9e597fcfa65022848a2577d8cb93fd7fb9f9f705
>>>>>>> 6a246fab5a70703ca261e8ccae458db63a17ccde
