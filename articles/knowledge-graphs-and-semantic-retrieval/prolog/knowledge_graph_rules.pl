edge('Information Retrieval', related_to, 'Search Architecture').
edge('Search Architecture', uses, 'Inverted Index').
edge('Search Architecture', uses, 'Ranking Signals').
edge('Ranking Signals', related_to, 'Relevance Models').
edge('Knowledge Graphs', supports, 'Semantic Retrieval').
edge('Semantic Retrieval', uses, 'Entity Resolution').
edge('Semantic Retrieval', uses, 'Graph Traversal').
edge('Knowledge Graphs', requires, 'Provenance').
edge('Provenance', supports, 'Traceability').

risk(entity_confusion).
risk(unsupported_edge).
risk(ontology_drift).
risk(inference_overreach).
risk(dense_node_bias).
