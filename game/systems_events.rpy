label event_first_job:

    "You receive a part-time job offer."

    menu:
        "Accept":
            $ money += 100
            $ energy -= 2

        "Decline":
            $ academics += 1

    return

label check_month_events:

    if month == 2:
        call event_first_job

    if month == 6:
        call event_first_jealousy

    if month == 12:
        call end_of_act_1

    return
