{{ config(
    materialized='table'
) }}

WITH source AS (
    SELECT
        id AS playerId,
        shootingAttributes.positioning,
        shootingAttributes.finishing,
        shootingAttributes.shotPower,
        shootingAttributes.longShots,
        shootingAttributes.volleys,
        shootingAttributes.penalties
    FROM {{ ref('raw_player_data') }}
)

SELECT * FROM source;
