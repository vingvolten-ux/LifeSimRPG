default money = 500
default health = 10
default energy = 10
default hygiene = 10

default social = 0
default confidence = 0
default kindness = 0

default academics = 0
default creativity = 0

init python:
    def change_stat(stat, value):
        setattr(store, stat, getattr(store, stat) + value)
$ money += 100