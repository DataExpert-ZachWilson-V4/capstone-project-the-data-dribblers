{{ config(
    materialized='table'
) }}

WITH source AS (
    SELECT * FROM (
        VALUES
            (0, 'Non-Rare'),
            (1, 'Rare'),
            (3, 'TOTW'),
            (4, 'Hero'),
            (5, 'TOTY'),
            (6, 'Record Breaker'),
            (7, 'Unknown'),
            (8, 'MOTM'),
            (9, 'Unknown'),
            (10, 'Professional Player card'),
            (11, 'TOTS'),
            (12, 'Icon'),
            (16, 'FUTTIES'),
            (18, 'FUT Champions'),
            (21, 'Ones To Watch'),
            (22, 'Rulebreakers'),
            (24, 'Squad Building Challenge'),
            (25, 'Squad Building Challenge Premium'),
            (28, 'Award Winner'),
            (30, 'FUT Birthday')
    ) AS t(id, name)
)

SELECT * FROM source;
