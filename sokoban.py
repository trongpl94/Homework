map = {'sizex':9,
       'sizey':9}

player = {'x': 1,
          'y': 1}
boxes = [
    {"x":3, "y": 3},
    {"x":5, "y": 6},
    {"x":2, "y": 4},
]
destiny = [
    {'x':2, "y":4},
    {'x':5, "y":2},
    {'x':4, "y":2}
]
waters = [
     {"x":3, "y":1},
    {"x":2, "y":2}
]
while True:
     dx = 0
     dy = 0
     cou = 1
     for y in range(map['sizex']+1):
        for x in range(map['sizey']+1):
            box_is_here = False
            for b in boxes:
                if b['x'] == x and b['y'] == y:
                    box_is_here = True
                    break
            destiny_here = False
            for d in destiny:
                if d['x'] == x and d['y'] == y:
                    destiny_here = True
                    break
            water_here = False
            for w in waters:
                if w['x'] == x and d['y'] == y:
                    water_here = True
                    break
            player_here = False
            if x == player['x'] and y == player['y']:
                print('P ', end="")
                player_here = True
            elif x == 0 or y == 0 or x == map['sizex'] or y == map['sizey']:
                print("! ",end="")
            elif box_is_here:
                print("B ", end="")
            elif destiny_here:
                print("D ", end="")
            elif water_here:
                print("~ ",end="")
            else:
                print('_ ',end="")
        print()
     win = True
     for box in boxes:
         if box not in destiny:
             win = False
     if win:
         print("U win!!!")
         break
     move = input("Your move?").upper()
     if move =="W":
        dy -= 1
        print("Up")
     elif move =="S":
        print("Down")
        dy += 1
     elif move =="A":
        dx -= 1
        print("Left")
     elif move =="D":
        dx += 1
        print("Right")
     else:
        print("WTF")
     if 0 <= player['x'] + dx < map['sizex']+1 \
             and 0 <= player['y'] + dy < map['sizey']+1:
         player['x'] += dx
         player['y'] += dy
     for k in boxes:
          if 0 <= k['x'] + dx < map['sizex']+1 \
                and 0 <= k['y'] + dy < map['sizey']+1:
              if player['x'] == k['x'] and player['y'] == k['y']:
                  k['x'] += dx
                  k['y'] += dy
                  for w1 in waters:
                    if (boxes[1]["x"] == boxes[2]["x"] and boxes[1]["y"] == boxes[2]["y"]) or \
                     (boxes[2]["x"] == boxes[0]["x"] and boxes[2]["y"] == boxes[0]["y"]) or \
                     (boxes[0]["x"] == boxes[1]["x"] and boxes[0]["y"] == boxes[1]["y"]) or \
                          (k["x"] == w1["x"] and k["y"] == w1["y"]):
                            k["x"] -= dx
                            k["y"] -= dy
                            player["x"] -= dx
                            player["y"] -= dy

