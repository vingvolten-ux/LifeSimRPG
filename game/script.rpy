# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    call intro_scene

    while True:

        call morning_event
        call afternoon_event
        call evening_event

        call advance_time

        call check_month_events
    return
