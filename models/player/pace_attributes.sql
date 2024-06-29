{{ config(
    materialized='table'
) }}

WITH source AS (
    SELECT
        id AS playerId,
        paceAttributes.acceleration,
        paceAttributes.sprintSpeed
    FROM {{ ref('raw_player_data') }}
)

SELECT * FROM source;
