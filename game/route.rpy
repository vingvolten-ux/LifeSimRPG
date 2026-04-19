label ava_route:

    if ava_trust >= 10:
        "Ava smiles softly..."

    else:
        "Ava avoids your gaze..."

label kai_route:

    if kai_trust >= 10:
        "Kai seems more open around you..."

    else:
        "Kai keeps his distance from you..."

label mira_route:

    if mira_trust >= 10:
        "Mira shares her thoughts with you..."

    else:
        "Mia is quiet and reserved around you..."

label lila_route:

    if lila_trust >= 10:
        "Lila laughs and jokes with you..."

    else:
        "Lila seems uninterested in talking to you..."

label nia_route:
    if nia_trust >= 10:
        "Nia confides in you about her feelings..."

    else:
        "Nia is distant and unresponsive to you..."

label spend_time_with_ava:

    $ change_affection("ava", 1)

    $ trigger_jealousy("ava")

label spend_time_with_kai:
    $ change_affection("kai", 1)
    $ trigger_jealousy("kai")

label spend_time_with_mira:
    $ change_affection("mira", 1)
    $ trigger_jealousy("mira")

label spend_time_with_lila:
    $ change_affection("lila", 1)
    $ trigger_jealousy("lila")

label spend_time_with_nia:
    $ change_affection("nia", 1)
    $ trigger_jealousy("nia")

    return

if ava_commitment and ava_trust > 10:
    jump ava_good_ending

elif money < 200:
    jump bad_financial_ending

elif len(active_relationships) == 0:
    jump lonely_ending
else:
    jump neutral_ending

if kai_commitment and kai_trust > 10:
    jump kai_good_ending

elif money < 200:
    jump bad_financial_ending

elif len(active_relationships) == 0:
    jump lonely_ending
else:
    jump neutral_ending

if mira_commitment and mira_trust > 10:
    jump mira_good_ending

elif money < 200:
    jump bad_financial_ending

elif len(active_relationships) == 0:
    jump lonely_ending
else:
    jump neutral_ending 

if lila_commitment and lila_trust > 10:
    jump lila_good_ending

elif money < 200:
    jump bad_financial_ending

elif len(active_relationships) == 0:
    jump lonely_ending
else:
    jump neutral_ending

if nia_commitment and nia_trust > 10:
    jump nia_good_ending

elif money < 200:
    jump bad_financial_ending

elif len(active_relationships) == 0:
    jump lonely_ending
else:
    jump neutral_ending
