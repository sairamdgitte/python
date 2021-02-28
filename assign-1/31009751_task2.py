"""
Created by Sai Ram (31009751) for Assignment 1 of FIT9136
Start Date: 28/04/2020
End Date: 01/05/2020
Last edit: 01/05/2020


Description: Inventory system of cantilever umbrellas for a company to record the available stock and revenue for a
given year.

"""


# Input to the program
def read_data():
    data_read = ['start_year', 'start_stock', 'start_revenue']
    file = open('AU_INV_START.txt', 'r')
    file1 = file.read().split('\n')
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


# Function for first occurrence of financial year (2009, 2010 and 2011)
def first_fin_crisis(year, qty, list_years):
    lst_qty = list(qty.values())
    if year == list_years[0]:
        lst_qty = [round(i * 0.8) for i in lst_qty]  # Quantity falls to 80%
        # Price per unit is calculated from year 2000 and to 2009 and then increased by 10%
        lst_rev = [round(i * (1.1 ** ((year - 2000) + 1)), 2) for i in rev_list]
        lst_rev = [round(a * b, 2) for a, b in zip(lst_rev, lst_qty)]  # Total revenue is calculated

        return sum(lst_rev)  # Returns the summed up revenue for 2009

    # Similarly for 2010 is carried out
    if year == list_years[1]:
        lst_qty = [round(i * 0.8 * 0.9) for i in lst_qty]  # Quantity falls to 80% (2009) and then 90%(2010)

        # Price increases to 10% (2009) and then 5% (2010)
        lst_rev = [round((i * 1.05 * (1.1 ** ((year - 2000) + 1))), 2) for i in rev_list]
        lst_rev = [round(a * b, 2) for a, b in zip(lst_rev, lst_qty)]  # Total revenue is calculated

        return sum(lst_rev)

    # Similarly for 2011 is carried out
    if year == list_years[2]:
        # Quantity falls to 80% (2009) and then 90%(2010) and then 95%(2011)
        lst_qty = [round(i * 0.8 * 0.9 * 0.95) for i in lst_qty]

        # Price increases to 10% (2009) and then 5% (2010) and then 3%(2011)
        lst_rev = [round((i * 1.05 * 1.03 * (1.1 ** ((year - 2000) + 1))), 2) for i in rev_list]
        lst_rev = [round(a * b, 2) for a, b in zip(lst_rev, lst_qty)]  # Total revenue is calculated

        return sum(lst_rev)

    # Calculate the revenue and stock from 2012 to 2019 considering the 2009, 2010 and 2011 conditions
    if 2012 <= year <= 2019:
        lst_qty = [round(i * 0.8 * 0.9 * 0.95) for i in lst_qty]
        lst_rev = [round((i * 1.05 * 1.03 * (1.1 ** ((year - 2000) + 1))), 2) for i in rev_list]
        lst_rev = [round(a * b, 2) for a, b in zip(lst_rev, lst_qty)]

        return sum(lst_rev)


