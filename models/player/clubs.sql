{{ config(
    materialized='table'
) }}

WITH source AS (
    SELECT * FROM (
        VALUES
            (1, 'Arsenal', 13),
            (2, 'Aston Villa', 13),
            (3, 'Blackburn Rovers', 14),
            (4, 'Bolton', 60),
            (5, 'Chelsea', 13),
            (7, 'Everton', 13),
            (8, 'Leeds United', 14),
            (9, 'Liverpool', 13),
            (10, 'Manchester City', 13),
            (11, 'Manchester Utd', 13),
            (12, 'Middlesbrough', 14),
            (13, 'Newcastle Utd', 13),
            (14, 'Nott\'m Forest', 13),
            (15, 'QPR', 14),
            (17, 'Southampton', 14),
            (18, 'Spurs', 13),
            (19, 'West Ham', 13),
            (21, 'FC Bayern München', 19),
            (22, 'Borussia Dortmund', 19),
            (23, 'M\'gladbach', 19)
    ) AS t(id, name, league)
)

SELECT * FROM source;
