{{ config(
    materialized='table'
) }}

WITH source AS (
    SELECT
        id AS playerId,
        unnest(playStylePluses) AS playStylePlus
    FROM {{ ref('raw_player_data') }}
)

SELECT * FROM source;
