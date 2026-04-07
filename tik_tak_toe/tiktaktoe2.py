# source: https://www.youtube.com/watch?v=nbRpDXV7QDM

import tkinter 


def set_tile(row, column):
    global current_player

    if (game_over):
        return

    if board[row][column]["text"] != "":
        return
    
    board[row][column]["text"] = current_player

    if current_player == player_o: #switch player
        current_player = player_x
    else:
        current_player = player_o
    
    label["text"] = current_player+"'s turn"

    check_winner()


def check_winner():
    global turns, game_over
    turns += 1


    # horizontally, check 3 rows
    for row in range(3):
        if (board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"]
            and board[row][0]["text"] != ""):
            label.config(text=board[row][0]["text"]+" is the winner!", foreground=color_yellow)
            for column in range(3):
                board[row][column].config(foreground=color_yellow, background=color_light_gray)
            game_over = True
            return
    
    #vertically, check 3 columns
    for column in range(3):
        if (board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"]
            and board[0][column]["text"] != ""):
            label.config(text=board[0][column]["text"]+" is the winner!", foreground=color_yellow)
            for row in range(3):
                board[row][column].config(foreground=color_yellow, background=color_light_gray)
            game_over = True
            return
    
    #diagonally
    if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"]
        and board[0][0]["text"] != ""):
        label.config(text=board[0][0]["text"]+" is the winner!", foreground=color_yellow)
        for i in range(3):
            board[i][i].config(foreground=color_yellow, background=color_light_gray)
        game_over = True
        return

    #anti-diagionally
    if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"]
        and board[0][2]["text"] != ""):
        label.config(text=board[0][2]["text"]+" is the winner!", foreground=color_yellow)
        board[0][2].config(foreground=color_yellow, background=color_light_gray)
        board[1][1].config(foreground=color_yellow, background=color_light_gray)
        board[2][0].config(foreground=color_yellow, background=color_light_gray)
        game_over = True
        return
    
    #tie
    if (turns == 9):
        game_over = True
        label.config(text="Tie!", foreground=color_yellow)

    
def new_game():
    global turns, game_over

    turns = 0
    game_over = False

    label.config(text=current_player + "'s turn", fg="white")

    for row in range(3):
        for column in range(3):
            board[row][column].config(text="", fg=color_blue, bg=color_gray)

# --- Game setup ---
player_x = "X"
player_o = "O"
current_player = player_x

board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

color_blue = '#4584B6'
color_yellow = "#FFDE57"
color_gray = "#343434"
color_light_gray = "#646464"

turns = 0 
game_over = False


# --- Window setup ---
window = tkinter.Tk()
window.title("Tic Tac Toe")
window.resizable(0, 0)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text=f"{current_player}'s turn", font=("Consolas", 20), bg=color_gray, fg="white")
label.grid(row=0, column=0, columnspan=3, sticky="WE")

for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(frame, text="", font=("Consolas", 50, "bold"), bg=color_gray, fg=color_blue, width=4, height=1,
                                            command=lambda row=row, column=column: set_tile(row, column))
        board[row][column].grid(row=row+1, column=column)

restart_button = tkinter.Button(frame, text="restart", font=("Consolas", 20), bg=color_gray, fg="white", command=new_game)
restart_button.grid(row=4, column=0, columnspan=3, sticky="we")
frame.pack()

# --- Center the window ---
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width / 2) - (window_width / 2))
window_y = int((screen_height / 2) - (window_height / 2))
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()
