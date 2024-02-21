from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='4b50d6a4ccf74c95bb793c03a536b1ad')



# Fetch all articles
all_articles = newsapi.get_everything(q='economy',#Topic
                                      sources='bbc-news,the-verge',
                                      domains='bbc.co.uk,techcrunch.com',
                                      from_param='2024-02-18',
                                      to='2024-02-20',
                                      language='en',
                                      sort_by='relevancy',
                                      page=1)

articles = all_articles["articles"]

for article in articles:
    print(article["title"]+"=>" + article["description"])
    print("*************************************************************")
