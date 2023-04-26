{#
    This macro returns value 'Y' if the satellite is till in orbit
#}
{% macro get_orbiting_status(decay_date) -%}

CASE
    WHEN {{ decay_date }} IS NULL THEN 'Y' WHEN {{ decay_date }} IS NOT NULL THEN 'N'
END

{%- endmacro %}