# Function for second occurrence of financial crisis (2020, 2021 and 2022)
def second_fin_crisis(year, qty, list_years):
    lst_qty = list(qty.values())

    # Similarly for 2020 is carried out
    if year == list_years[0]:

        # Quantity falls to 80% (2009), 90%(2010), 95%(2011) and 80% (2020)
        lst_qty = [round(i * 0.8 * 0.8 * 0.9 * 0.95) for i in lst_qty]  # Quantity falls to 80% (2009) and 80% (2020)

        # Price increases to 10% (2009), then 5% (2010), then 3% (2011) and then 10% (2020)
        lst_rev = [round(i * 1.05 * 1.03 * 1.1 * (1.1 ** ((year - 2000) + 1)), 2) for i in rev_list]
        lst_rev = [round(a * b, 2) for a, b in zip(lst_rev, lst_qty)]

        return sum(lst_rev)  # Total revenue is calculated and returned

    # Similarly for 2021 is carried out
    if year == list_years[1]:
        # Quantity falls to 80% (2009), 90%(2010), 95%(2011), 80% (2020), 90%(2021)
        lst_qty = [round(i * 0.8 * 0.9 * 0.8 * 0.9 * 0.95) for i in lst_qty]

        # Price increases to 10% (2009), then 5% (2010), then 3% (2011), then 10% (2020), 5%(2021)
        lst_rev = [round(i * 1.05 * 1.05 * 1.03 * 1.1 * (1.1 ** ((year - 2000) + 1)), 2) for i in rev_list]
        lst_rev = [round(a * b, 2) for a, b in zip(lst_rev, lst_qty)]

        return sum(lst_rev)  # Total revenue is calculated and returned

    # Similarly for 2022 is carried out
    if year == list_years[2]:

        # Quantity falls to 80% (2009), 90%(2010), 95%(2011), 80% (2020), 90%(2021), 95%(2022)
        lst_qty = [round(i * 0.8 * 0.9 * 0.95 * 0.8 * 0.9 * 0.95) for i in lst_qty]

        # Price increases to 10% (2009), then 5% (2010), then 3% (2011), then 10% (2020), 5%(2021) and 3%(2022)
        lst_rev = [round(i * 1.05 * 1.03 * 1.05 * 1.03 * 1.1 * (1.1 ** ((year - 2000) + 1)), 2) for i in rev_list]
        lst_rev = [round(a * b, 2) for a, b in zip(lst_rev, lst_qty)]

        return sum(lst_rev)  # Total revenue is calculated and returned

    if 2023 <= year <= 2030:

        # Quantity falls to 80% (2009), 90%(2010), 95%(2011), 80% (2020), 90%(2021), 95%(2022)
        lst_qty = [round(i * 0.8 * 0.9 * 0.95 * 0.8 * 0.9 * 0.95) for i in lst_qty]

        # Price increases to 10% (2009), then 5% (2010), then 3% (2011), then 10% (2020), 5%(2021) and 3%(2022)
        lst_rev = [round(i * 1.05 * 1.03 * 1.05 * 1.03 * 1.1 ** ((year - 2000) + 2), 2) for i in rev_list]
        lst_rev = [round(a * b, 2) for a, b in zip(lst_rev, lst_qty)]

        return sum(lst_rev)  # Total revenue is calculated and returned


# Function for third occurrence of financial crisis (2031, 2032 and 2033)
def third_fin_crisis(year, qty, list_years):
    lst_qty = list(qty.values())

    # Similarly for 2031 is carried out
    if year == list_years[0]:

        # Quantity falls to 80% (2009), 90%(2010), 95%(2011), 80% (2020), 90%(2021), 95%(2022), 80%(2031)
        lst_qty = [round(i * 0.8 * (0.8 * 0.9 * 0.95) ** 2) for i in lst_qty]

        # Price increases to 10% (2009), then 5% (2010), then 3% (2011), then 10% (2020), 5%(2021), 3%(2022), 10%(2031)
        lst_rev = [round((i * (1.05 * 1.03) * 1.05 * 1.03 * (1.1 ** ((year - 2000) + 3))), 2) for i in
                   rev_list]
        lst_rev = [round(a * b, 2) for a, b in zip(lst_rev, lst_qty)]

        return sum(lst_rev)  # Total revenue is calculated and returned

    # Similarly for 2032 is carried out
    if year == list_years[1]:

        # Quantity falls to 80% (2009), 90%(2010), 95%(2011), 80% (2020), 90%(2021), 95%(2022), 80%(2031), 90%(2032)
        lst_qty = [round(i * 0.8 * 0.9 * (0.8 * 0.9 * 0.95) ** 2) for i in lst_qty]

        # Price increases to 10%(2009), 5% (2010), 3% (2011), 10% (2020), 5%(2021), 3%(2022), 10%(2031), 5%(2032)
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


def total_financial_crisis_years():
    # Calculate the first occurrence of the financial year e.g(2009, 2020 and 2031)
    first_occurrence_crisis = [i for i in range(2000 + CRIS_RECUR_FREQUENCY, 2040, CRIS_RECUR_FREQUENCY + 2)]

    # From the calculated first occurrences of financial year, calculate the remaining of them
    # e .g (2009, 2010 and 2011)
    first_crisis_years = [i for i in range(first_occurrence_crisis[0], first_occurrence_crisis[0] + years_in_crisis)]
    second_crisis_years = [i for i in range(first_occurrence_crisis[1], first_occurrence_crisis[1] + years_in_crisis)]
    third_crisis_years = [i for i in range(first_occurrence_crisis[2], first_occurrence_crisis[2] + years_in_crisis)]

    return first_crisis_years, second_crisis_years, third_crisis_years


