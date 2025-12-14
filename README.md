# VectorDB Similarity

VectorDB similarity is a practice projects the aims:

* Embedding a list of class title and description from walla walla's CS program using Word2Vec

* Storing that embedding in MongoDB

* Fetching and comparing the embedding using cosine similarity to a word of the user's choosing.  


To run the project you will need a the model which is the [word2vec Google News vector](https://github.com/mmihaltz/word2vec-GoogleNews-vectors/blob/master/GoogleNews-vectors-negative300.bin.gz)
I did not include the model as it is large. You will need to unzip it and add it to the folder "model" 

You will also need two dependencies (default version should work): gensim and pymongo. Simply use ```pip install gensim``` and ```pip install pymongo```.


The docker-compose simply sets up a local mongoDB server to start simply run:

```bash
docker compose up
```

Then run main (either with IDE or with CLI)

