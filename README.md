# to_vec_with_it

## Motivation
This is a pretty minimalist first pass. The intention behind this is to let me interact with a [vector database](https://weaviate.io/) and gain understanding of its capabilities. Thanks to ChatGPT and excellent documentation, I was shocked at how easy this was to assemble.  

I'm quite interested in Semantic Search. I've built a Keyword Search based search engine in [Apache Lucene](https://lucene.apache.org/) for a previous employer, and found it quite inflexible. In the building of it, I read lots of material on all of the work necessary to make a keyword-oriented technology extensible enough to provide semantic capabilities, and wow is it a lot. When I saw content around vector databases begin to be released, I instantly saw potential in it. For those who are new to the subject and technology, [this](https://www.youtube.com/watch?v=klTvEwg3oJ4) is a good place to start.   


## Running
Run `$ sudo docker compose up` to download text2vec and spin up the local db

Run `$ python main.py` however you run python files

Run `$ sudo docker compose down` if you want to write memory to disk

## Goals
The initial goal of building an MVP is complete. There are tons of ways for me to improve this, and tremendous amounts of more work to do to turn this into any kind of product. I'm pausing here for now. 