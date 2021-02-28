"""
Created by Sai Ram (31009751) for Assignment 2 of FIT9136
Start Date: 21/05/2020
End Date: 26/05/2020
Last edit: 07/06/2020


Description: To create a list of People of type Patient from the People class and further run a simulation to calculate
the number of cases on a daily basis.

This script requires to import the whole code from file a2_31009751_task1 for inheriting the Person class in order to
create a Patient class

This script also imports random module to generate random values in order to determine the meeting probability of the
patients and their friends

Math module is imported to help create a separate function to round off any floating point numbers to the nearest
integer.

"""

from a2_31009751_task1 import *
import random
import math


# Inheriting Person class and creating a new child class Patient
class Patient(Person):
    """ A class used to represent a Patient
        ...
        Attributes
        ----------
        first_name : str
                first name of the person
        last_name : str
                last name of the person
        health : int
                health point of a patient which ranges between 0 to 100

        Methods
        --------

        get_health()
                returns health point of a patients
        set_health(new_health)
                modifies/sets the health point of a patient
        is_contagious()
                returns true if a patient is contagious and false if patient is not contagious
        infect(viral_load)
                infects the patients based on the viral load passed in as the argument
        sleep()
                makes sure when called, to add 5 health points equivalent to putting a person to sleep
        """
    # Initialising the object with first name, last name and list of friends
    def __init__(self, first_name, last_name, health):
        self.first_name = first_name
        self.last_name = last_name

        self.health = health

        # Initialising the first and last name as that of the parent class
        Person.__init__(self, self.first_name, self.last_name)

    # Method returns the health of a Person object
    def get_health(self):
        return self.health

    # Sets the health of an object only if the new health is between 0 and 100
    def set_health(self, new_health):
        if 0 <= new_health <= 100:
            self.health = rounding_off(new_health)
        else:
            if new_health > 100:
                self.health = 100
            else:
                self.health = 0

    # Method checks if a person is contagious or not. If they are, then it returns True else it return False
    def is_contagious(self):

        if 50 <= self.health <= 100:
            return False
        elif 0 <= self.health <= 49:
            return True

    # Method infects object(s) based on the conditions provided
    def infect(self, viral_load):

        if 0 <= self.health <= 100:

            if self.health <= 29:
                self.set_health(round(self.health - (0.1 * viral_load), 2))

            elif 29 < self.health < 50:
                self.set_health(round(self.health - (1.0 * viral_load), 2))

            else:
                self.set_health(round(self.health - (2.0 * viral_load), 2))

    # Method makes sure when called, to add 5 health points equivalent to putting a person to sleep
    def sleep(self):
        if 0 <= self.health < 96:
            self.set_health(self.health+5)
        elif 96 <= self.health:
            self.set_health(100)
        else:
            self.set_health(0)


# Function to calculate the amount of viral load generated by a person object
def viral_load_lv(health):
    first_component = 5
    second_component = pow((health - 25), 2)
    third_component = 62
    lv = first_component + second_component / third_component
    return lv


