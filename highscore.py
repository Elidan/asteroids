def read_highscores():
    filename = "resources/highscores.txt"
    highscores = []
    try:
        with open(filename, "r") as file:
            for line in file:
                # Strip whitespace and split at the colon
                parts = line.strip().split(": ")
                if len(parts) == 2:  # Make sure the line has the expected format
                    player_name = parts[0]
                    try:
                        score = int(parts[1])  # Convert the score to an integer
                        highscores.append((player_name, score))
                    except ValueError:
                        # Handle the case where the score isn't a valid integer
                        print(f"Invalid score format in line: {line}")
    except FileNotFoundError:
        # Handle the case where the file doesn't exist yet
        print(f"Highscore file {filename} not found.")
    
    # Sort highscores by score (highest first)
    highscores.sort(key=lambda x: x[1], reverse=True)
    return highscores

def print_highscores_to_console():
        print("---- Highscores ----")
        for name, score in read_highscores():
            print(f"{name}: {score}")
        print("--------------------")

def is_top10(new_score):
    highscores = read_highscores()
    for name, score in highscores:
        if score < new_score or len(highscores) < 10:
            return True
    return False

def add_new_score(player_name, new_score):
    highscores = read_highscores()
    insert_position = 0
    for i, (_, score) in enumerate(highscores):
        if new_score > score:
            insert_position = i
            break
        else:
            insert_position = i + 1
            
    highscores.insert(insert_position, (player_name, new_score))        
    
    max_scores = 10
    if len(highscores) > max_scores:
        highscores = highscores[:max_scores]
    
    with open("resources/highscores.txt", "w") as file:
        for name, score in highscores:
            file.write(f"{name}: {score}\n")