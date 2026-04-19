default ava_affection = 0
default ava_trust = 0
default ava_awareness = 0
default ava_commitment = False

default kai_affection = 0
default kai_trust = 0
default kai_awareness = 0
default kai_commitment = False

default mira_affection = 0
default mira_trust = 0
default mira_awareness = 0
default mira_commitment = False

default lila_affection = 0
default lila_trust = 0
default lila_awareness = 0
default lila_commitment = False

default nia_affection = 0
default nia_trust = 0
default nia_awareness = 0
default nia_commitment = False

init python:
    def change_affection(girl, value):
        setattr(store, f"{girl}_affection",
            getattr(store, f"{girl}_affection") + value)
        if ava_affection >= 5 and ava_trust >= 3:
    $ ava_commitment = True
        if kai_affection >= 5 and kai_trust >= 3:
    $ kai_commitment = True
        if mira_affection >= 5 and mira_trust >= 3:
    $ mira_commitment = True
        if lila_affection >= 5 and lila_trust >= 3:
    $ lila_commitment = True
        if nia_affection >= 5 and nia_trust >= 3:
    $ nia_commitment = True
    def change_trust(girl, value):
        setattr(store, f"{girl}_trustin",
            getattr(store, f"{girl}_trustin") + value)
        if ava_trust >= 3 and ava_affection >= 5:
    $ ava_commitment = True
        if kai_trust >= 3 and kai_affection >= 5:
    $ kai_commitment = True
        if mira_trust >= 3 and mira_affection >= 5:
    $ mira_commitment = True
        if lila_trust >= 3 and lila_affection >= 5:
    $ lila_commitment = True
        if nia_trust >= 3 and nia_affection >= 5:
    $ nia_commitment = True