# Function which runs the simulation taking the days, meeting probability and patient zero health as parameters
def run_simulation(days, meeting_probability, patient_zero_health):

    list_of_patients = load_patients(patient_zero_health)  # List of people with updated health points
    contagious_people = []

    # Function to run the simulation for the specified number of days
    for i in range(days):
        count = 0

        for j in range(len(list_of_patients)):  # For each patient the loop is run
            if random.random() < meeting_probability:  # The chance of the meet happening
                friends_met = list_of_patients[j].get_friends()  # friends_met is updated to list of friends

                for each in range(len(friends_met)):  # The actual meeting happening takes place

                    if list_of_patients[j].is_contagious() or friends_met[each].is_contagious():
                        # If the person visiting them is contagious, the friend will be infected with the viral load
                        if list_of_patients[j].is_contagious():
                            friends_met[each].infect(viral_load_lv(list_of_patients[j].get_health()))

                        # If the friend is contagious, the person visiting them will be infected with the viral load
                        else:
                            list_of_patients[j].infect(viral_load_lv(friends_met[each].get_health()))

                    # if both the person and the friend are contagious
                    elif list_of_patients[j].is_contagious() and friends_met[each].is_contagious():
                        before_meet_friend_lv = friends_met[each].get_health()
                        before_meet_person_lv = list_of_patients[j].get_health()

                        # Both of them release the viral load and infect each other at the same time
                        friends_met[each].infect(viral_load_lv(before_meet_person_lv))
                        list_of_patients[j].infect(viral_load_lv(before_meet_friend_lv))

        # After end of each day, count the number of contagious people and put everyone the sleep
        for k in range(len(list_of_patients)):
            if list_of_patients[k].is_contagious():
                count += 1
            list_of_patients[k].sleep()
        contagious_people.append(count)  # Keep a record of number of contagious people for each day
    return contagious_people  # Return a list of number of contagious people for each day


# Function to load patients
def load_patients(initial_health):

    df = read_file()  # Calling the read function to get the input in the form of data frame

    # Create a list of name of persons
    name_of_person = []
    for i in range(df.index.size - 1):
        name_of_person.append(df.index[i])

    df['Friends'] = df['Friends'].str.split(', ')  # splitting the values in 'Friends' column to a list of friends

    # create an object Patient for each name in the list "name_of_person" and update people list
    patients = []
    for each in name_of_person:
        unique_name_split = each.split(' ')  # Split first and last name
        if name_of_person.index(each) == 0:
            initial_health = initial_health  # For the first patient in the list initialise the health as passed
        else:
            initial_health = 75  # For all the patients except patient 1 make health point as 75

        # Create a Patient object and update the patients list
        patients.append(Patient(unique_name_split[0], unique_name_split[1], initial_health))

    # Create a list of list and each element of the outter list corresponds to the list of friends of an object
    friends_name = []
    for i in range(df.index.size - 1):  # Loop will run for the number of patients in the list (200)
        friend_list = []  # Each time the list of friends are added, friend_list is reset to empty list
        for friend_name in df.loc[name_of_person[i], 'Friends']:
            for person in patients:
                if friend_name == person.get_name():
                    friend_list.append(person)  # Keep updating the friend list for a particular Patient object

        friends_name.append(friend_list)  # Create a list of list

    # Add friends to each Patient object created, respectively
    for people_index in range(len(patients)):
        for k in range(len(friends_name[people_index])):
            patients[people_index].add_friend(friends_name[people_index][k])

    return patients  # Return the list of people


# Function to round off the floating values
def rounding_off(number):
    integral_decimal_part = list(math.modf(number))  # Separate the integer and decimal part and convert to a list
    if integral_decimal_part[0] < 0.5:  # if the decimal part is less than 0.5, round it down
        return math.floor(number)
    else:  # if the decimal part is more than 0.5, round it up
        return math.ceil(number)


if __name__ == '__main__':

    # load_patients(10)
    # You may add your own testing code within this main block
    # to check if the code is working the way you expect.

    # # This is a sample test case. Write your own testing code here.
    test_result = run_simulation(15, 0.8, 49)
    print(test_result)
    # # Sample output for the above test case (15 days of case numbers):
    # # [8, 16, 35, 61, 93, 133, 153, 171, 179, 190, 196, 198, 199, 200, 200]
    # #
    # # Note: since this simulation is based on random probability, the
    # # actual numbers may be different each time you run the simulation.
    #
    # # Another sample test case (high meeting probability means this will
    # # spread to everyone very quickly; 40 days means will get 40 entries.)
    test_result = run_simulation(40, 1, 1)
    print(test_result)
    # # sample output:
    # # [19, 82, 146, 181, 196, 199, 200, 200, 200, 200, 200, 200, 200, 200,
    # # 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200,
    # # 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200]

# do not add code here (outside the main block).