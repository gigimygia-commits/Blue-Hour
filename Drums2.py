# BLUE HOUR - SNARE
# this cell creates the backbeat of my R&B rhythm
# the snare helps make the beat easier to feel


# INTRO
# no snare at the start

rest(32)


# VERSE
for i in range(16):

    # rest() controls when the snare enters
    # I do not want every drum sound playing together

    rest(1)

    # note 2 is the snare sound
    # beats=0.5 keeps the snare short
    # velocity=48 keeps it soft

    playNote(2, beats=0.5, velocity=48)

    rest(1.5)

    # second snare is slightly stronger
    # small velocity changes make it feel more natural

    playNote(2, beats=0.5, velocity=52)

    rest(0.5)


# CHORUS
for i in range(16):

    rest(1)

    # louder snare during the chorus

    playNote(2, beats=0.5, velocity=58)

    rest(1)

    playNote(2, beats=0.5, velocity=60)

    rest(1)


# OUTRO
# drums disappear again

rest(32)
