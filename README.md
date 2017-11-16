# MIT Confessions Bot

We used publicly posted data from MIT Confessions, a Facebook page where members of the MIT community can post 
anonymously about any aspect of life at the Institute. We have scraped all confessions ever posted using this open-source scraper,
<a href="https://github.com/minimaxir/facebook-page-post-scraper">Facebook Page Post Scraper</a>. 
The total number of posts as of September 22, 2017 is ~700KB of data. We also took in the comments into our dataset to obtain more data points. In total, our dataset will be at least 1.5MB 
 
We built a model that learns how to create ‘MIT-style’ confessions. We used an LSTM to generate text.
