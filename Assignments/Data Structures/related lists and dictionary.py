player_1 = ["Lebron James", "Position: Small Forward"]
player_2 = ["Lonzo Ball,", "Position: Point Guard"]
player_1 = player_1.append(player_2)
print (player_1)







players = {"LeBron James,": "Position: Small Forward","Lonzo Ball,": "Position: Point Guard","Rajon Rondo,": "Position: Point Guard",
            "Brandon Ingram,": "Position: Small Forward","Kyle Kuzma,": "Position: Small Forward","Javale McGee,": "Position: Center",
            "Josh Hart,": "Position: Small Forward","Lance Stephenson,": "Position: Small Forward","Jonathan Williams,": "Position: Power Forward",
            "Tyson Chandler,": "Position: Center","Michael Beasley,": "Position: Small Forward","Kentavious Caldwell-Pope,": "Position: Small Forward",
            "Sviatoslav Mykhailiuk,": "Position: Shooting Guard", "Moritz Wagner,": "Position: Point Forward","Isaac Bonga,": "Position: Small Forward",
            "Ivica Zubac,": "Position: Center", "Alex Caruso,": "Position: Shooting Guard"}



for key, value in players.items():
    print(key, value)

