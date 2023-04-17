{{ config(materialized="table") }}

with satcat_data as (
    select *
    from {{ ref('stg_satcatdata') }}
), 
dim_countries as (
    select * 
    from {{ ref('dim_countries') }}
),
dim_object as (
    select * 
    from {{ ref('dim_object') }}
)
select
    satcat_data.sat_id,
    satcat_data.intldes_id,
    satcat_data.norad_id,
    satcat_data.satellite_name,
    dim_countries.country,
    satcat_data.launch_date,
    satcat_data.decay_date,
    satcat_data.is_orbiting,
    satcat_data.launch_site,
    satcat_data.launch_num,
    satcat_data.launch_piece,
    satcat_data.launch_year,
    satcat_data.period,
    satcat_data.inclination,
    satcat_data.apogee,
    satcat_data.perigee,
    satcat_data.file,
from satcat_data
inner join dim_countries
on satcat_data.country = dim_countries.country_id
inner join dim_object
on satcat_data.intldes_id = dim_object.object_id
order by satcat_data.launch_date asc

