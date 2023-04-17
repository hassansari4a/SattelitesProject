{{ config(materialized="table") }}

select
    country_id as country_id,
    country as country
from {{ ref('country_lookup') }}