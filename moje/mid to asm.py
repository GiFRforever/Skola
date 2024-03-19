import mido

# from time import sleep

# import matplotlib.pyplot as plt
uspt: float = 1041.7


def read_midi(file_path) -> list[tuple[int, int, int]]:
    # C5 is the 72nd note in the MIDI standard
    # 240 is quarter note at 120 bpm
    notes: list[tuple[int, int, int]] = []
    # Open the MIDI file
    global uspt

    with mido.MidiFile(file_path) as midi_file:
        # Iterate over each track in the MIDI file
        tpb = midi_file.ticks_per_beat
        print(f"Ticks per beat: {tpb}")
        for i, track in enumerate(midi_file.tracks):
            # print(f"Track {i}:")
            # Initialize variables to keep track of note start times
            current_time = 0
            note_start_times = {}

            # Iterate over each message in the track
            for msg in track:
                # Update current time based on the message time
                current_time += msg.time

                if msg.type == "set_tempo":
                    tempo = msg.tempo
                    print(f"Tempo: {tempo}")

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
                        # plt.plot([start_time, current_time], [note, note], "r-")
                        notes.append((start_time, current_time, note))
    uspb = tempo / tpb
    print(f"Microseconds per beat: {uspb}")
    return notes


# Provide the path to your MIDI file
midi_file_path = r"moje\545.mid"
notes: list[tuple[int, int, int]] = read_midi(midi_file_path)
# plt.ion()
# plt.show()

# change notes so only one note is played at a time, the highest note is played
notes.sort(key=lambda x: x[0])
new_notes = []
new_notes.append(notes.pop(0))

for note in notes:
    while True:
        if (
            note[0] < new_notes[-1][1]
        ):  # if the note starts before the previous note ends
            if (
                note[0] < new_notes[-1][0] and note[2] > new_notes[-1][2]
            ):  # if the note starts before the previous note starts and is higher than the previous note
                new_notes.pop()
                continue
            else:
                if (
                    note[2] > new_notes[-1][2]
                ):  # if the note is higher than the previous note
                    new_notes[-1] = (
                        new_notes[-1][0],
                        note[0],
                        new_notes[-1][2],
                    )  # change the end of the previous note to the start of the current note
                    new_notes.append(note)  # add the current note
                elif (
                    note[1] > new_notes[-1][1]
                ):  # if the note is lower than the previous note and ends after the previous note
                    new_notes.append(
                        (new_notes[-1][1], note[1], note[2])
                    )  # add the part of the current note that is after the previous note
        else:
            new_notes.append(
                (new_notes[-1][1], note[0], 0)
            )  # add silence between the previous note and the current note
            new_notes.append(note)

        break


notes = new_notes


# for note in notes:
#     plt.plot([note[0], note[1]], [note[2], note[2]], "k-")
# plt.show()

# delete notes that are too short
# notes = [note for note in notes if note[1] - note[0] > 10]

# round the start and end times to the nearest 10
# notes = [
#     (one, two, note[2])
#     for note in notes
#     if (two := round(note[1], -1), note[2]) != (one := round(note[0], -1))
# ]

# min_note = min(notes, key=lambda x: x[2] if x[2] else 255)[2]
# max_note = max(notes, key=lambda x: x[2])[2]
# min_time = (n := min(notes, key=lambda x: x[1] - x[0]))[1] - n[0]
# max_time = (n := max(notes, key=lambda x: x[1] - x[0]))[1] - n[0]
# print(f"{min_note=}, {max_note=}, {min_time=}, {max_time=}")

# for note in notes:
#     print(f"Start: {note[0]:>5}, End: {note[1]:>5}, Note: {note[2]:>3}")
#     sleep(0.5)


# notes_dt: list[tuple[int, float]] = [
#     ((note[1] - note[0]), halftimes[note[2]]) for note in notes
# ]

casy: dict[int, tuple[int, int, int]] = {}
with open("moje\\casy.txt", "r") as f:
    for line in f.readlines():
        try:
            note, r1, r0, t = line.split()
            casy[int(note)] = (int(r1), int(r0), int(t))
        except Exception as e:
            print(e)

# noty = []
# for note in notes:
#     cas: tuple[int, int, int] = casy[note[2]]
#     # beats: int = note[1] - note[0]
#     # us: float = beats * uspt
#     # count: int = int(us / cas[2])
#     count: int = int((note[1] - note[0]) * uspt / cas[2])
#     if count > 0:
#         while count > 255:
#             noty.append((cas[0], cas[1], 255))
#             count -= 255
#         noty.append((cas[0], cas[1], count))

# with open("moje\\out.asm", "w") as f:
#     f.write("HL:")
#     for i, note in enumerate(noty):
#         f.write(
#             f"""
#         MOV R2,#{note[2]}
# {f"N{i}:":<8}MOV R1,#{note[0]}
#         MOV R0,#{note[1]}
#         SETB P0.7
#         CALL WAIT
#         MOV R1,#{note[0]}
#         MOV R0,#{note[1]}
#         CALL WAIT
#         CLR P0.7
#         DJNZ R2, {f"N{i}"}
# """
#         )
#     f.write(
#         """
# WAIT:   DJNZ R0,WAIT
#         CJNE R1,#0,WAIT1
#         RET
# WAIT1:  MOV R0,#255
# WAIT2:  DJNZ R0,WAIT2
#         DJNZ R1,WAIT1
#         RET
# END
# """
#     )

noty: list[tuple[int, int]] = []
for note in notes:
    cas: tuple[int, int, int] = casy[note[2]]
    count: int = int((note[1] - note[0]) * uspt / cas[2])
    if count > 0:
        while count > 255:
            noty.append((note[2], 255))
            count -= 255
        noty.append((note[2], count))
noty.append((0, 255))  # silence at the end

with open("moje\\out.asm", "w") as f:
    f.write("HL:")
    for i, note in enumerate(noty):
        f.write(
            f"""
        MOV R2,#{note[1]}
{f"T{i}:":<8}CALL N{note[0]}
        DJNZ R2, T{i}
"""
        )

    f.write(
        """
        JMP HL
"""
    )

    casy.pop(0)
    f.write(
        f"""
N0:     MOV R1,#1
	MOV R0,#235
	CALL WAIT
	MOV R1,#1
	MOV R0,#235
	CALL WAIT
	RET
"""
    )

    for n, c in casy.items():
        f.write(
            f"""
{f"N{n}:":<8}MOV R1,#{c[0]}
	MOV R0,#{c[1]}
	SETB P0.7
	CALL WAIT
	MOV R1,#{c[0]}
	MOV R0,#{c[1]}
	CALL WAIT
	CLR P0.7
	RET
"""
        )

    f.write(
        """
WAIT:   DJNZ R0,WAIT
        CJNE R1,#0,WAIT1
        RET
WAIT1:  MOV R0,#255
WAIT2:  DJNZ R0,WAIT2
        DJNZ R1,WAIT1
        RET
END
"""
    )
