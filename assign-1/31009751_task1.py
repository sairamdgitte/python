"""
Created by Sai Ram (31009751) for Assignment 1 of FIT9136
Start Date: 04/04/2020
End Date: 28/04/2020
Last edit: 01/05/2020


Description: Inventory system of cantilever umbrellas for a company to record the available stock and revenue for a
given year.

"""


# Input to the program
def read_data():
    data_read = ['start_year', 'start_stock', 'start_revenue']
    file = open('AU_INV_START.txt', 'r')
    file1 = file.read().split("\n")
    data_read = dict(zip(data_read, file1))
    file.close()
    return data_read


# Output to the program
def write_data(writing_data):
    write_file = open('AU_INV_END.txt', 'w')
    file = list(writing_data.values())
    for i in file:
        write_file.write(str(i) + '\n')


# Check if given year is leap or not
def leap_year(simulation_year):
    leap = False
    if simulation_year % 4 == 0:
        leap = True
    return leap


# Function for first occurrence of financial crisis (2009, 2010 and 2011)
def first_fin_crisis(year, qty, list_years):
    lst_qty = list(qty.values())
    if year == list_years[0]:
        # Quantity falls to 80%(2009)
        lst_qty = [round(i * 0.8) for i in lst_qty]  # Quantity falls to 80%
        # Price per unit is calculated from year 2000 and to 2009 and then increased by 10%
        lst_rev = [round(i * (1.1 ** ((year - 2000) + 1)), 2) for i in rev_list]
        lst_rev = [round(a * b, 2) for a, b in zip(lst_rev, lst_qty)]  # Total revenue is calculated

        return sum(lst_rev)  # Returns the summed up revenue for 2009

    # Similarly for 2010 is carried out
    if year == list_years[1]:
        # Quantity falls to 80%(2009),90%(2010)
        lst_qty = [round(i * 0.8 * 0.9) for i in lst_qty]

        # Price increases to 10%(2009), 5%(2010)
        lst_rev = [round((i * 1.05 * (1.1 ** ((year - 2000) + 1))), 2) for i in rev_list]
        lst_rev = [round(a * b, 2) for a, b in zip(lst_rev, lst_qty)]

        return sum(lst_rev)  # Total revenue is calculated and returned

    # Similarly for 2011 is carried out
    if year == list_years[2]:
        # Quantity falls to 80%(2009),90%(2010),95%(2011)
        lst_qty = [round(i * 0.8 * 0.9 * 0.95) for i in lst_qty]

        # Price increases to 10%(2009), 5%(2010), 3%(2011)
        lst_rev = [round((i * 1.05 * 1.03 * (1.1 ** ((year - 2000) + 1))), 2) for i in rev_list]
        lst_rev = [round(a * b, 2) for a, b in zip(lst_rev, lst_qty)]

        return sum(lst_rev)  # Total revenue is calculated and returned

    if 2012 <= year <= 2019:
        # Quantity falls to 80%(2009),90%(2010),95%(2011)
        lst_qty = [round(i * 0.8 * 0.9 * 0.95) for i in lst_qty]

        # Price increases to 10%(2009), 5%(2010), 3%(2011)
        lst_rev = [round((i * 1.05 * 1.03 * (1.1 ** ((year - 2000) + 1))), 2) for i in rev_list]
        lst_rev = [round(a * b, 2) for a, b in zip(lst_rev, lst_qty)]

        return sum(lst_rev)  # Total revenue is calculated and returned


