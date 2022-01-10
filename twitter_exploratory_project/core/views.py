from django.shortcuts import render
from twitter_exploratory_project.core.toolkit_twitter.recent_search import *
from twitter_exploratory_project.core.toolkit_plot.text_mining import *
from datetime import datetime, timedelta
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import os
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


stop_words_domain=["não","da",
                    "só","pra","vc","pois","lá","outro",
                    "outra","vou","vão","assim","outro",
                    "outra","ter","ver","agora","hoje",
                    "tudo","todos","todo","ah","acho",
                    "achamos","né","ser","vai","alguma",
                    "mas","porém","entretanto",
                    "faz","fazemos","farão",
                    "tbm","fazia","tá","tb","ia",
                    "ir","to","nela","nele","nelas",
                    "neles","naquele","naquueles",
                    "naquelas","naquela","coisa","mim",
                    "tô","aí","n",
                    "pro","é","dessa","vamos","q",
                    "desse","tava","msm","vamo","que","porque",
                    "nem","mano","manos","caras","xd","kkkk","pq","por","cara",
                    "gente","dar","sobre","tão","toda","vezes",
                    "então","viu","vemos","pode","podemos","vez",
                    "vcs","hein","quer","sim","deu","já","demos",
                    "todas","aqui","sei","sabemos","fazer","fiz",
                    "fez","fazemos","vem","vamos","ainda","tanto","nesse"] 


LOCAL_PATH = os.path.dirname(os.path.abspath(__file__))

IMAGE_WORD_CLOUD_TWEETS_PATH = os.path.join(LOCAL_PATH,"static" + os.sep + "css" + os.sep + "word_cloud_tweets.png")

IMAGE_WORD_CLOUD_HASHTAGS_CITATIONS_PATH = os.path.join(LOCAL_PATH,"static" + os.sep + "css" + os.sep + "word_cloud_hashtags_citations.png")

PERSIST_JSON_DATA_PATH = os.path.join(LOCAL_PATH,"temp_file_json_folder")




if os.path.isfile(PERSIST_JSON_DATA_PATH + os.sep + "data_tranfer.json"):

  os.remove(PERSIST_JSON_DATA_PATH + os.sep + "data_tranfer.json")


if os.path.isfile(IMAGE_WORD_CLOUD_TWEETS_PATH):

  os.remove(IMAGE_WORD_CLOUD_TWEETS_PATH)


if os.path.isfile(IMAGE_WORD_CLOUD_HASHTAGS_CITATIONS_PATH):

  os.remove(IMAGE_WORD_CLOUD_HASHTAGS_CITATIONS_PATH)



'''

if os.path.isfile(PERSIST_DATA_TWEET_PATH_RUNNING + os.sep + 'status_system.json'):

     with open(PERSIST_DATA_TWEET_PATH_RUNNING + os.sep + 'status_system.json') as f:

          status_system_data = json.load(f)

          status_system = status_system_data["status"]

          print("\n")
          print("\n")
          print(status_system)
          print("\n")
          print("\n")


else:

          status_system = "Stopped"


'''


