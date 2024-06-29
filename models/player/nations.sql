{{ config(
    materialized='table'
) }}

WITH source AS (
    SELECT * FROM (
        VALUES
            (1, 'Albania'),
            (2, 'Andorra'),
            (3, 'Armenia'),
            (4, 'Austria'),
            (5, 'Azerbaijan'),
            (6, 'Belarus'),
            (7, 'Belgium'),
            (8, 'Bosnia and Herzegovina'),
            (9, 'Bulgaria'),
            (10, 'Croatia'),
            (11, 'Cyprus'),
            (12, 'Czech Republic'),
            (13, 'Denmark'),
            (14, 'England'),
            (15, 'Montenegro'),
            (16, 'Faroe Islands'),
            (17, 'Finland'),
            (18, 'France'),
            (19, 'North Macedonia'),
            (20, 'Georgia')
    ) AS t(id, name)
)

SELECT * FROM source;
