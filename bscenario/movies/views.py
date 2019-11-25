from django.shortcuts import render, get_object_or_404, redirect, HttpResponse, HttpResponseRedirect, reverse
from .models import Movie
from ..orders.models import Order, FivePromo, TenPromo
from ..orders.forms import OrderModelForm


def index(request):
    movies = Movie.objects.all()
    return render(request, 'pages/home.html', {'movies': movies})


def detail(request, mid):
    movie = get_object_or_404(Movie, pk=mid)

    if request.method == 'POST':
        form = OrderModelForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.movie = movie

            #total price and promotion
            total_count = order.adult_counts + order.student_counts + order.child_counts
            if total_count >= 10:
                promo = TenPromo
            elif total_count >= 5:
                promo = FivePromo
            else:
                promo = None
            order.promotion = promo
            order.total_price = order.due()

            order.save()
            return HttpResponseRedirect(reverse('orders:detail', args=[str(order.pk)]))
    else:
        form = OrderModelForm()

    return render(request, 'movies/detail.html', {'movie': movie, 'form': form})
