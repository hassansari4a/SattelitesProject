{{ config(materialized="table") }}

WITH geocodes AS (
  SELECT Country_name as country_name, Code as country_code
  FROM {{ ref("geocode") }}
)


SELECT
    cl.country_id AS country_id,
    cl.country AS country,
    {{ get_geocode_unmatched('g.country_code') }} as ge0_code,
    g.country_code AS country_geo_code
FROM 
{{ ref("country_lookup") }} as cl
LEFT JOIN
    geocodes as g
ON 
CONCAT('%', LOWER(cl.country), '%')
LIKE CONCAT('%', LOWER(g.country_name), '%')