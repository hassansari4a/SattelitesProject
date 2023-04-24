{#
    This macro returns value 'Y' if the satellite is till in orbit
#}
{% macro get_orbiting_status(decay_date) -%}

case when  {{ decay_date }} is null then 'Y' when  {{ decay_date }} is not null then 'N' end

{%- endmacro %}
