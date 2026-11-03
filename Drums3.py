# New TunePad cell
# BLUE HOUR - HI HAT
# this cell adds movement to the R&B beat

# I use the 808 Drumkit because it fits the modern R&B sound
# note 4 is the main hi hat sound in this kit

# repeat the hi hat pattern
for i in range(16):

    # I change the velocity so the hi hats do not all sound the same
    # this makes the rhythm feel less robotic

    playNote(4, beats=0.25, velocity=34)
    rest(0.25)

    playNote(4, beats=0.25, velocity=24)
    rest(0.25)

    playNote(4, beats=0.25, velocity=32)
    rest(0.25)

    playNote(4, beats=0.25, velocity=22)
    rest(0.25)

    # I use note 5 here for a small variation
    # this makes the pattern more interesting
    playNote(5, beats=0.25, velocity=30)
    rest(0.25)

    playNote(4, beats=0.25, velocity=24)
    rest(0.25)

    playNote(4, beats=0.25, velocity=32)
    rest(0.25)

    playNote(5, beats=0.25, velocity=26)
    rest(0.25)


