# Select all female bears' names and ages
select_all_female_bears_return_name_and_age = """
    SELECT
        name,
        age
    FROM bears
    WHERE sex = 'F';
"""

# Select the names of bears that are older than 5 years
select_names_of_bears_older_than_5_years = """
    SELECT
        name
    FROM bears
    WHERE age > 5;
"""

# Select the colors of bears that are alive
select_colors_of_alive_bears = """
    SELECT
        color
    FROM bears
    WHERE alive = 1;
"""

# Select the names of bears that are brown and have a temperament of 'Friendly'
select_names_of_friendly_brown_bears = """
    SELECT
        name
    FROM bears
    WHERE color = 'Brown' AND temperament = 'Friendly';
"""

# Select the names of bears that are either 2 years old or have a temperament of 'Grumpy'
select_names_of_bears_2_years_old_or_grumpy = """
    SELECT
        name
    FROM bears
    WHERE age = 2 OR temperament = 'Grumpy';
"""
