from abc import ABC, abstractmethod
from django.db import models
from django.contrib.auth import get_user_model
<<<<<<< HEAD
from ..movies.models import Movie, Session, Cinema
=======
from ..movies.models import Movie, Session
>>>>>>> 9e597fcfa65022848a2577d8cb93fd7fb9f9f705


class Order(models.Model):
    # STUDENT = 'ST'
    # ADULT = 'AD'
    # CHILD = 'CH'
    # CUSTOMER_TYPE_CHOICES = [
    #     (STUDENT, 'Student'),
    #     (ADULT, 'Adult'),
    #     (CHILD, 'Child')
    # ]

    OPEN = 'OP'
    CANCELLED = 'CANCELLED'
    COMPLETED = 'COMPLETED'
    STATUS_CHOICES = (
        (OPEN, 'Open'),
        (CANCELLED, 'Cancelled'),
        (COMPLETED, 'Completed')
    )

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    # customer_type = models.CharField(max_length=10, choices=CUSTOMER_TYPE_CHOICES, default=ADULT)
    adult_counts = models.PositiveIntegerField()
    student_counts = models.PositiveIntegerField()
    child_counts = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=OPEN)
<<<<<<< HEAD
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
=======
>>>>>>> 9e597fcfa65022848a2577d8cb93fd7fb9f9f705

    def total(self):
        return self.movie.adult_price * self.adult_counts + self.movie.student_price * self.student_counts + self.movie.child_price * self.child_counts

    promotion = None
<<<<<<< HEAD
=======

>>>>>>> 9e597fcfa65022848a2577d8cb93fd7fb9f9f705
    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self, self)
        return float(self.total()) - discount


<<<<<<< HEAD
#strategy
=======
>>>>>>> 9e597fcfa65022848a2577d8cb93fd7fb9f9f705
class Promotion(ABC):

    @abstractmethod
    def discount(self, order):
        pass


class FivePromo(Promotion):
    """five tickets discount"""

    def discount(self, order):
        return float(order.total()) * 0.15


class TenPromo(Promotion):
    """ten tickets discount"""

    def discount(self, order):
        return float(order.total()) * 0.3
