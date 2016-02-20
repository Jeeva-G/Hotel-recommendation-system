# Reading hotel details from offering file & user reviews from reviews file.
"""This script reads the json files and make a python list out of it."""
import json

hoteldata = []
with open("/Users/jeevananthamganesan/Hotel-recommendation-system/\
Hotel_review_dataset/offering.json") as f:
    for line in f:
        hoteldata.append(json.loads(line))

reviewdata = []
with open("/Users/jeevananthamganesan/Hotel-recommendation-system/\
Hotel_review_dataset/review.json") as r:
    for line in r:
        reviewdata.append(json.loads(line))
