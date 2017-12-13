# MIT Confessions Bot

The rise of GPU computing power in the past decade has made it possible to levy deep learning approaches towards different tasks in natural language processing research. One example is text generation, a complex unsupervised learning task. A model must learn the underlying distribution of training data to organize characters or words from a given vocabulary into a coherent structure.
  We implemented and trained multiple recurrent neural network architectures on posts from the MIT Confessions Facebook page, using both character-by-character and word-by-word approaches for text generation. We also designed a model to simulate more popular posts by weighting training samples with the number of 'reactions' received on Facebook. We evaluated models both qualitatively and quantitatively (using perplexity and a novel 'confidence' metric), and found that the best performing model was a word-based LSTM model. 

We scraped all confessions ever posted using this open-source scraper, <a href="https://github.com/minimaxir/facebook-page-post-scraper">Facebook Page Post Scraper</a>. 
The total number of posts as of September 22, 2017 is ~700KB of data. We also took in the comments into our dataset to obtain more data points. In total, our dataset was aound 1.5MB.
