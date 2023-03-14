from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import Avg
from .models import Beer, Review


def recalc_beer_rating(beer: Beer):
    reviews = Review.objects.filter(beer=beer)
    _current_rating = reviews.aggregate(Avg('grade'))
    beer.current_rating = _current_rating['grade__avg'] if _current_rating['grade__avg'] else 0
    beer.save()


@receiver(post_save, sender=Review)
def calc_beer_rating_post_save(sender, instance, created, **kwargs):
    recalc_beer_rating(instance.beer)


@receiver(post_delete, sender=Review)
def calc_beer_rating_post_delete(sender, instance, **kwargs):
    recalc_beer_rating(instance.beer)
