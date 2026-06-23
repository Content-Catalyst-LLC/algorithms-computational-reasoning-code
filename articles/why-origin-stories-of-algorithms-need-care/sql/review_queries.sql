-- Core algorithm origin-story care threads.
SELECT theme_id, origin_care_score, interpretive_status
FROM origin_story_care_map
WHERE interpretive_status = 'core_origin_story_care_thread'
ORDER BY origin_care_score DESC;

-- Themes with high anachronism control.
SELECT theme_id, anachronism_control, origin_care_score
FROM origin_story_care_map
WHERE anachronism_control >= 0.95
ORDER BY anachronism_control DESC;

-- Interpretation cautions.
SELECT caution, meaning
FROM interpretation_cautions
ORDER BY caution;
