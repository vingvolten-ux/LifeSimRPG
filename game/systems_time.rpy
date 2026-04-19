default day = 1
default month = 1
default year = 1
default time_of_day = "morning"

label advance_time:

    if time_of_day == "morning":
        $ time_of_day = "afternoon"

    elif time_of_day == "afternoon":
        $ time_of_day = "evening"

    else:
        $ time_of_day = "morning"
        $ day += 1
        call end_of_day_check

    return

label end_of_day_check:

    if day > 30:
        $ day = 1
        $ month += 1
        call monthly_update

    if month > 12:
        $ month = 1
        $ year += 1
        call yearly_update

    return