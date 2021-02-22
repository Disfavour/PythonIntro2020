def turtle(coord, direction):
    val = yield coord
    while val:
        if val == "f":
            if direction == 0:
                coord = [coord[0] + 1, coord[1]]
            elif direction == 1:
                coord = [coord[0], coord[1] + 1]
            elif direction == 2:
                coord = [coord[0] - 1, coord[1]]
            else:
                coord = [coord[0], coord[1] - 1]

        elif val == "l":
            direction = (direction + 1) % 4

        elif val == "r":
            direction = (direction + 3) % 4

        val = yield coord
