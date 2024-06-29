{{ config(
    materialized='table'
) }}

WITH source AS (
    SELECT
        id AS playerId,
        dribblingAttributes.agility,
        dribblingAttributes.balance,
        dribblingAttributes.reactions,
        dribblingAttributes.ballControl,
        dribblingAttributes.dribbling,
        dribblingAttributes.composure
    FROM {{ ref('raw_player_data') }}
)

SELECT * FROM source;
