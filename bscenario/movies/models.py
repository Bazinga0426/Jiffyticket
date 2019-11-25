from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name


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

    def __str__(self):
        return self.title


class Session(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.start} - {self.end}"
