# Reading hotel details from offering file & user reviews from reviews file.
"""This script reads the json files and make a python list out of it."""
# import json
import ujson
import pandas as pd

hotellist = []
with open("/Users/jeevananthamganesan/Documents/\
Hotel_review_dataset/offering.json") as f:
    for line in f:
        h = ujson.loads(line)
        hotellist.append(
                         {"offering_id": h["id"],
                             "Hotel": h["name"]
                          }
        )

hoteldata = pd.DataFrame(hotellist)

reviewlist = []
with open("/Users/jeevananthamganesan/Documents/\
Hotel_review_dataset/review.json") as f:
    for line in f:
        d = ujson.loads(line)
        reviewlist.append(
            {"offering_id": d["offering_id"],
             "username": d["author"]["username"],
             "pub_date": d["date"],
             "comment": d["text"],
             "comment": d["ratings"]["overall"]
             }
        )

reviewdata = pd.DataFrame(reviewlist)

pd.set_option('display.expand_frame_repr', False)
data = pd.merge(hoteldata, reviewdata, how='inner')
