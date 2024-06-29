{{ config(
    materialized='table'
) }}

WITH source AS (
    SELECT
        id AS playerId,
        defendingAttributes.interceptions,
        defendingAttributes.headingAccuracy,
        defendingAttributes.standingTackle,
        defendingAttributes.slidingTackle,
        defendingAttributes.defenseAwareness
    FROM {{ ref('raw_player_data') }}
)

SELECT * FROM source;
