from django.shortcuts import render
from twitter_exploratory_project.core.toolkit_twitter.recent_search import *
from twitter_exploratory_project.core.toolkit_plot.text_mining import *




# Create your views here.

def home(request):

    qnt = 1000

    keyword = "flamengo lang:pt -is:retweet"
    start_time = "2021-12-13T00:00:00.000Z"
    end_time = "2021-12-14T23:07:00.000Z"

    df_tweets = get_data_from_twitter(keyword, start_time,end_time,qnt)


    print(df_tweets)

    return render(request,'index.html')