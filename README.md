As of 11 DEC 2020
# DraftKings_Twitter_NLP

The sportsbetting industry is worth over $150 billion and projected to grow as more states legalize sportsbetting.  One of the leaders in the space is DraftKings which went public in April 2020, during the early days of the global COVID 19 pandemic.  On one hand, the pandemic may have helped increase business because people were spending less money on activies.  On the other, many sporting events were cancelled due to the pandemic.  In this project, I compared the Twitter activity between DraftKings and FanDuel (main competitor) and used Natural Language Processing techniques and topic modeling to reveal insights about DraftKings and FanDuel.


# Data Sources
Twitter API to collect tweets on DraftKings and FanDuel using the following hashtags:

    1. DraftKings - [#DraftKings,'#DraftKings_bet, #DK_Assist, #DKSportsbook, #dks, #DraftKingsNews, #dkuk, #DraftKings_AUS, #DKCasino] #8931 Tweets
    2. FanDuel - [#FanDuel, #FDSportsbook, #FanDuelSupport] #5748 Tweets
    Dates of Tweets: 24 NOV - 01 DEC 2020 (Thanksgiving Week) 

# Background
Being an NLP Project, the word cloud below shows a few background notes about DraftKings with the states where sports betting is legal.

![DraftKings Background](/img/DK_Background_wordcloud.png)

# Exploratory Data Analysis
## My first thought was to see if one company had significantly more tweet activity.  Both companies generally had similar trends and the increases seemed to line up with NFL games.  
![Number of Tweets](/img/Num_Tweets.png)


## I compared the number of followers a user had with the number of retweets to try identifying influencers DraftKings could partner with.  I did not identify a strong trend between the number of followers and the number of retweets in this data  
Note: There were two users in this dataset with a lot of retweets.  After further investigation, they were self promoting their own products and I removed them from the dataset.    
![Influencers](/img/Followers%20and%20Retweets.png)


## Next, I wanted to see the distribution of the top user locations between the two companies for potential areas to target increased market share.  The top locations between the companies are very similar, likely due to users that use both platforms. 

![Users by Location](/img/User%20Location.png)


## To better understand user behavior, the pie chart below shows the types of devices used by the users.  

![Source Device](/img/Source%20Device.png)


## I wanted to see if one company had better user sentiment over the other. Sentiment is similar between the companies.
![Sentiment Analysis](/img/Sentiment_Analysis.png)


# Topic Modeling
After processing and cleaning the tweet text, I used TFIDF to vectorize the data.  Using Non-negative Matrix Factorization, I found three topics and determined which topic each tweet was most strongly associated with.  Upon further investigation into samples of each topic, I noticed that there was quite a bit of topic overlap within a tweet.  
    1. Upcoming Games (8% of Tweets)
    2. Picks and Bets (18% of Tweets)
    3. Promotions (73% of Tweets)
    Reconstruction Error: 69

# Conclusion
The two companies are very similar and DraftKings should consider more ways to distinguish themselves in areas such as tweet topics by diversifying their features or products from FanDuel.  With more states legalizing sportsbetting, they could target user bases in those states.  They could take advantage of this relatively reduced sports activities to test out different products.  

# Next Steps
Future twitter analysis could involve deep diving into the comment sectiosn and analyzing the images and GIFs. 
