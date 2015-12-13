# Opinion-Polling-Using-Exotel-API
Getting Live Sentiment of audiance using Exotel API and Visualizing the result using Kibana

### Steps :

1. Created an Exotel API using Exotel dashboard.

2. Used IRV system and sms event as a callback function.

3. Install ngrok (It provide public ip for Localhost).
 (https://ngrok.com/)

4. pass the url of ngrok to exotel API

5. Using Flask collect the query parameters and pass it to elacticsearch database.

6. Used Kibana to visualize the live data.
