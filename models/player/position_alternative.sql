{{ config(
    materialized='table'
) }}

WITH source AS (
    SELECT
        id AS playerId,
        unnest(positionAlternatives) AS positionAlternative
    FROM {{ ref('raw_player_data') }}
)

SELECT * FROM source;
