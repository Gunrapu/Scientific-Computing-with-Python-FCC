def add_time(start, duration, start_day = ''):
    # Exclude AM/PM and then split
    start_hour, start_minute = map(int, start[:-3].split(':'))
    duration_hour, duration_minute = map(int, duration.split(':'))
    # Extract AM/PM
    start_ampm = start[-2:]
    days_add = 0

    # Calculate 24-hour clock format
    if start_ampm == "PM" :
        start_hour += 12 

    # Calculate new_hour and new_minute
    new_hour = start_hour + duration_hour
    new_minute = start_minute + duration_minute

    # Convert new_minute to new_hour if minutes >= 60
    if new_minute >= 60:
        hours_add = new_minute // 60
        new_minute -= hours_add * 60
        new_hour += hours_add

    # Find day added and new_hour in that day
    if new_hour > 24:
        days_add = new_hour // 24
        new_hour -= days_add * 24

    # Find AM and PM
    if new_hour > 0 and new_hour < 12:
        start_ampm = 'AM'
    elif new_hour == 12:
        start_ampm = 'PM'
    elif new_hour > 12:
        start_ampm = 'PM'
        new_hour -= 12
    else: # if new_hour == 0
        start_ampm = 'AM'
        new_hour += 12

    if days_add > 0 :
        if days_add == 1 :
            days_later = " (next day)"
        else :
            days_later = " (" + str(days_add) + " days later)"
    else :
        days_later = ""

    weeks = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

    if start_day:
        week = days_add // 7
        i = weeks.index(start_day.lower().capitalize()) + (days_add - 7 * week)
        if i > 6:
            i -= 7
        day = ", " + weeks[i]
    else:
        day = ""

    new_time = str(new_hour) + ":" + \
        (str(new_minute) if new_minute > 9 else ("0" + str(new_minute))) + \
        " " + start_ampm + day + days_later

    return new_time

print(add_time('3:30 PM', '2:12', 'Monday')) 
