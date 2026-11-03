# BLUE HOUR - KICK
# this cell creates the low drum pulse of the song
# the kick is important for giving the track an R&B groove


# INTRO
# no kick for the first 32 beats
# I want the song to start softly before the full beat comes in

rest(32)


# VERSE
for i in range(16):

    # note 0 is the kick in my 808 Drumkit
    # the first kick is stronger

    playNote(0, beats=0.5, velocity=65)

    rest(1)

    # second kick is softer
    # changing velocity makes the beat feel less robotic

    playNote(0, beats=0.5, velocity=48)

    rest(0.5)

    # extra kick near the end
    # this makes the rhythm more syncopated
    # instead of having a very basic straight beat

    playNote(0, beats=0.5, velocity=58)

    rest(1)


# CHORUS
for i in range(16):

    # stronger kick pattern makes the chorus feel bigger

    playNote(0, beats=0.5, velocity=70)

    rest(0.5)

    playNote(0, beats=0.5, velocity=52)

    rest(1)

    playNote(0, beats=0.5, velocity=64)

    rest(1)


# OUTRO
# I remove the kick completely
# this brings the calm feeling back

rest(32)

