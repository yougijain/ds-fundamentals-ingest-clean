-- Total and average injuries by borough
SELECT
  borough,
  COUNT(*)                        AS crash_count,
  SUM(number_of_persons_injured)  AS total_injuries,
  AVG(number_of_persons_injured)  AS avg_injuries_per_crash
FROM collisions_clean
GROUP BY borough
ORDER BY total_injuries DESC;