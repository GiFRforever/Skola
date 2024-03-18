import mido
import matplotlib.pyplot as plt


def read_midi(file_path):
    # C5 is the 72nd note in the MIDI standard
    # 240 is quarter note at 120 bpm
    notes: list[tuple[int, int, int]] = []
    # Open the MIDI file
    with mido.MidiFile(file_path) as midi_file:
        # Iterate over each track in the MIDI file
        for i, track in enumerate(midi_file.tracks):
            # print(f"Track {i}:")

            # Initialize variables to keep track of note start times
            current_time = 0
            note_start_times = {}

            # Iterate over each message in the track
            for msg in track:
                # Update current time based on the message time
                current_time += msg.time

                # If it's a note-on message, store the note and its start time
                if msg.type == "note_on" and msg.velocity != 0:
                    note_start_times[msg.note] = current_time

                # If it's a note-off message, calculate the duration and print the note
                elif msg.type == "note_off" or (
                    msg.type == "note_on" and msg.velocity == 0
                ):
                    note = msg.note
                    start_time = note_start_times.pop(note, None)
                    if start_time is not None:
                        # duration = current_time - start_time
                        # print(f"Note {note} at time {start_time}, duration {duration}")
                        plt.plot([start_time, current_time], [note, note], "r-")
                        notes.append((start_time, current_time, note))
    return notes


# Provide the path to your MIDI file
midi_file_path = r"moje\545.mid"
notes: list[tuple[int, int, int]] = read_midi(midi_file_path)
# plt.show()

# change notes so only one note is played at a time, the highest note is played
notes.sort(key=lambda x: x[0])
new_notes = []
new_notes.append(notes.pop(0))
for note in notes:
    if note[0] < new_notes[-1][1]:
        if note[2] > new_notes[-1][2]:
            new_notes[-1] = (new_notes[-1][0], note[0], new_notes[-1][2])
            new_notes.append(note)
    else:
        new_notes.append((new_notes[-1][1], note[0], 0))
        new_notes.append(note)

notes = new_notes

for note in notes:
    plt.plot([note[0], note[1]], [note[2], note[2]], "k-")

plt.show()
