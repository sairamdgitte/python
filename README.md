# Assignment-1

## Overview
The assignment here is to simulate the stocking level of one product: Cantilever Umbrella, inside an inventory
management system in an Australian firm. The firm provides this product to its distributors together with a
recommended retail price (RRP). 

Here is some information regarding this product and its relevant parties:
1. The Australian firm was established in January 1st, 2000. For the past 20 years, there have been no
changes to the inventory management system. There was also no change in product model in the
past 20 years as it is quite robust design, the product model will not change in the future either.
On January 1st, 2000, when the firm was first open for business, there were 1000 cantilever umbrellas
in stock, the distribution number of the cantilever umbrella on that day to the distributors was 36,
and each cantilever umbrella’s RRP was $705 AUD (This date has taken the peak season, which causes
increase in sales quantity and increase in price, into account, details of peak season is mentioned in
part 2).
Please note when the inventory stock drops to 400, the firm will restock 600 cantilever umbrellas
back to the warehouse (We do not consider any cost related to restocking fee). 

2. Cantilever Umbrella has a peak selling season. It is from 1st November to end of February each year
(Number of days in February is decided by whether that year is a leap year or not).
During the peak season, the company is expected to have a 35% increase in quantity for distribution
(Which means the number of cantilever umbrellas that goes out of the inventory system is increased
by 35%, rounded up to an integer).
It is also expected to have 20% increase in RRP (Recommended Retail Price, contains 2 decimal places,
it will be the same for the rest of the document) during peak season as it is hard to supply enough
umbrellas to meet the demand.

3. The stocking system is updated daily at 11:59 pm. This number has been consistent every day until
the beginning of a new financial year.
At the beginning of the new financial year each year (1st July), the company will impose a 10% increase
in the supply of cantilever umbrellas to its distributors (rounded up) and 5% increase of the RRP due
to inflation. 

4. Based on statistics, global financial crisis happens every 9 years, and lasts for another 2 years, the
number of cantilever umbrella distributed to distributors will drop by 20% in the first year when
global financial crisis hit the market, the number will continue to drop by 10% and 5% for the next 2
years when the economy is recovering.
In order to make up the losses, during the year that a global financial crisis starts, the company will
add an additional 10% increase in RRP to the product, the increase of the product RRP will become
5% in the next year, and 3% the year after to make up the loss. 
During the crisis, the price inflation and increase in quantity for distribution are still valid and
applicable.
Note: the crisis will start on 1st Jan on the 9th year, and end on 31st Dec the 11th year. In this example,
it will start on 1st January, 2009 and ends on 31st Dec, 2011. And there will be another crisis start on
1st January, 2020 etc.
Example of price increase to make up the loss during crisis is: the price increase will start on 1st
January, 2009, and it will have another increase on 1st January, 2010, etc. 

5. It is expected that 5% of items will be defective and returned to warehouse every month.
Defective items will be refurbished and redistributed at 80% of original price (original price is the RRP
at the time the product is returned) in the following months.

This firm assesses the quantity of product distributed and total revenue earned from distributors every year
(The most basic formula for revenue is: Revenue = RRP x total quantity. But please bear in mind you also
need to consider the defective items as well as global financial crisis and inflation and increase over the
supply of cantilever umbrella).
The firm also runs predictions 20 years in advance. (We are currently in year 2020, the company will have a
prediction of this information to year 2040)

# Task 1
Create a function that reads in data, the function name for reading data is called read_data()
Note: This data you are reading should be stored in one single variable which is a dictionary data type,
variable name is up to you.
Make sure the keys are exactly as follows:
{
"start_year": XXX,
"start_stock": XXX,
"start_revenue": XXX
}

Create the second function in your python file that calculate total stock remaining and total revenue of a
single year's cycle.
Note: The function name is cal_stock_revenue(first_variable). (Instead of first_variable, you
should use a descriptive name for the parameter). Example for single year cycle is, 1st Jan, 2000 to 31st Dec
20010, the year can be either normal year or leap year, starting day for the year is always 1st Jan and ending
year is always 31st Dec.
This function should take in one variable which you created based on the reading data part and output one
single dictionary variable that contains the end year in 4 digits, total stock available
at the end of the year and total revenue (2 decimal places if have) it made at the end of the year.
The structure of dictionary is as follows:
{
"end_year": XXX,
"end_stock": XXX,
"end_revenue": XXX
}
Lastly, your python file should have a function that can create a new file called “AU_INV_END.txt”, writing
the data you calculated.
Note: The function name is called write_data(second_variable), the variable is the dictionary
variable that has been output from the cal_stock_revenue function.
The file that you are writing will have the following format (The txt file will have 3 lines inside):
1. Ending year
2. Total stock available
3. Total revenue it made for end year