def cal_stock_revenue(year_dictionary):

    year = int(year_dictionary['start_year'])
    available_stock = [1000]
    total_units_sold_per_month = 0
    monthly_defective_items = 0
    total_distribution_per_month = [0]
    total_revenue_quarterly = 0
    total_revenue_generated = 0
    season_dict_qty = {}
    season_dict_rev = {}

    first_crisis_years, second_crisis_years, third_crisis_years = total_financial_crisis_years()

    if 2040 >= year >= 2000:
        for loop in range(2000, year + 1):

            if leap_year(loop):
                year_dict['Feb'] = 29
            else:
                year_dict['Feb'] = 28

            units_per_day_jan = round(qty_list[0] * (1.1 ** (loop - 2000)))
            units_per_day_mar = round(qty_list[1] * (1.1 ** (loop - 2000)))
            units_per_day_jul = round(qty_list[2] * (1.1 ** (loop - 2000)))
            units_per_day_nov = round(qty_list[3] * (1.1 ** (loop - 2000)))

            price_per_unit_jan = round(rev_list[0] * (1.1 ** (loop - 2000)), 2)
            price_per_unit_mar = round(rev_list[1] * (1.1 ** (loop - 2000)), 2)
            price_per_unit_jul = round(rev_list[2] * (1.1 ** (loop - 2000)), 2)
            price_per_unit_nov = round(rev_list[3] * (1.1 ** (loop - 2000)), 2)

            for i in year_dict:
                for j in range(year_dict[i]):

                    if i in ['Jan', 'Feb']:
                        if j > 0:
                            units_per_day_jan = units_per_day_jan
                        else:
                            total_units_sold_per_month = 0  # Start counting units sold pm for Feb, from the beginning

                        available_stock[0] = available_stock[0] - units_per_day_jan

                        while available_stock[0] <= 400:
                            available_stock[0] += 600
                        total_units_sold_per_month += units_per_day_jan

                        if j == year_dict[i] - 1:
                            defective_units = round(total_units_sold_per_month * def_per)
                            monthly_defective_items += defective_units
                            total_units_sold_per_month -= defective_units
                            available_stock[0] += defective_units
                            total_distribution_per_month[0] += total_units_sold_per_month

                            if i == 'Feb':
                                season_dict_qty.update([('Jan-Feb', total_distribution_per_month[0])])
                                total_revenue_quarterly = round((season_dict_qty['Jan-Feb'] * price_per_unit_jan) +
                                                                (monthly_defective_items * price_per_unit_jan * 0.8), 2)
                                season_dict_rev.update([('Jan-Feb', total_revenue_quarterly)])
                                monthly_defective_items = 0

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
                                total_revenue_quarterly += round((season_dict_qty['Nov-Dec'] * price_per_unit_nov) +
                                                                 (monthly_defective_items * price_per_unit_nov * 0.8)
                                                                 - (defective_units * price_per_unit_nov * 0.8), 2)
                                season_dict_rev.update(
                                    [('Nov-Dec', round(total_revenue_quarterly -
                                                       season_dict_rev['Jan-Feb'] - season_dict_rev['Mar-Jun'] -
                                                       season_dict_rev['Jul-Oct'], 2))])
                                total_distribution_per_month[0] = 0
                                monthly_defective_items = 0

        available_stock = available_stock[0]

        total_revenue_generated = sum(list(season_dict_rev.values()))

        if year in first_crisis_years:
            total_revenue_generated = first_fin_crisis(year, season_dict_qty, first_crisis_years)

        if 2012 <= year <= 2019:
            total_revenue_generated = first_fin_crisis(year, season_dict_qty, first_crisis_years)
        if year in second_crisis_years:
            total_revenue_generated = second_fin_crisis(year, season_dict_qty, second_crisis_years)

        if 2023 <= year <= 2030:
            total_revenue_generated = second_fin_crisis(year, season_dict_qty, second_crisis_years)
        if year in third_crisis_years:
            total_revenue_generated = third_fin_crisis(year, season_dict_qty, third_crisis_years)

        if 2034 <= year <= 2040:
            total_revenue_generated = third_fin_crisis(year, season_dict_qty, third_crisis_years)

    return {'end_year': year + 1, 'end_stock': available_stock,
            'end_revenue': round(total_revenue_generated, 2)}


