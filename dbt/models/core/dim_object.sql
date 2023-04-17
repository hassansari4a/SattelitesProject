{{ config(materialized="table") }}

select
    object_id,		
    object_name,		
    object_number,
    object_type
from {{ ref('stg_satcatdata') }}