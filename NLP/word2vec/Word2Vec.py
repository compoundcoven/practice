from gensim.models import word2vec
sentences = word2vec.Text8Corpus('./wiki_wakati.txt')
model = word2vec.Word2Vec(sentences, sg=0, vector_size=100, window=5, min_count=5)
model.save("./wiki.model")
