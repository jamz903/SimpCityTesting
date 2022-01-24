def save_game(turn_num, building_pool, board):
    building_pool_str = ""
    for i in range(len(building_pool)):
        building_pool_str += building_pool[i]
        if i != (len(building_pool)-1):
            building_pool_str += ","
    with open('SimpCityBoard.csv', 'w') as file:
        file.write(str(turn_num))
        file.write("\n")
        file.write(building_pool_str)
        for line in board:
            file.write("\n")
            for x in line[:-1]:
                file.write(x + ",")
            file.write(line[-1])
    print("Game saved!")


#save_game(1,["PRK","SHP","HWY","FAC","HSE"],([["?","?","?","?"],["?","?","?","?"],["?","?","?","?"],["?","?","?","?"]]))
