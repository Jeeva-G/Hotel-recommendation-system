"""This script will contain the model entities."""
from django.db import models
import numpy as np
# Create your models here.


class Hotel(models.Model):
    """Hotel class which holds details about hotel."""

    name = models.CharField(max_length=200)

    def average_rating(self):
        """Use this funtion to return the average rating for a hotel."""
        all_ratings = map(lambda x: x.rating, self.review_set.all())
        return np.mean(all_ratings)

    def __unicode__(self):
        """Use this to return the hotel name."""
        return self.name


class Review(models.Model):
    """This class holds all the fields in review entity."""

    RATING_CHOICES = (
        (1.0, '1'),
        (2.0, '2'),
        (3.0, '3'),
        (4.0, '4'),
        (5.0, '5'),
    )
    Hotel = models.ForeignKey(Hotel)
    pub_date = models.DateTimeField('date published')
    user_name = models.CharField(max_length=100)
    comment = models.CharField(max_length=1500)
    rating = models.IntegerField(choices=RATING_CHOICES)
