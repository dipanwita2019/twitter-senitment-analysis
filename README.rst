=================
twitter-sentiment
=================

A quick introduction of sentiment analysis on twitter data, saving the result ine elastic search and visualizing the data in kibana


Steps:

1. using the docker-compose.yml file in the docker folder build a docker elasticsearchand-kibana image and then run the container

            docker build -rm -t=elasticsearch-kibana .

            docker-compose up -d
            
   The elastic serach server is running locally : at 0.0.0.0:9200 and kibana: at 0.0.0.0:5601

2. Run the twitter_sentiment.py file which queries the tweets for the search terms, calculates the sentiments and stores the needed fields in the elastic search.

3. Open the browser for the elastic search and see if you make few queries on the elastic search data store.
            example: http://localhost:9200/sentiment/_search?q=term
            
4. Then open Kibana : go to index pattern -> create a new index pattern -> add date as the index --> go to visualization --> pie chart --> aggregation(Terms),
Field(sentiment.keyword) -> go.

So Simple.....Go try now !! :)
