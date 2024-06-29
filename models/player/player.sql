{{ config(
    materialized='table'
) }}

WITH source AS (
    SELECT
        id,
        resourceId,
        resourceBaseId,
        futBinId,
        futWizId,
        firstName,
        lastName,
        name,
        commonName,
        height,
        weight,
        gender,
        birthDate,
        age,
        league,
        nation,
        club,
        rarity,
        position,
        skillMoves,
        weakFoot,
        foot,
        attackWorkRate,
        defenseWorkRate,
        totalStats,
        totalStatsInGame,
        color,
        rating,
        ratingAverage,
        pace,
        shooting,
        passing,
        dribbling,
        defending,
        physicality
    FROM {{ ref('raw_player_data') }}
)

SELECT * FROM source;