# Check the available stock just for "calculating_stock_revenue" function
def stock_availability(av_stock, days, units):
    av_stock = av_stock - days * units

    while av_stock <= 400:
        av_stock += 600

    return av_stock


# Function to calculate revenue and stock for each days and months
def function_for_months_and_days(start_year, year_sim, months, days, rev, stocks):
    until_months = months
    until_days = days
    revenue = rev
    stock = stocks

    '''Calculating the number of units sold and the price of each unit from Jan-Feb, Mar-Jun, Jul-Oct and Nov-Dec 
        starting from 2000 until start_year+NO_YEAR_SIM '''
    units_per_day_jan = round(qty_list[0] * (1.1 ** ((start_year + year_sim) - 2000)))
    units_per_day_mar = round(qty_list[1] * (1.1 ** ((start_year + year_sim) - 2000)))
    units_per_day_jul = round(qty_list[2] * (1.1 ** ((start_year + year_sim) - 2000)))
    units_per_day_nov = round(qty_list[3] * (1.1 ** ((start_year + year_sim) - 2000)))

    price_per_unit_jan = round(rev_list[0] * (1.1 ** ((start_year + year_sim) - 2000)), 2)
    price_per_unit_mar = round(rev_list[1] * (1.1 ** ((start_year + year_sim) - 2000)), 2)
    price_per_unit_jul = round(rev_list[2] * (1.1 ** ((start_year + year_sim) - 2000)), 2)
    price_per_unit_nov = round(rev_list[3] * (1.1 ** ((start_year + year_sim) - 2000)), 2)

    # Calculating for each days and months given in the input
    for j in month[:until_months]:  # Loop through the months list until the given input month
        if j == 'Jan' or j == 'Feb':
            if j == month[until_months - 1]:
                revenue += until_days * units_per_day_jan * price_per_unit_jan  # Cal the revenue for specified month
                stock = stock_availability(stock, until_days, units_per_day_jan)  # Cal the stock using
            else:
                revenue += year_dict[j] * units_per_day_jan * price_per_unit_jan
                stock = stock_availability(stock, year_dict[j], units_per_day_jan)

        if j == 'Mar' or j == 'Apr' or j == 'May' or j == 'Jun':
            if j == month[until_months - 1]:
                revenue += until_days * units_per_day_mar * price_per_unit_mar
                stock = stock_availability(stock, until_days, units_per_day_jan)
            else:
                revenue += year_dict[j] * units_per_day_mar * price_per_unit_mar
                stock = stock_availability(stock, year_dict[j], units_per_day_jan)

        if j == 'Jul' or j == 'Aug' or j == 'Sep' or j == 'Oct':
            if j == month[until_months - 1]:
                revenue += until_days * units_per_day_jul * price_per_unit_jul
                stock = stock_availability(stock, until_days, units_per_day_jan)
            else:
                revenue += year_dict[j] * units_per_day_jul * price_per_unit_jul
                stock = stock_availability(stock, year_dict[j], units_per_day_jan)

        if j == 'Nov' or j == 'Dec':
            if j == month[until_months - 1]:
                revenue += until_days * units_per_day_nov * price_per_unit_nov
                stock = stock_availability(stock, until_days, units_per_day_jan)
            else:
                revenue += year_dict[j] * units_per_day_nov * price_per_unit_nov
                stock = stock_availability(stock, year_dict[j], units_per_day_jan)
    return revenue, stock


""" Calculating the stock and revenue starting from the initial year (2000) and summing it up until the specified input 
    year + NO_YEAR_SIM"""