# Function for second occurrence of financial crisis (2020, 2021 and 2022)
def second_fin_crisis(year, qty, list_years):
    lst_qty = list(qty.values())

    # Similarly for 2020 is carried out
    if year == list_years[0]:
        # Quantity falls to 80%(2009),90%(2010),95%(2011),80%(2020)
        lst_qty = [round(i * 0.8 * 0.8 * 0.9 * 0.95) for i in lst_qty]

        # Price increases to 10%(2009), 5%(2010), 3%(2011), 10%(2020)
        lst_rev = [round(i * 1.05 * 1.03 * 1.1 * (1.1 ** ((year - 2000) + 1)), 2) for i in rev_list]
        lst_rev = [round(a * b, 2) for a, b in zip(lst_rev, lst_qty)]

        return sum(lst_rev)  # Total revenue is calculated and returned

    # Similarly for 2021 is carried out
    if year == list_years[1]:
        # Quantity falls to 80%(2009),90%(2010),95%(2011),80%(2020),90%(2021)
        lst_qty = [round(i * 0.8 * 0.9 * 0.8 * 0.9 * 0.95) for i in lst_qty]

        # Price increases to 10%(2009), 5%(2010), 3%(2011), 10%(2020), 5%(2021)
        lst_rev = [round(i * 1.05 * 1.05 * 1.03 * 1.1 * (1.1 ** ((year - 2000) + 1)), 2) for i in rev_list]
        lst_rev = [round(a * b, 2) for a, b in zip(lst_rev, lst_qty)]

        return sum(lst_rev)  # Total revenue is calculated and returned

    # Similarly for 2022 is carried out
    if year == list_years[2]:
        # Quantity falls to 80%(2009),90%(2010),95%(2011),80%(2020),90%(2021),95%(2022)
        lst_qty = [round(i * 0.8 * 0.9 * 0.95 * 0.8 * 0.9 * 0.95) for i in lst_qty]

        # Price increases to 10%(2009), 5%(2010), 3%(2011), 10%(2020), 5%(2021), 3%(2022)
        lst_rev = [round(i * 1.05 * 1.03 * 1.05 * 1.03 * 1.1 * (1.1 ** ((year - 2000) + 1)), 2) for i in rev_list]
        lst_rev = [round(a * b, 2) for a, b in zip(lst_rev, lst_qty)]

        return sum(lst_rev)  # Total revenue is calculated and returned

    if 2023 <= year <= 2030:
        # Quantity falls to 80%(2009),90%(2010),95%(2011),80%(2020),90%(2021),95%(2022)
        lst_qty = [round(i * 0.8 * 0.9 * 0.95 * 0.8 * 0.9 * 0.95) for i in lst_qty]

        # Price increases to 10%(2009), 5%(2010), 3%(2011), 10%(2020), 5%(2021), 3%(2022)
        lst_rev = [round(i * 1.05 * 1.03 * 1.05 * 1.03 * 1.1 ** ((year - 2000) + 2), 2) for i in rev_list]
        lst_rev = [round(a * b, 2) for a, b in zip(lst_rev, lst_qty)]

        return sum(lst_rev)  # Total revenue is calculated and returned


# Function for third occurrence of financial crisis (2031, 2032 and 2033)
def third_fin_crisis(year, qty, list_years):
    lst_qty = list(qty.values())

    # Similarly for 2031 is carried out
    if year == list_years[0]:
        # Quantity falls to 80%(2009),90%(2010),95%(2011),80%(2020),90%(2021),95%(2022),80%(2031)
        lst_qty = [round(i * 0.8 * (0.8 * 0.9 * 0.95) ** 2) for i in lst_qty]

        # Price increases to 10%(2009), 5%(2010), 3%(2011), 10%(2020), 5%(2021), 3%(2022), 10%(2031)
        lst_rev = [round((i * (1.05 * 1.03) * 1.05 * 1.03 * (1.1 ** ((year - 2000) + 3))), 2) for i in
                   rev_list]
        lst_rev = [round(a * b, 2) for a, b in zip(lst_rev, lst_qty)]

        return sum(lst_rev)  # Total revenue is calculated and returned

    # Similarly for 2032 is carried out
    if year == list_years[1]:

        # Quantity falls to 80%(2009),90%(2010),95%(2011),80%(2020),90%(2021),95%(2022),80%(2031),90%(2032)
        lst_qty = [round(i * 0.8 * 0.9 * (0.8 * 0.9 * 0.95) ** 2) for i in lst_qty]

        # Price increases to 10%(2009), 5%(2010), 3%(2011), 10%(2020), 5%(2021), 3%(2022), 10%(2031), 5%(2032)
        lst_rev = [round(i * 1.05 * (1.05 * 1.03) * 1.05 * 1.03 * (1.1 ** ((year - 2000) + 3)), 2) for i in rev_list]
        lst_rev = [round(a * b, 2) for a, b in zip(lst_rev, lst_qty)]

        return sum(lst_rev)  # Total revenue is calculated and returned

    # Similarly for 2033 is carried out
    if year == list_years[2]:
        # Quantity falls to 80%(2009),90%(2010),95%(2011),80%(2020),90%(2021),95%(2022),80%(2031),90%(2032),95%(2033)
        lst_qty = [round(i * (0.8 * 0.9 * 0.95) ** 3) for i in lst_qty]

        # Price increases to 10%(2009), 5%(2010), 3%(2011), 10%(2020), 5%(2021), 3%(2022), 10%(2031), 5%(2032), 3%(2033)
        lst_rev = [round(i * 1.03 * 1.05 * (1.05 * 1.03) * 1.05 * 1.03 * (1.1 ** ((year - 2000) + 3)), 2) for i in
                   rev_list]
        lst_rev = [round(a * b, 2) for a, b in zip(lst_rev, lst_qty)]

        return sum(lst_rev)  # Total revenue is calculated and returned

    if 2034 <= year <= 2040:

        # Quantity falls to 80%(2009),90%(2010),95%(2011),80%(2020),90%(2021),95%(2022),80%(2031),90%(2032),95%(2033)
        lst_qty = [round(i * (0.8 * 0.9 * 0.95) ** 3) for i in lst_qty]

        # Price increases to 10%(2009), 5%(2010), 3%(2011), 10%(2020), 5%(2021), 3%(2022), 10%(2031), 5%(2032), 3%(2033)
        lst_rev = [round(i * 1.03 * 1.05 * (1.05 * 1.03) * 1.05 * 1.03 * (1.1 ** ((year - 2000) + 3)), 2) for i in
                   rev_list]
        lst_rev = [round(a * b, 2) for a, b in zip(lst_rev, lst_qty)]

        return sum(lst_rev)  # Total revenue is calculated and returned


