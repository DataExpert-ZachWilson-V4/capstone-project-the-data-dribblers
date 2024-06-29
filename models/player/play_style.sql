{{ config(
    materialized='table'
) }}

WITH source AS (
    SELECT
        id AS playerId,
        unnest(playStyles) AS playStyle
    FROM {{ ref('raw_player_data') }}
)

SELECT * FROM source;
