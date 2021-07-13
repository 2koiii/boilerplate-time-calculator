def add_time(start, duration, days=False):
    
    week_index = {'monday': 0, 'tuesday': 1, 'wednesday': 2, 'thursday': 3, 'friday': 4, 'saturday': 5, 'sunday': 6}
    week_array = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    d_sp = duration.split(':')
    d_hours = int(d_sp[0])
    d_minutes = int(d_sp[1])

    s_sp = start.split(':')
    sM_sp = s_sp[1].split()
    s_hours = int(s_sp[0])
    s_minutes = int(sM_sp[0])
    period = sM_sp[1]
    am_pm_flip = {'AM':'PM', 'PM':'AM'}

    amt_of_days = int(d_hours / 24)

    new_minutes = s_minutes + d_minutes
    if new_minutes >= 60:
        s_hours += 1
        new_minutes = new_minutes % 60
    amount_of_am_pm_flips = int((s_hours + d_hours) / 12)
    new_hours = (s_hours + d_hours) % 12
    
    new_minutes = new_minutes if new_minutes > 9 else '0' + str(new_minutes)
    new_hours = new_hours = 12 if new_hours == 0 else new_hours
    if(period == 'PM' and s_hours + (d_hours % 12) >= 12):
        amt_of_days += 1
    
    period = am_pm_flip[period] if amount_of_am_pm_flips % 2 == 1 else period

    new_time = str(new_hours) + ':' + str(new_minutes) + " " + period
    if(days):
        days = days.lower()
        index = int((week_index[days]) + amt_of_days) % 7
        n_day = week_array[index]
        new_time += ", " + n_day

    if(amt_of_days == 1):
        return new_time + " " + "(next day)"
    elif(amt_of_days > 1):
        return new_time + " (" + str(amt_of_days) + " days later)"

    return new_time