# 20090131 var1 = 20000131 to 20090131 20110131 var2 = 20000131 to 20110131 var2-var = 20090131 to 20110131
def calculating_stock_revenue(input_dict):
    rev_start = 0  # Revenue at the begining of input year
    rev_end = 0  # Revenue at the end of NO_YEAR_SIM
    stock_start = 0  # Initialising stock of start year to 0 for further calculation
    stock_end = 0  # Initialising stock of end year to 0 for further calculation
    start_year = int(input_dict['start_year'])  # Input year is taken into start_year variable

    ''' A for loop is run to calculate the revenue and stock from year 2000 until the start_year '''
    for k in range(2000, start_year):
        input_dict['start_year'] = k
        rev_start += float(cal_stock_revenue(input_dict)['end_revenue'])
        stock_start = cal_stock_revenue(input_dict)['end_stock']

    '''Check if the start_year is a leap year or not'''
    if leap_year(start_year):
        year_dict['Feb'] = 29
    else:
        year_dict['Feb'] = 28

    '''until which month and days should the calculation be carried out is given by these 2 variables, respectively '''
    until_months = int(input_dict['start_month'])
    until_days = int(input_dict['start_days'])

    # This gives the sum of revenue and stock from year 2000 until the input yyyymmdd (including days and months)
    rev_start, stock_start = function_for_months_and_days(start_year, 0, until_months, until_days, rev_start,
                                                          stock_start)

    '''Check if the start_year + NO_YEAR_SIM is a leap year or not, if so add an extra day to Feb'''
    if leap_year(start_year + NO_YEAR_SIM - 1):
        year_dict['Feb'] = 29
    else:
        year_dict['Feb'] = 28

    '''Calculating the sum of revenue until the last year (start_year + NO_YEAR_SIM)'''
    for k in range(2000, start_year+NO_YEAR_SIM):
        input_dict['start_year'] = k
        rev_end += float(cal_stock_revenue(input_dict)['end_revenue'])
        stock_end = cal_stock_revenue(input_dict)['end_stock']

    # Revenue for the complete start_year + NO_YEAR+SIM including the days
    rev_end, stock_end = function_for_months_and_days(start_year, NO_YEAR_SIM - 1, until_months, until_days, rev_end,
                                                      stock_end)
    if start_year == 2000:  # Only when the start_year is 2000, add all the values from 2000 till the last year
        rev = rev_end
    else:
        rev = rev_end - rev_start  # Subtract the start_year revenue from the last_year (start_year + NO_YEAR_SIM)

    out = str(start_year+NO_YEAR_SIM) + input_dict['start_month'] + input_dict['start_days']
    return {'end_year': out, 'end_stock': stock_end, 'end_revenue': round(rev + float(input_dict['start_revenue']), 2)}


if __name__ == '__main__':
    # Some variables to be used inside cal_stock_revenue() function
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # List of days in months
    month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']  # List of months
    year_dict = dict(zip(month, month_days))  # Dictionary containing corresponding day values for the months
    rev_list = [705.00, 587.50, 587.5 * 1.05, 587.5 * 1.05 * 1.2]  # List of quarterly revenue for the first year (2000)
    qty_list = [36, 26.67, 29.7, 40.09]  # List of quarterly unit quantity for year 2000
    CRIS_RECUR_FREQUENCY = 9
    years_in_crisis = 3  # No. of years the financial crisis lasts
    NO_YEAR_SIM = 3
    PER_DEF = 5
    def_per = PER_DEF / 100  # Converting the PER_DEF to percentage

    input_data_dict = read_data()  # Reading the input and storing in a variable (input_data_dict is of Dictionary)

    # Splitting the input to get YYYY MM DD
    input_dictionary = {'start_year': input_data_dict['start_year'][:4], 'start_month':
                        input_data_dict['start_year'][4:6], 'start_days': input_data_dict['start_year'][6:],
                        'start_revenue': input_data_dict['start_revenue']}

    # Sending the dictionary as input to calculating_stock_revenue
    output_data_dict = calculating_stock_revenue(input_dictionary)
    write_data(output_data_dict)  # Writing the output to the file (AU_INV_END.TXT)
