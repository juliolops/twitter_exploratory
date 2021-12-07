from django.shortcuts import render
from twitter_exploratory_project.core.toolkit_twitter.recent_search import *




# Create your views here.

def home(request):

    qnt = 610

    keyword = "flamengo lang:pt -is:retweet"
    start_time = "2021-12-03T00:00:00.000Z"
    end_time = "2021-12-04T23:07:00.000Z"

    df_tweets = get_csv_from_twitter(keyword, start_time,end_time,qnt)


    print(df_tweets)

    return render(request,'index.html')