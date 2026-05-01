def computePolkadotScore(ascii_art: str) -> int:
    lines = ascii_art.split("\n")

    O_positions = []
    pupil_positions = []
    lips_start = None
    lips_end = None

    for i, line in enumerate(lines):
        for j, ch in enumerate(line):
            if ch == "O":
                O_positions.append(j)

            if ch == "•":
                pupil_positions.append(j)

        # first valid face line with pupils defines lips range
        if "•" in line and line.count("•") >= 2 and lips_start is None:
            lips_start = line.find("•")
            lips_end = line.rfind("•")

    pupil_count = 2

    inside = 0
    outside = 0

    for x in O_positions:
        if lips_start <= x <= lips_end:
            inside += 1
        else:
            outside += 1

    return outside + inside * pupil_count