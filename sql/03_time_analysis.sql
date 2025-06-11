-- Crash counts by hour of day
WITH hourly AS (
  SELECT
    CAST(strftime('%H', crash_datetime) AS INTEGER) AS hour_24,
    COUNT(*)                                         AS crash_count
  FROM collisions_clean
  GROUP BY hour_24
)
SELECT
  CASE
    WHEN hour_24 = 0  THEN '12 AM'
    WHEN hour_24 BETWEEN 1  AND 11 THEN printf('%d AM', hour_24)
    WHEN hour_24 = 12 THEN '12 PM'
    ELSE printf('%d PM', hour_24 - 12)
  END AS hour_label,
  crash_count
FROM hourly
ORDER BY hour_24;