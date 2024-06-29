{{ config(
    materialized='table'
) }}

WITH source AS (
    SELECT * FROM (
        VALUES
            (0, 'WC', NULL, NULL),
            (1, '3F Superliga', NULL, 'male'),
            (4, '1A Pro League', NULL, 'male'),
            (10, 'Eredivisie', 34, 'male'),
            (13, 'Premier League', 14, 'male'),
            (14, 'EFL Championship', 14, 'male'),
            (16, 'Ligue 1 Uber Eats', 18, 'male'),
            (17, 'Ligue 2 BKT', 18, 'male'),
            (19, 'Bundesliga', 21, 'male'),
            (20, 'Bundesliga 2', 21, 'male'),
            (31, 'Serie A TIM', 27, 'male'),
            (32, 'Serie BKT', 27, 'male'),
            (39, 'MLS', 95, 'male'),
            (41, 'Eliteserien', NULL, 'male'),
            (50, 'cinch Prem', 42, 'male'),
            (53, 'LALIGA EA SPORTS', 45, 'male'),
            (54, 'LALIGA HYPERMOTION', 45, 'male'),
            (56, 'Allsvenskan', 46, 'male'),
            (60, 'EFL League One', 14, 'male'),
            (61, 'EFL League Two', 14, 'male')
    ) AS t(id, name, nationId, gender)
)

SELECT * FROM source;
