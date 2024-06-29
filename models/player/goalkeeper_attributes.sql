{{ config(
    materialized='table'
) }}

WITH source AS (
    SELECT
        id AS playerId,
        goalkeeperAttributes.diving,
        goalkeeperAttributes.handling,
        goalkeeperAttributes.kicking,
        goalkeeperAttributes.positioning,
        goalkeeperAttributes.reflexes
    FROM {{ ref('raw_player_data') }}
)

SELECT * FROM source;
