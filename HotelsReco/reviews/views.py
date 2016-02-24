"""URLs with reviews and empty suffix will be pointed this page."""
from django.shortcuts import get_object_or_404, render

from .models import Review, Hotel


def review_list(request):
    """Use this function to display the list of reviews."""
    latest_review_list = Review.objects.order_by('-pub_date')[:9]
    context = {'latest_review_list': latest_review_list}
    return render(request, 'reviews/review_list.html', context)


def review_detail(request, review_id):
    """Use this function to display the detail for each review."""
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'reviews/review_detail.html', {'review': review})


def Hotel_list(request):
    """Use this function to display the hotel list."""
    hotel_list = Hotel.objects.order_by('-name')
    context = {'hotel_list': hotel_list}
    return render(request, 'reviews/Hotel_list.html', context)


def Hotel_detail(request, hotel_id):
    """Use this function to display the detail for each Hotel."""
    hotel = get_object_or_404(Hotel, pk=hotel_id)
    return render(request, 'reviews/Hotel_detail.html', {'hotel': hotel})