# Function for calculating the years in financial crisis
def total_financial_crisis_years():
    # Calculate the first occurrence of the financial year e.g(2009, 2020 and 2031)
    first_occurrence_crisis = [i for i in range(2000 + CRIS_RECUR_FREQUENCY, 2040, CRIS_RECUR_FREQUENCY + 2)]

    # From the calculated first occurrences of financial year, calculate the remaining of them
    # e .g (2009, 2010 and 2011)
    first_crisis_years = [i for i in range(first_occurrence_crisis[0], first_occurrence_crisis[0] + years_in_crisis)]
    second_crisis_years = [i for i in range(first_occurrence_crisis[1], first_occurrence_crisis[1] + years_in_crisis)]
    third_crisis_years = [i for i in range(first_occurrence_crisis[2], first_occurrence_crisis[2] + years_in_crisis)]

    return first_crisis_years, second_crisis_years, third_crisis_years


# Function for calculating the stock and revenue of the given year
def cal_stock_revenue(year_dictionary):  # Argument is a dictionary from the read_data()
    year = int(year_dictionary['start_year'])  # Converting the year to int and taking it in a variable
    available_stock = [1000]  # Available stock for the year 2000
    total_units_sold_per_month = 0
    monthly_defective_items = 0
    total_distribution_per_month = [0]
    total_revenue_quarterly = 0  # Here quarter is divided as shown : Jan-Feb, Mar-Jun, Jul-Oct and Nov-Dec
    total_revenue_generated = 0  # Revenue generated per year
    season_dict_qty = {}  # A dictionary to hold the values of quarterly sold units
    season_dict_rev = {}  # A dictionary to hold the values of quarterly revenue generated

    # Taking the values of all the financial crisis years from the function total_financial_crisis()
    first_crisis_years, second_crisis_years, third_crisis_years = total_financial_crisis_years()

    # This logic will run from 2000 to 2040
    if 2040 >= year >= 2000:
        for loop in range(2000, year + 1):  # From the year 2000, calculating the remaining revenue and stocks

            if leap_year(loop):  # Check if the input year is a leap year or not, if so add 1 extra day to Feb
                year_dict['Feb'] = 29
            else:
                year_dict['Feb'] = 28

            '''Calculating the number of units sold and the price of each unit from Jan-Feb, Mar-Jun, Jul-Oct and 
            Nov-Dec starting from 2000 until the year specified in the input '''
            units_per_day_jan = round(qty_list[0] * (1.1 ** (loop - 2000)))
            units_per_day_mar = round(qty_list[1] * (1.1 ** (loop - 2000)))
            units_per_day_jul = round(qty_list[2] * (1.1 ** (loop - 2000)))
            units_per_day_nov = round(qty_list[3] * (1.1 ** (loop - 2000)))

            price_per_unit_jan = round(rev_list[0] * (1.1 ** (loop - 2000)), 2)
            price_per_unit_mar = round(rev_list[1] * (1.1 ** (loop - 2000)), 2)
            price_per_unit_jul = round(rev_list[2] * (1.1 ** (loop - 2000)), 2)
            price_per_unit_nov = round(rev_list[3] * (1.1 ** (loop - 2000)), 2)

            for i in year_dict:  # Run a loop inside the dictionary for all the 12 months
                for j in range(year_dict[i]):  # Inside the months, run the loop on the basis of days in them

                    if i in ['Jan', 'Feb']:
                        if j > 0:
                            units_per_day_jan = units_per_day_jan  # For days greater than 0, units is initialised
                        else:
                            total_units_sold_per_month = 0  # Start counting units sold pm for Jan and Feb, from the
                            # beginning
                        # At the same time reduce the units sold per day from the available stock
                        available_stock[0] = available_stock[0] - units_per_day_jan
                        # Make sure the available stock does not fall less than or equal to 400, if so add 600
                        while available_stock[0] <= 400:
                            available_stock[0] += 600
                        total_units_sold_per_month += units_per_day_jan  # Accumulate the no. of units sold per month

                        if j == year_dict[i] - 1:  # On the last day of the month, cal defective and total distribution
                            defective_units = round(total_units_sold_per_month * def_per)
                            monthly_defective_items += defective_units
                            total_units_sold_per_month -= defective_units
                            available_stock[0] += defective_units
                            total_distribution_per_month[0] += total_units_sold_per_month

                            if i == 'Feb':  # On the last day of the month of Feb, cal total revenue and quantity sold
                                season_dict_qty.update([('Jan-Feb', total_distribution_per_month[0])])
                                total_revenue_quarterly = round((season_dict_qty['Jan-Feb'] * price_per_unit_jan) +
                                                                (monthly_defective_items * price_per_unit_jan * 0.8), 2)
                                season_dict_rev.update([('Jan-Feb', total_revenue_quarterly)])
                                monthly_defective_items = 0

                    # Doing the above mentioned method (Jan-Feb) for (Mar-Jun) as well
                    elif i in ['Mar', 'Apr', 'May', 'Jun']:
                        if j > 0:
                            units_per_day_mar = units_per_day_mar
                        else:
                            total_units_sold_per_month = 0  # Start counting units sold pm for Feb, from the beginning

                        available_stock[0] = available_stock[0] - units_per_day_mar
                        while available_stock[0] <= 400:
                            available_stock[0] += 600
                        total_units_sold_per_month += units_per_day_mar

                        if j == year_dict[i] - 1:
                            defective_units = round(total_units_sold_per_month * def_per)
                            monthly_defective_items += defective_units
                            total_units_sold_per_month -= defective_units
                            available_stock[0] += defective_units
                            total_distribution_per_month[0] += total_units_sold_per_month

                            if i == 'Jun':
                                season_dict_qty.update([('Mar-Jun',
                                                         round(total_distribution_per_month[0] - season_dict_qty[
                                                             'Jan-Feb']))])
                                total_revenue_quarterly += round((season_dict_qty['Mar-Jun'] * price_per_unit_mar) +
                                                                 (monthly_defective_items * price_per_unit_mar * 0.8),
                                                                 2)
                                season_dict_rev.update(
                                    [('Mar-Jun', round(total_revenue_quarterly -
                                                       season_dict_rev['Jan-Feb'], 2))])
                                monthly_defective_items = 0

                    # Doing the above mentioned method (Mar-Jun) for (Jul-Oct) as well
                    elif i in ['Jul', 'Aug', 'Sep', 'Oct']:
                        if j > 0:
                            units_per_day_jul = units_per_day_jul
                        else:
                            total_units_sold_per_month = 0  # Start counting units sold pm for Feb, from the beginning

                        available_stock[0] = available_stock[0] - units_per_day_jul
                        while available_stock[0] <= 400:
                            available_stock[0] += 600
                        total_units_sold_per_month += units_per_day_jul
                        if j == year_dict[i] - 1:
                            defective_units = round(total_units_sold_per_month * def_per)
                            monthly_defective_items += defective_units
                            total_units_sold_per_month -= defective_units
                            available_stock[0] += defective_units
                            total_distribution_per_month[0] += total_units_sold_per_month
                            if i == 'Oct':
                                season_dict_qty.update(
                                    [('Jul-Oct',
                                      round(
                                          total_distribution_per_month[0] -
                                          season_dict_qty['Jan-Feb'] - season_dict_qty['Mar-Jun']))])
                                total_revenue_quarterly += round((season_dict_qty['Jul-Oct'] * price_per_unit_jul) +
                                                                 (monthly_defective_items * price_per_unit_jul * 0.8),
                                                                 2)
                                season_dict_rev.update(
                                    [('Jul-Oct', round(total_revenue_quarterly -
                                                       season_dict_rev['Jan-Feb'] - season_dict_rev['Mar-Jun'],
                                                       2))])
                                monthly_defective_items = 0

                    # Doing the above mentioned method (Jul-Oct) for (Nov-Dec) as well
                    elif i in ['Nov', 'Dec']:
                        if j > 0:
                            units_per_day_nov = units_per_day_nov
                        else:
                            total_units_sold_per_month = 0  # Start counting units sold pm for Feb, from the beginning

                        available_stock[0] = available_stock[0] - units_per_day_nov
                        while available_stock[0] <= 400:
                            available_stock[0] += 600
                        total_units_sold_per_month += units_per_day_nov
                        if j == year_dict[i] - 1:
                            defective_units = round(total_units_sold_per_month * def_per)
                            monthly_defective_items += defective_units
                            total_units_sold_per_month -= defective_units
                            available_stock[0] += defective_units
                            total_distribution_per_month[0] += total_units_sold_per_month

                            if i == 'Dec':
                                season_dict_qty.update([('Nov-Dec',
                                                         round(total_distribution_per_month[0]
                                                               - season_dict_qty['Mar-Jun'] - season_dict_qty[
                                                                   'Jan-Feb'] -
                                                               season_dict_qty['Jul-Oct']))])
                                total_revenue_quarterly += ((season_dict_qty['Nov-Dec'] * price_per_unit_nov) +
                                                            (monthly_defective_items * price_per_unit_nov * 0.8)
                                                            - (defective_units * price_per_unit_nov * 0.8))

                                season_dict_rev.update(
                                    [('Nov-Dec', round(total_revenue_quarterly -
                                                       season_dict_rev['Jan-Feb'] - season_dict_rev['Mar-Jun'] -
                                                       season_dict_rev['Jul-Oct'], 2))])
                                total_distribution_per_month = [0]
                                monthly_defective_items = 0

        available_stock = available_stock[0]  # Makes sure the available stock is passed on to the next year
        total_revenue_generated = sum(list(season_dict_rev.values()))  # Calculate the revenue from revenue dictionary

        if year in first_crisis_years:  # Check for year in 2009, 2010 or 2011
            total_revenue_generated = first_fin_crisis(year, season_dict_qty, first_crisis_years)

        if 2012 <= year <= 2019:  # For years between first and second financial crisis would start from 2011's value
            total_revenue_generated = first_fin_crisis(year, season_dict_qty, first_crisis_years)
        if year in second_crisis_years:  # Check for year in 2020, 2021 or 2022
            total_revenue_generated = second_fin_crisis(year, season_dict_qty, second_crisis_years)

        if 2023 <= year <= 2030:  # For years between second and third financial crisis would start from 2022's value
            total_revenue_generated = second_fin_crisis(year, season_dict_qty, second_crisis_years)
        if year in third_crisis_years:  # Check for year in 2031, 2032 or 2033
            total_revenue_generated = third_fin_crisis(year, season_dict_qty, third_crisis_years)

        if 2034 <= year <= 2040:  # For years between third financial crisis and 2040 would start from 2033's value
            total_revenue_generated = third_fin_crisis(year, season_dict_qty, third_crisis_years)

    return {'end_year': year + 1, 'end_stock': available_stock,
            'end_revenue': round(total_revenue_generated + float(year_dictionary['start_revenue']), 2)}


if __name__ == '__main__':
    # Some variables to be used in side cal_stock_revenue() function
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    year_dict = dict(zip(month, month_days))  # Dictionary containing corresponding day values for the months
    rev_list = [705.00, 587.50, 587.5*1.05, 587.5*1.05*1.2]  # List of quarterly revenue for the first year (2000)
    qty_list = [36, 26.67, 29.7, 40.09]  # List of quarterly unit quantity for year 2000
    CRIS_RECUR_FREQUENCY = 9
    years_in_crisis = 3  # No. of years the financial crisis lasts
    NO_YEAR_SIM = 3
    PER_DEF = 5
    def_per = PER_DEF / 100  # Converting the PER_DEF to percentage

    input_data_dict = read_data()  # Reading the input and storing in a variable (input_data_dict is of Dictionary)

    # Sending the dictionary as input to cal_stock_revenue and storing the dictionary in output_data_dict
    output_data_dict = cal_stock_revenue(input_data_dict)
    write_data(output_data_dict)  # Writing the output to the file (AU_INV_END.TXT)
