columns = [ 'adult_obesity', 'unemployment', 'food_environment_index', 
            'primary_care_physicians', 'dentists', 'mental_health_providers', 
            'other_primary_care_providers', 'adult_smoking', 'excessive_drinking',
            'motor_vehicle_crash_deaths', 'homicide_rate', 'sexually_transmitted_infections', 
            'health_care_costs', 'diabetes', 'hiv_prevalence_rate', 'violent_crime', 
            'alcoholimpaired_driving_deaths', 'premature_death', 'poor_or_fair_health', 
            'poor_physical_health_days', 'poor_mental_health_days', 'low_birthweight', 
            'physical_inactivity', 'access_to_exercise_opportunities', 'teen_births', 
            'uninsured', 'preventable_hospital_stays', 'diabetic_screening', 
            'mammography_screening', 'high_school_graduation', 'some_college', 
            'children_in_poverty', 'children_in_singleparent_households', 
            'social_associations', 'injury_deaths', 'polution_ppm', 
            'drinking_water_violations', 'severe_housing_problems', 
            'population_living_in_a_rural_area', 'premature_ageadjusted_mortality', 
            'infant_mortality', 'child_mortality', 'food_insecurity', 'limited_access_to_healthy_foods', 
            'drug_poisoning_deaths', 'uninsured_adults', 'uninsured_children', 
            'could_not_see_doctor_due_to_cost', 'children_eligible_for_free_lunch', 
            'income_inequality', 'driving_along_to_work', 'long_commute__driving_alone',
            'population_that_is_not_proficient_in_english', 'population_estimate',
            'median_household_income', 
            ]


def convert_column_to_title(column_name):
    """Takes api column name and converts to human readable title."""

    return " ".join([word.capitalize() for word in column_name.split('_')])



column_to_title = {}

for column in columns:
    title = convert_column_to_title(column)
    column_to_title[column] = title

