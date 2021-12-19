# For sending GET requests from the API
import requests
# For saving access tokens and for file management when creating and adding to the dataset
import os
# For dealing with json responses we receive from the API
import json
# For displaying the data after
import pandas as pd
# For saving the response data in CSV format
import csv
# For parsing the dates received from twitter in readable formats
import datetime
import dateutil.parser
import unicodedata
#To add wait time between requests
import time


def auth():
    return os.getenv('TOKEN')


def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers


def create_url(keyword, start_date, end_date, max_results = 100):
    
    search_url = "https://api.twitter.com/2/tweets/search/recent" #Change to the endpoint you want to collect data from

    
    
    #change params based on the endpoint you are using
    query_params = {'query': keyword,
                    'start_time': start_date,
                    'end_time': end_date,
                    'max_results': max_results,
                    'expansions': 'author_id',
                    'tweet.fields': 'author_id,conversation_id,created_at,id,in_reply_to_user_id,public_metrics,text',
                    'user.fields': 'id,name,username,created_at',
                    'next_token': {}}
    return (search_url, query_params)


def connect_to_endpoint(url, headers, params, next_token = None):
    params['next_token'] = next_token   #params object received from create_url function
    response = requests.request("GET", url, headers = headers, params = params)
    print("Endpoint Response Code: " + str(response.status_code))
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def paginate(url,headers,next_token=""):

    if next_token:
        
        data = connect_to_endpoint(url[0], headers, url[1],next_token=next_token)
        
    else:
        
        data = connect_to_endpoint(url[0], headers, url[1])

    yield data

    if "next_token" in data.get("meta",{}):

        yield from paginate(url,headers,data["meta"]["next_token"])



def get_data_from_twitter(keyword, start_time,end_time,qnt):

    bearer_token = auth()
    
    headers = create_headers(bearer_token)

    df_tweets = pd.DataFrame(columns=['conversation_id', 'in_reply_to_user_id', 'public_metrics',
           'created_at', 'author_id', 'id', 'text'])
    
    
    limit_iterations = qnt//100 if qnt//100 > 0 else 1
        
    count = 0
    
    url = create_url(keyword, start_time,end_time)
    
    for json_response in paginate(url,headers):
        
        

        df_tweets = pd.concat([df_tweets,pd.DataFrame.from_dict(json_response["data"])])

        count+=1

        if count == limit_iterations:

            break

    df_tweets = df_tweets.reset_index(drop=True)
    
    return df_tweets


