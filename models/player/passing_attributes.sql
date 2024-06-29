{{ config(
    materialized='table'
) }}

WITH source AS (
    SELECT
        id AS playerId,
        passingAttributes.vision,
        passingAttributes.crossing,
        passingAttributes.freeKickAccuracy,
        passingAttributes.shortPassing,
        passingAttributes.longPassing,
        passingAttributes.curve
    FROM {{ ref('raw_player_data') }}
)

SELECT * FROM source;
