"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO: define the 'EXPECTED_BAKE_TIME' constant.
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_time_in_minutes):
    bake_time_remaining = EXPECTED_BAKE_TIME - elapsed_time_in_minutes
    return bake_time_remaining

    """Calculate the bake time remaining
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.
    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """



#TODO: Define the 'preparation_time_in_minutes()' function below.
# You might also consider using 'PREPARATION_TIME' here, if you have it defined.
def preparation_time_in_minutes(number_of_layers):

    preparationTime = number_of_layers * PREPARATION_TIME 
    return preparationTime 

    
    """Calculate the preparation time in minutes.
    :param layers: int - the number of layers you want to add to the lasagna.
    :return: int - the total preparation time.
    Function that takes the number of layers you want to add to the lasagna as
    an argument and returns how many minutes you would spend making them.
    """


#TODO: define the 'elapsed_time_in_minutes()' function below.
# Remember to add a docstring (you can copy and then alter the one from bake_time_remaininelapsed_time_in_minutes(number_of_layers,bake_time_remaining):
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time

    
    """Calculate the elapsed time in minutes.
    :param layers: int - the number of layers you want to add to the lasagna.
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - the total elapsed time.
    Function that takes two arguments:
    1. the number of layers you want to add to the lasagna.
    2. the number of minutes the lasagna has been baking in the oven.
    The function should return how many minutes in total you've worked on cooking the lasagna.
    """