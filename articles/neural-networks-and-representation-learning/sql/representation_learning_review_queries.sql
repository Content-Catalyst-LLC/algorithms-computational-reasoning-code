-- Review train/test behavior.
SELECT split, n, accuracy, mean_loss
FROM model_evaluation_summary
ORDER BY split;

-- Identify governance items not complete.
SELECT item, review_question, status
FROM representation_governance_register
WHERE status IN ('partial', 'needs_review')
ORDER BY item;

-- Review strongest embedding similarities.
SELECT left_item, right_item, cosine_similarity
FROM embedding_similarity_examples
ORDER BY cosine_similarity DESC;
