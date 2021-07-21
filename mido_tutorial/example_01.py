from mido import MidiFile

mid = MidiFile('../examples/midifiles/VampireKillerCV1.mid', clip=True)

if __name__ == "__main__":
    print(mid)

