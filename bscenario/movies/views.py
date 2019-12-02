from django.shortcuts import render, get_object_or_404, redirect, HttpResponse, HttpResponseRedirect, reverse
from .models import Movie, AddPopcorn, AddCoke, Drink
from ..orders.models import Order, FivePromo, TenPromo
from ..orders.forms import OrderModelForm


def index(request):
    movies = Movie.objects.all()
    return render(request, 'pages/home.html', {'movies': movies})


def detail(request, mid):
    movie = get_object_or_404(Movie, pk=mid)
    cinemas = movie.cinema.all()

    if request.method == 'POST':
        form = OrderModelForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.movie = movie

            #total price and promotion
            #strategy
            total_count = order.adult_counts + order.student_counts + order.child_counts

            if total_count >= 10:
                promo = TenPromo
            elif total_count >= 5:
                promo = FivePromo
            else:
                promo = None
            order.promotion = promo
            order.total_price = order.due()

            #decorator Design Pattern
            order.drink = AddCoke(AddPopcorn(Drink("Tea")))

            #check pre-condition
            if movie.ticket_count < total_count:
                return HttpResponse('ticket not enough')
            else:
                movie.ticket_count -= total_count
                movie.save()
            order.save()
            return HttpResponseRedirect(reverse('orders:detail', args=[str(order.pk)]))
    else:
        form = OrderModelForm()

    return render(request, 'movies/detail.html', {'movie': movie, 'form': form, 'cinemas': cinemas})


#factory design pattern
def print_ticket(request, order_id):
    from ..tickets.models import get_ticket_creator
    ticket = get_ticket_creator()

    return render(request, 'movies/print_ticket.html', {'ticket': ticket.print()})


def add_to_wishlist(request):
    return render(request, 'movies/add_to_wishlist_done.html')


def top_rank_movies(request):
    movie = Movie.objects.all()
    return render(request, 'movies/top_rank_movies.html', {'tops': movie})