## Input files
The file that is given as the inpu is called “AU_INV_START.txt” and structure will be the following format:
1. Starting year
2. Total stock available.
3. Total revenue it made for that year

## Output file
The file that the output is written on is called "AU_INV_END.txt" and structure will be of the following format:
1. End year
2. End stock
3. End revenue it made for that year


# Task 2
Using the techniques demonstrated in the previous tasks, create the full simulation of the town in a script. 
Your simulation should adhere to the following algorithm which was created using the overview section:
1. Starting year, date, stock and revenue could be customized inside the “AU_INV_START.txt”
2. Number of years of simulation could be set inside the python file with a constant variable
NO_YEAR_SIM, default value is 3.
3. Percentage of defective items could be adjusted with a constant variable PER_DEF. Default value is
5.
4. The global financial crisis reoccurring frequency can be customized by a constant variable
CRIS_RECUR_FREQUENCY, default value is 9.

## Input files
The file that is given as the inpu is called “AU_INV_START.txt” and structure will be the following format:
1. year-month-date (without the '-')
2. Total stock available.
3. Total revenue it made for that year

## Output file
The file that the output is written on is called "AU_INV_END.txt" and structure will be of the following format:
1. End year
2. End stock
3. End revenue it made for the number of years specified


Tools used: PyCharm

Language: Python 



# Assignment-2
In the past, there have been viral disease epidemics (including the 1918 influenza pandemic) which have got out of
hand. We would like to simulate the way such diseases spread, to better understand how this happens.
In this assignment, I have created the necessary data structure to simulate social links and disease transmission
between people, simulate infections among the population over a period of time, and plot graphs to determine
whether an outbreak is contained or not.
The model I have used is a simplification of the real world; I will not use actual parameters or consider all important
factors. However, this assignment is to understand how such simulations
are written in the real world. 

# The source data
A survey is considered consisting of 200 fake people, all with unique names, and were asked to provide the names of their friends in the
group who they are in regular contact with. Assumming that each person has specified at least one friend, and
each of the person’s friends has also named that person as a friend.
The data to be read is in a file named a2_sample_set.txt. 

The data file consists of 200 records. Each record is recorded on its own line in the file, and consists of a person’s
name, together with all the names of that person’s friends. The real file is 200 lines long, but to illustrate the file
format, just the first two lines of the file are shown here as a sample:
Gill Bates: Jodee Killam, Natacha Osterhoudt, Jom Tones, Verdie Tong, Ossie Digangi
Jom Tones: Marry Blakely, Masako Miguel, Gill Bates
. . .
Syntax of each record line: As seen in the example above, each line of data in the file consists of the first and last
name of a particular person, followed by a colon and a space character “: “ and then the first and last names of
each of their friends (people they are in regular contact with) with each friend’s name separated by a comma and a
space “, ”. 

# Example interpretation of source data above:
1. The first line in the file is the record for Gill Bates. Gill Bates has named the following people as her social
connections: Jodee Killam, Natacha Osterhoudt, Jom Tones, Verdie Tong, and Ossie Digangi. This means that
if Gill Bates is contagious (able to spread the virus), Gill Bates may infect the people she has named, and if
her friends are contagious, they may infect Gill Bates. 
2. On the next line, Jom Tones has named his friends in a similar way, and so on.
3. Note that Gill Bates has named Jom Tones as one of her friends. This means that Jom Tones must also name
Gill Bates as one of his friends. It’s not unusual that may both visit each other, and the virus may travel from
either person to the other. You can assume that this rule is followed for all records in the file. 

# How the virus spreads
## Health of each person
Each person has a number of health points which changes over time depending on a person’s health.
The government has published the following guidance about health points. The number of health points is used to
check if a patient is contagious (i.e. able to infect other people) or not: 

76-100 health points: perfect health, not contagious
75 health points: average health, not contagious
50-74 health points: fair health, not contagious
30-49 health points: contagious
0-29 health points: poor health, contagious. 

When sleeping after each day, each person’s immune system will naturally add 5 health points to that person, up to
a maximum of 100 health points.
Health points are not required to be in an integer form, so each time you need to check if a person is contagious or
not, the person’s current health should be rounded to the nearest integer. The maximum possible health of a
healthy person is 100 (the health point value of each person should be limited to this maximum), and the minimum
possible value is 0. A person with 0 health can still recover, but cannot lose any further health points. 

