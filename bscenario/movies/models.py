from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name


class Cinema(models.Model):
    city = models.CharField(max_length=20)
    name = models.CharField(max_length=30)
    location = models.TextField()

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=20)
    desp = models.TextField()
    country = models.CharField(max_length=20)
    language = models.CharField(max_length=30)
    published = models.DateField()
    duration = models.PositiveIntegerField()
    directors = models.ManyToManyField(Person, related_name='direct_movies')
    actors = models.ManyToManyField(Person, related_name='act_in_movies')
    poster = models.ImageField()
    adult_price = models.DecimalField(max_digits=10, decimal_places=2)
    child_price = models.DecimalField(max_digits=10, decimal_places=2)
    student_price = models.DecimalField(max_digits=10, decimal_places=2)
    cinema = models.ManyToManyField(Cinema)
    ticket_count = models.PositiveIntegerField(default=40)


    def get_charge(self):
        return self.price.get_charge()

    def __str__(self):
        return self.title


class Price:
    def get_charge(self):
        pass


class AdultPrice(Price):
    def get_charge(self):
        return 88


class ChildrensPrice(Price):
    def get_charge(self):
        return 22


class StudentPrice(Price):
    def get_charge(self):
        return 44


class Session(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.start} - {self.end}"


class Constrain:

    def check(self):
        pass
