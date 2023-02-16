from datetime import date, timedelta
from collections import defaultdict

def next_date_occurence(cycle_date: date, base_date=date.today()) -> date:
    '''
    Return first occurence of the cycle date after the base date
    Default base date is today
    '''
    day = cycle_date.day
    month = cycle_date.month
    year = base_date.year
    estimated_date = date(year, month, day)
    if estimated_date >= base_date:
        next_date = estimated_date  
    else:
        next_date = date(year + 1, month, day)
    return next_date

def transfer_date_from_weekend(date: date) -> date:
    '''Transfer date from Saturday and Sunday to Monday'''
    weekday = date.weekday()
    if weekday in [5, 6]:
        offset = 7-weekday
        date += timedelta(days=offset)
    return date

def get_birthdays_per_week(users: dict) -> defaultdict:
    '''
    Selects birthdays that will be during the week
    Print birtdays timetable per week and return appropriate dictionary
    '''
    today = date.today()
    end_of_the_week = today + timedelta(days=6)
    birthdays = defaultdict(list)

    for user in users:
        name, *_ = user
        b_date = user[name]
        current_b_date = next_date_occurence(b_date, today)
        if current_b_date <= end_of_the_week:
            congr_day = transfer_date_from_weekend(current_b_date)
            if congr_day > end_of_the_week:
                continue
            birthdays[congr_day].append(name) 

    for d, names in birthdays.items():
        w_d = d.strftime('%A')
        names_str = ', '.join(names)
        print(f'{w_d}: {names_str}')

    return birthdays

def main():
    users = [{'Bob': date(1998, 2, 16)}, {'Flint': date(2003, 2, 18)}, {'Flont': date(1980, 1, 19)}]
    birthdays_per_week = get_birthdays_per_week(users)
    return birthdays_per_week
    

if __name__ == '__main__':
    main()




