{{ config(materialized="view") }}

select
    {{ dbt_utils.surrogate_key(['intldes', 'norad_cat_id'])}} as sat_id,
    cast(intldes as string) as intldes_id,
    cast(norad_cat_id as integer) as norad_id,
    cast(object_type as string) as object_type,
    cast(satname as string) as satellite_name,
    cast(country as string) as country,
    cast(launch as timestamp) as launch_date,
    cast(site as string) as launch_site,
    cast(decay as timestamp) as decay_date,
    {{ get_orbiting_status('decay') }} as is_orbiting,
    cast(period as numeric) as period,
    cast(inclination as numeric) as inclination,
    cast(apogee as numeric) as apogee,
    cast(perigee as numeric) as perigee,
    cast(file as integer) as file,
    cast(launch_year as integer) as launch_year,
    cast(launch_num as integer) as launch_num,
    cast(launch_piece as string) as launch_piece,
    -- cast('CURRENT' as string) as current_tag,
    cast(object_name as string) as object_name,
    cast(object_id as string) as object_id,
    cast(object_number as integer) as object_number
from {{ source("staging", "satcatdata") }}
