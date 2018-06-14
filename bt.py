all_map = [{
    "size_x": 7,
    "size_y": 7
},
    {"size_x": 8,
     "size_y": 8
     },
    {"size_x": 9,
     "size_y": 9
     }
]

all_player = [
    {
        "x": 1,
        "y": 1
    },
    {
        "x": 1,
        "y": 1
    },
    {
        "x": 1,
        "y": 1
    }
]

all_boxes = [
    [
        {"x": 2, "y": 2},
        {"x": 3, "y": 3},
        {"x": 4, "y": 4}
    ],
    [
        {"x": 2, "y": 4},
        {"x": 4, "y": 3},
        {"x": 6, "y": 5}
    ],
    [
        {"x": 2, "y": 3},
        {"x": 2, "y": 2},
        {"x": 3, "y": 2}
    ]
]

all_destination = [
    [
        {"x": 3, "y": 2},
        {"x": 4, "y": 3},
        {"x": 5, "y": 4}
    ],
    [
        {"x": 6, "y": 6},
        {"x": 5, "y": 6},
        {"x": 4, "y": 6}
    ],
    [
        {"x": 7, "y": 1},
        {"x": 1, "y": 7},
        {"x": 7, "y": 7}
    ],
]

all_obstacle = [
    [
        {"x": 5, "y": 2},
        {"x": 2, "y": 4}
    ],
    [
        {"x": 4, "y": 4},
        {"x": 3, "y": 2},
        {"x": 2, "y": 5}
    ],
    [
        {"x": 6, "y": 1},
        {"x": 6, "y": 3},
        {"x": 6, "y": 4},
        {"x": 6, "y": 6},
        {"x": 4, "y": 6},
        {"x": 3, "y": 6},
        {"x": 1, "y": 6}
    ]
]

for i in range(len(all_map)):
    map = all_map[i]
    player = all_player[i]
    boxes = all_boxes[i]
    destination = all_destination[i]
    obstacle = all_obstacle[i]

    # inmapbandau
    print('''INSTRUCTION:
    1. Enter WASD to move
    2. Enter "UNDO" to rewind 1 step
    3. Enter "QUIT" to quit the game
    ''')
    print("LEVEL", i + 1)
    for y in range(map["size_y"]):
        for x in range(map["size_x"]):
            player_is_here = False
            box_is_here = False
            desti_is_here = False
            wall_is_here = False
            obstacle_is_here = False
            for box in boxes:
                if box["x"] == x and box["y"] == y:
                    box_is_here = True
                    break
            for des in destination:
                if des["x"] == x and des["y"] == y:
                    desti_is_here = True
                    break
            for obs in obstacle:
                if obs["x"] == x and obs["y"] == y:
                    obstacle_is_here = True
                    break
            if y == player["y"] and x == player["x"]:
                player_is_here = True
            if y == 0 or x == 0 or y == map["size_y"] or x == map["size_x"]:
                wall_is_here = True

            if player_is_here:
                print("P ", end="")
            elif box_is_here:
                print("B ", end="")
            elif desti_is_here:
                print("X ", end="")
            elif obstacle_is_here:
                print("O ", end="")
            elif wall_is_here:
                print("I ", end="")
            else:
                print("- ", end="")
        print()

    dx = 0
    dy = 0
    while True:
        # dichuyen
        action = input("Your move: ").upper()
        undo = False
        if action == "W":
            dx = 0
            dy = -1
        elif action == "S":
            dx = 0
            dy = 1
        elif action == "A":
            dx = -1
            dy = 0
        elif action == "D":
            dx = 1
            dy = 0
        elif action == "UNDO":
            dx = -dx
            dy = -dy
            undo = True
        elif action == "QUIT":
            break
        else:
            print("Nhap sai roi!")

        for obs in obstacle:
            if player["x"] + dx == obs["x"] and player["y"] + dy == obs["y"]:
                player["x"] -= dx
                player["y"] -= dy
                break

        if 1 <= player["x"] + dx < map["size_x"] - 1 and 1 <= player["y"] + dy < map["size_y"] - 1:
            player["x"] += dx
            player["y"] += dy

        for box in boxes:
            if box["x"] == player["x"] - 2 * dx and box["y"] == player["y"] - 2 * dy:
                if undo:
                    box["x"] += dx
                    box["y"] += dy
            if box["x"] == player["x"] and box["y"] == player["y"]:
                if 1 <= box["x"] + dx < map["size_x"] - 1 and 1 <= box["y"] + dy < map["size_y"] - 1:
                    box["x"] += dx
                    box["y"] += dy
                    for obs in obstacle:
                        if (boxes[1]["x"] == boxes[2]["x"] and boxes[1]["y"] == boxes[2]["y"]) or \
                                (boxes[2]["x"] == boxes[0]["x"] and boxes[2]["y"] == boxes[0]["y"]) or \
                                (boxes[0]["x"] == boxes[1]["x"] and boxes[0]["y"] == boxes[1]["y"]) or \
                                (box["x"] == obs["x"] and box["y"] == obs["y"]):
                            box["x"] -= dx
                            box["y"] -= dy
                            player["x"] -= dx
                            player["y"] -= dy
                else:
                    player["x"] -= dx
                    player["y"] -= dy

        # inmap
        for y in range(map["size_y"]):
            for x in range(map["size_x"]):
                player_is_here = False
                box_is_here = False
                desti_is_here = False
                wall_is_here = False
                obstacle_is_here = False
                for box in boxes:
                    if box["x"] == x and box["y"] == y:
                        box_is_here = True
                        break
                for des in destination:
                    if des["x"] == x and des["y"] == y:
                        desti_is_here = True
                        break
                for obs in obstacle:
                    if obs["x"] == x and obs["y"] == y:
                        obstacle_is_here = True
                        break
                if y == player["y"] and x == player["x"]:
                    player_is_here = True
                if y == 0 or x == 0 or y == map["size_y"] - 1 or x == map["size_x"] - 1:
                    wall_is_here = True

                if player_is_here:
                    print("P ", end="")
                elif box_is_here:
                    print("B ", end="")
                elif desti_is_here:
                    print("X ", end="")
                elif obstacle_is_here:
                    print("O ", end="")
                elif wall_is_here:
                    print("I ", end="")
                else:
                    print("- ", end="")
            print()

        # checkkqua
        x = 0
        for des in destination:
            for box in boxes:
                if box["x"] == des["x"] and box["y"] == des["y"]:
                    x += 1
                    break
        if x == 3:
            print()
            print("YOU WON !!!")
            break

    while True:
        stop = False
        decision = input("Continue? ").upper()
        if decision == "NO":
            stop = True
            break
        elif decision == "YES":
            print()
            break
        else:
            print("Nhap sai roi")
            print()

    if stop:
        break