## Meeting probability
Each day, a person may or may not visit another person for a meeting. For each person, the probability that they will
travel to visit one of their friends depends on social distancing regulations. A single meeting probability parameter
will be applied to all people in the group to determine the effect of a certain level of social distancing. This
probability is a fraction of 1. For example, running the simulation with a meeting probability of 1.0 means that every
day, every person will leave home to visit all of their friends, and all their friends will also travel to visit them during
the same day. A probability of 0.0 means nobody can leave home to visit anyone else, and a probability of 0.333
means there is a 33.3% random chance of each visit happening. 

## Viral load
The virus spreads when a contagious person passes a viral load to a person they are visiting, or a person who has
visited them. The term ‘viral load’ is a measure of the quantity of virus in the air which the other person breathes in
when they are visiting and/or being visited by any contagious person. A person can be affected by a viral load even if
they are already partly sick.
The viral load produced by a contagious person is given by the following formula (where Lv is the viral load
produced, and HPc is the number of health points of the contagious person who spreads the virus): 

<img src="https://latex.codecogs.com/svg.latex?\Large&space;L_{v}=5+\frac{(HP_{c}-25)^2}{62}" title="\Large L_{v}=5+\frac{(HP_{c}-25)^2}{62}" />

A small viral load will not make a healthy patient sick, but a larger viral load or viral loads from several people might
reduce a patient’s health to the point that they become contagious with the disease and begin to spread it to others.
Also, our Lv formula shows that a contagious person who is only mildly sick may produce a larger viral load than a
person whose health has worsened, due to the nature of this disease. 

## Effect of infection
When a contagious person produces a viral load, every person they meet when visiting (or being visited) will be
infected by their viral load. If the viral load is small, or a person is healthy, the person who is infected might not
become sick, and they will quickly recover their health later when they sleep. 

The change in health from receiving a viral load from another person is given by the following formula (where HPa is
the current health points of the recipient before the viral load hits them, and HPb is the new value of person’s health
points after receiving the viral load). The formula is different depending on the health of the person who receives
the viral load: 

HP = HP - (0.1 * Lv), if HP <= 29
HP = HP - (1.0 * Lv), if 29 < HP < 50
HP = HP - (2.0 * Lv), if 50 <= HP

## Task 1 Representing social connections in your program
### Loading people
1. Opens the data file which contains the data set given.
2. Creates a new Person object for each record (line) in the file, which contains the name of the person
represented by that record.
3. Where a person’s record indicates that they have friends, you should use the addFriend() method to add
each friend to that Person object. 3
4. Finally, return a list of all the Person objects that have been created from the file records (making sure to
have closed the file first). 


## Task 2 To simulate disease spread 
### Loading patients
1. Reads from the data file.
2. Creates a new Patient object for each record (line) in the file, which contains the name of the person
represented by that record. For each Patient object created, you should assign the health value given by
the default_health argument, since the initial health of each person is not listed in the file.
3. Where a person’s record indicates that they have friends, you should use the inherited add_friend
method to add each friend to that Person object.
4. Finally, return a list of all the Patient objects that have been created from the file records. 


### Running simulations
1. Take in the following arguments:
    a. days: the integer number of days the simulation should run for.
    b. meeting_probability: the fractional probability that any person may visit a certain friend on
        a certain day. 0.0 means 0% chance, 1.0 means 100% chance. (This was explained in section 2.)
    c. patient_zero_health: the initial health of the first person in the file. (See below.) If the
    (rounded) initial health is less than or equal to 49, this person is contagious and there may be
    the chance of a disease outbreak.
2. Use your load_patients function to load patient data from the disk. The first patient in the returned
list (who we will call ‘patient zero’) should be given the starting health value specified in the
patient_zero_health argument. The remaining patients should be given an initial health value of
75, which is the average health of the population from section 2.
3. Run through each day of the simulation. For each day, do the following:
a. For each patient in the group, look at each of the person’s friends, and randomize whether the
person should meet that friend today. 7
 The probability for this to happen is given by the
meeting_probability argument. If the meeting takes place, each person in that pair who is
contagious 8
 should spread a viral load to the other person, by calling the infect() method on
the other person. You will need to calculate what viral load to infect each friend with according
to the rules in section 2.
b. After all meetings have completed for the day, check how many people are now contagious in
the simulation. 


## Task 3 Visualise the curve
1. Runs the simulation by calling the run_simulation function with the specified arguments for days,
meeting_probability, patient_zero_health.
2. After the simulation is complete, prints the whole daily list of contagious patient counts from the returned
data.
3. Then, using functionality from either the matplotlib or pandas library, plot a curve showing the daily
number of contagious patients over the number of days of the simulation. The days of the simulation should
be on the X axis and the contagious patient count on the Y axis. Your graph should have the X and Y axis
labelled accordingly. 




