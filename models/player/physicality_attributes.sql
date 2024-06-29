{{ config(
    materialized='table'
) }}

WITH source AS (
    SELECT
        id AS playerId,
        physicalityAttributes.jumping,
        physicalityAttributes.stamina,
        physicalityAttributes.strength,
        physicalityAttributes.aggression
    FROM {{ ref('raw_player_data') }}
)

SELECT * FROM source;
