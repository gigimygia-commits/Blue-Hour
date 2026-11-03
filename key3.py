# New TunePad cell
from tunepad.constants import *

# BLUE HOUR - AD LIB
# this is a second small melody
# it answers the main melody instead of playing all the time

# I use Musicbox because it sounds different from the Crystal Organ
# this helps the two melody layers stay separate


# INTRO
# no ad lib during the intro
# I want the song to slowly build

rest(32)


# VERSE
for i in range(4):

    # wait first
    # the ad lib only fills empty spaces

    rest(4)

    # small high note

    playNote(Eb5, beats=0.5, velocity=30)

    rest(0.5)

    # second response note

    playNote(C5, beats=0.5, velocity=28)

    # longer ending note

    playNote(Bb4, beats=1, velocity=32)

    # lots of silence
    # I do this because too many notes would make the R&B track crowded

    rest(9.5)


# CHORUS
for i in range(4):

    # the ad lib becomes slightly more active in the chorus

    rest(2)

    playNote(Eb5, beats=0.5, velocity=34)

    rest(0.5)

    playNote(C5, beats=0.5, velocity=32)

    playNote(Bb4, beats=0.5, velocity=30)

    rest(4)

    # higher response note

    playNote(G5, beats=0.5, velocity=36)

    playNote(F5, beats=0.5, velocity=34)

    playNote(Eb5, beats=1, velocity=32)

    rest(6)


# OUTRO
# only a few quiet notes at the end

rest(16)

playNote(Eb5, beats=1, velocity=26)

rest(3)

playNote(C5, beats=1, velocity=24)

rest(3)

playNote(Bb4, beats=2, velocity=22)

rest(6)


