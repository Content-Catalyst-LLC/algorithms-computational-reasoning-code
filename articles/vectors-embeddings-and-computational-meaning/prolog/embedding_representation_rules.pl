embedding_quality('Semantic article search', 83.92).
embedding_quality('Case similarity review', 84.20).
embedding_quality('Content recommendation', 80.48).
embedding_quality('Image-text retrieval', 81.80).

similar_to(article_search, document_index).
similar_to(document_index, article_search).
similar_to(policy_review, graph_relationship).
meaning_overclaim_risk(X) :- similar_to(X, _).
