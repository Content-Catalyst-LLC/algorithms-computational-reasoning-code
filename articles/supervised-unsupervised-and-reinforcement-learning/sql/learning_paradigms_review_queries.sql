-- Review supervised performance by split.
SELECT split, accuracy, precision, recall, f1
FROM supervised_metrics
ORDER BY CASE split WHEN 'train' THEN 1 WHEN 'test' THEN 2 ELSE 3 END;

-- Review cluster size and cohesion.
SELECT cluster, n, mean_distance_to_centroid
FROM unsupervised_cluster_summary
ORDER BY cluster;

-- Review reward estimates and selection frequency.
SELECT arm, times_selected, observed_mean_reward, true_reward_probability
FROM reinforcement_learning_summary
ORDER BY observed_mean_reward DESC;

-- Surface unresolved governance concerns.
SELECT paradigm, governance_item, review_question
FROM learning_paradigm_governance_register
WHERE status IN ('partial', 'needs_review')
ORDER BY paradigm, governance_item;
