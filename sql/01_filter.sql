-- Filter crashes with any injuries or fatalities
SELECT *
FROM collisions_clean
WHERE number_of_persons_injured    > 0
   OR number_of_pedestrians_injured > 0
   OR number_of_persons_killed     > 0;
