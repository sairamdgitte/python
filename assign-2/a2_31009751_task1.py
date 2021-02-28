"""
Created by Sai Ram (31009751) for Assignment 2 of FIT9136
Start Date: 18/05/2020
End Date: 21/05/2020
Last edit: 08/06/2020


Description: To create a list of People of type Person from the given sample data set

This script requires that `pandas` be installed within the Python
environment you are running this script in.
"""

import pandas as pd


class Person:
    """ A class used to represent a Person
    ...
    Attributes
    ----------
    first_name : str
            first name of the person
    last_name : str
            last name of the person

    Methods
    --------

    add_friend(friend_person)
            adds friends to the person object
    get_name()
            returns the name of the person object
    get_friends()
            returns the list of friends the person has

    """

    # Initialising the object with first name, last name and an empty list of friends
    def __init__(self, first_name, last_name):
        self.friend_list = []
        self.first_name = first_name
        self.last_name = last_name

    # Method adds friends to the object
    def add_friend(self, friend_person):
        self.friend_list.append(friend_person)

    # Method returns the name of the object
    def get_name(self):
        return self.first_name + ' ' + self.last_name

    # Method returns the list of friends an object Person has
    def get_friends(self):
        lists = []
        for i in range(len(self.friend_list)):
            lists.append(self.friend_list[i])
        return lists


# function to load people in and return a list of all the 200 people as Person object
def load_people():
    df = read_file()  # Get the read data frame here to start working on the data set

    # Create a list of name of persons
    name_of_person = []
    for i in range(df.index.size - 1):
        name_of_person.append(df.index[i])

    df['Friends'] = df['Friends'].str.split(', ')  # splitting the values in 'Friends' column to a list of friends

    people = []

    # create an object Person for each name in the list "name_of_person" and update people list
    for each in name_of_person:
        unique_name_split = each.split(' ')
        people.append(Person(unique_name_split[0], unique_name_split[1]))

    # Create a list of list and each element of the outter list corresponds to the list of friends of an object
    friends_name = []
    for i in range(df.index.size - 1):  # Loop will run for the number of people in the list (200)
        friend_list = []  # Each time the list of friends are added, friend_list is reset to empty list
        for each_friend_name in df.loc[name_of_person[i], 'Friends']:
            for person in people:
                if each_friend_name == person.get_name():
                    friend_list.append(person)  # Keep updating the friend list for a particular Person object

        friends_name.append(friend_list)

    # Add friends to each Person object created, respectively
    for people_index in range(len(people)):
        for k in range(len(friends_name[people_index])):
            people[people_index].add_friend(friends_name[people_index][k])

    return people  # Return the list of people


def read_file():
    open_file = open('a2_sample_set.txt', 'r')  # Open the file in read mode
    reading_data = open_file.read().split('\n')  # Split the contents over the new line delimiter
    df = pd.DataFrame([i.split(': ') for i in reading_data],
                      columns=['Name', 'Friends'])  # Make two columns in data frame 'Name' and 'Friends'

    df = df.set_index('Name')  # Make the column 'Name' as the index in the data frame
    open_file.close()  # Close the file
    return df


if __name__ == '__main__':
    lst = load_people()
    print(lst[0].get_friends()[0].get_name())


# do not add code here (outside the main block).
