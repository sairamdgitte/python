"""
Created by Sai Ram (31009751) for Assignment 2 of FIT9136
Start Date: 26/05/2020
End Date: 27/05/2020
Last edit: 07/06/2020


Description: To visualise the data produced with the help of a2_31009751_task1 and a2_31009751_task2 to study the trend
of spread of the virus

This script requires to import the whole code from file a2_31009751_task2

This script also imports pyplot module from mathplotlib to plot the graphs of the data

"""

from a2_31009751_task2 import *
from matplotlib import pyplot as plt


# Function to plot/visualise the number of contagious cases for a given number of days
def visual_curve(days, meeting_probability, patient_zero_health):
    contagious_count = run_simulation(days, meeting_probability, patient_zero_health)  # get the cases count per day
    print(contagious_count)

    x_axis = []  # List of total days the simulation ran for
    for i in range(len(contagious_count)):
        x_axis.append(i)

    plt.plot(x_axis, contagious_count)  # plotting the graph with x-axis: no. of days and y-axis: contagious count
    plt.xlabel('Days')  # Labelling x-axis as 'Days'
    plt.ylabel('Count')  # Labelling y-axis as 'Count'

    """ The following code can be uncommented and can be used to update the scenario_A, scenario_B and 
    scenario_C files """
    # plt.savefig('scenario_A.png')
    # plt.savefig('scenario_B.png')
    # plt.savefig('scenario_C.png')
    plt.show()


if __name__ == '__main__':
    sim_days = int(input('Days: '))  # Variable to hold the value of number of days
    sim_meeting_probability = float(input('Meeting Probability: '))  # Variable to hold the meeting probability
    sim_patient_zero_health = int(input('Patient zero health: '))  # Variable to hold the health of the first patient

    # calling the function to plot and visualize the curve with the user inputs as parameters
    visual_curve(sim_days, sim_meeting_probability, sim_patient_zero_health)


# do not add code here (outside the main block).