def home(request):


     current_date = datetime.utcnow() - timedelta(minutes=10)
     current_date = current_date.strftime("%Y-%m-%dT%H:%M:%S.000Z")

     past_date = datetime.utcnow() - timedelta(days=5) - timedelta(minutes=10)
     past_date = past_date.strftime("%Y-%m-%dT%H:%M:%S.000Z")


     if os.path.isfile(PERSIST_JSON_DATA_PATH + os.sep + "data_tranfer.json"):


          # LOAD data_tweets

          
          file_name_data_tranfer = open(PERSIST_JSON_DATA_PATH + os.sep + "data_tranfer.json", 'r')
          
          data_tranfer_json = json.load(file_name_data_tranfer)

          qnt = int(data_tranfer_json["qnt_tweets"])

          content = data_tranfer_json["query"]


          keyword = "{} lang:pt -is:retweet".format(content)
          
          #start_time = "2021-12-13T00:00:00.000Z"
          #end_time = "2021-12-14T23:07:00.000Z"

          tweet_data = get_data_from_twitter(keyword, start_time=past_date,end_time=current_date,qnt=qnt)






          # Create extra columns


          tweet_data["text_clean"] = tweet_data["text"].apply(lambda x: text_cleaner(text = x,
                                                                                     stop_words_domain=stop_words_domain+[content],
                                                                                     rmv_citations=True,
                                                                                     rmv_hashtags=True))

          tweet_data["citations"] = tweet_data["text"].apply(lambda x: extract_hashtags_citations(tweet = x,extract="citation",remove_content_tweet=True, content=content))
          tweet_data["hashtags"] = tweet_data["text"].apply(lambda x: extract_hashtags_citations(tweet = x,extract="hashtag",remove_content_tweet=True, content=content))
          tweet_data["citations_hashtags"] = tweet_data["text"].apply(lambda x: extract_hashtags_citations(tweet = x,extract="both",remove_content_tweet=True, content=content))
          tweet_data["unique_words"] = tweet_data["text"].apply(lambda x: convert_text_to_no_repeat_words(text = x))
          tweet_data["unique_words_clean"] = tweet_data["text_clean"].apply(lambda x: convert_text_to_no_repeat_words(text = x))





          # create wordcloud
          
          text_tweets_joined = " ".join(review for review in tweet_data.text_clean)

          wordcloud_tweets = WordCloud(max_font_size=300, max_words=70, background_color="black",width=3000, height=1300).generate(text_tweets_joined)

          wordcloud_tweets.to_file(IMAGE_WORD_CLOUD_TWEETS_PATH)



          hashtags_citations_joined = " ".join(review for review in tweet_data.citations_hashtags)

          
          hashtags_citations_joined = re.sub("\#{0}|\@{0}".format(content)," ",hashtags_citations_joined)

          wordcloud_hashtags_citations = WordCloud(include_numbers=True,max_font_size=300, max_words=70, background_color="black",width=3000, height=1300).generate(hashtags_citations_joined)

          wordcloud_hashtags_citations.to_file(IMAGE_WORD_CLOUD_HASHTAGS_CITATIONS_PATH)






          # Create data for plot 

          hashtag_report_count = plot_bar_count_words(text_column='hashtags',
                                                       dataframe=tweet_data,
                                                       metric='SUM',top=10,return_df=True)


          hashtag_report_count["WORDS"] =  "#" + hashtag_report_count["WORDS"]



          citation_report_count = plot_bar_count_words(text_column='citations',
                                                  dataframe=tweet_data,
                                                  metric='SUM',top=10,return_df=True)


          citation_report_count["WORDS"] =  "@" + citation_report_count["WORDS"]



          words_report_count = plot_bar_count_words(text_column='text_clean',
                                                       dataframe=tweet_data,
                                                       metric='SUM',top=10,return_df=True)


          
          words_report_count_bigram = plot_bar_count_words(text_column='text_clean',
                                                       dataframe=tweet_data,
                                                       metric='SUM',top=10,return_df=True, ngram = (2,2))


          words_report_count_trigram = plot_bar_count_words(text_column='text_clean',
                                             dataframe=tweet_data,
                                             metric='SUM',top=10,return_df=True, ngram = (3,3))






          docs_report_count = plot_bar_count_words(text_column='unique_words_clean',
                                                            dataframe=tweet_data,
                                                            metric='SUM',top=10,return_df=True)


          data_plot = {"hashtag_report_count_y": hashtag_report_count["SUM"].tolist(),
                         "hashtag_report_count_x": hashtag_report_count["WORDS"].tolist(),
                         
                         "citation_report_count_y": citation_report_count["SUM"].tolist(),
                         "citation_report_count_x": citation_report_count["WORDS"].tolist(),
                         
                         "words_report_count_y": words_report_count["SUM"].tolist(),
                         "words_report_count_x": words_report_count["WORDS"].tolist(),
                         
                         "docs_report_count_y": docs_report_count["SUM"].tolist(),
                         "docs_report_count_x": docs_report_count["WORDS"].tolist(),

                         "words_report_count_y_bigram": words_report_count_bigram["SUM"].tolist(),
                         "words_report_count_x_bigram": words_report_count_bigram["WORDS"].tolist(),

                         "words_report_count_y_trigram": words_report_count_trigram["SUM"].tolist(),
                         "words_report_count_x_trigram": words_report_count_trigram["WORDS"].tolist(),
                         
                         }



     else:


                    # create wordcloud
          
          text_tweets_joined = "TWEET_0 TWEET_1 TWEET_2 TWEET_3 TWEET_4 TWEET_5 TWEET_6 TWEET_7 TWEET_8 TWEET_9"

          wordcloud_tweets = WordCloud(max_font_size=300, max_words=70, background_color="black",width=3000, height=1300).generate(text_tweets_joined)

          wordcloud_tweets.to_file(IMAGE_WORD_CLOUD_TWEETS_PATH)



          hashtags_citations_joined = "CITATION_0 HASHTAG_0 CITATION_1 HASHTAG_1 CITATION_2 HASHTAG_2 CITATION_3 HASHTAG_3 CITATION_4 HASHTAG_4 CITATION_5 HASHTAG_5 CITATION_6 HASHTAG_6 CITATION_7 HASHTAG_7 CITATION_8 HASHTAG_8 CITATION_9 HASHTAG_9"


          wordcloud_hashtags_citations = WordCloud(include_numbers=True,max_font_size=300, max_words=70, background_color="black",width=3000, height=1300).generate(hashtags_citations_joined)

          wordcloud_hashtags_citations.to_file(IMAGE_WORD_CLOUD_HASHTAGS_CITATIONS_PATH)



          data_plot = {"hashtag_report_count_y": [0,0,0,0,0,0,0,0,0,0],
                         "hashtag_report_count_x": ["word0","word1","word2","word3","word4","word5","word6","word7","word8","word9"],
                         
                         "citation_report_count_y": [0,0,0,0,0,0,0,0,0,0],
                         "citation_report_count_x": ["word0","word1","word2","word3","word4","word5","word6","word7","word8","word9"],
                         
                         "words_report_count_y": [0,0,0,0,0,0,0,0,0,0],
                         "words_report_count_x": ["word0","word1","word2","word3","word4","word5","word6","word7","word8","word9"],
                         
                         "docs_report_count_y": [0,0,0,0,0,0,0,0,0,0],
                         "docs_report_count_x": ["word0","word1","word2","word3","word4","word5","word6","word7","word8","word9"],


                         "words_report_count_y_bigram": [0,0,0,0,0,0,0,0,0,0],
                         "words_report_count_x_bigram": ["word0","word1","word2","word3","word4","word5","word6","word7","word8","word9"],

                         "words_report_count_y_trigram": [0,0,0,0,0,0,0,0,0,0],
                         "words_report_count_x_trigram": ["word0","word1","word2","word3","word4","word5","word6","word7","word8","word9"]

                         }






     return render(request,'index.html',data_plot)





#___________________________________________________________________________________________________________________________________________________________
#ROTA PARA PERSISTIR OS DADOS
@csrf_exempt 
def persist_results(request):

     data_json = json.loads(json.dumps(request.POST))

     print("\n")
     print("\n")
     print("\n")
     print("data: \n")
     print(type(data_json))
     print("\n")
     print("\n")
     print("\n")



     #PERSIST_JSON_DATA_PATH = open(PERSIST_JSON_DATA_PATH + os.sep +"running" + os.sep + "data_tweets.json", 'w+', encoding='utf8')



     file_data_tranfer = open("{}/data_tranfer.json".format(PERSIST_JSON_DATA_PATH), 'w')


     json.dump(data_json, file_data_tranfer)
    
    

     return HttpResponse("status: okay")

