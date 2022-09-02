# Dikatso Moshweunyane
# 25 May 2020
# OXO Game Client

from GameClient import *
import time

class OXOTextClient(GameClient):

    def __init__(self):
        GameClient.__init__(self)
        self.board = [' '] * BOARD_SIZE
        self.shape = None
        
    def clear_board(self):
        self.board = [' '] * BOARD_SIZE
        
    def input_server(self):
        return input('enter server:')
     
    def input_move(self):
        return input('enter move(0-8):')
     
    def input_play_again(self):
        return input('play again(y/n):')

    def display_board(self):
        _1st = "0"
        _2nd = "1"
        _3rd = "2"
        _4th = "3"
        _5th = "4"
        _6th = "5"
        _7th = "6"
        _8th = "7"
        _9th = "8"
        if self.board[0] == " " and self.board[1] == " " and self.board[2] == " " and self.board[3] == " " and self.board[4] == " " and self.board[5] == " " and self.board[6] == " " and self.board[7] == " " and self.board[8] == " ":  # Checks if there is anything on the board
            print("+~~~~~+~~~~~+~~~~~+")                                                        # Prints out the board layout with numbering guidlines.
            print("|"+ "  "+ _1st + "  "+"|"+ "  "+ _2nd + "  "+"|"+ "  "+ _3rd + "  "+"|")
            print("+~~~~~+~~~~~+~~~~~+")
            print("|"+ "  "+ _4th + "  "+"|"+ "  "+ _5th + "  "+"|"+ "  "+ _6th + "  "+"|")
            print("+~~~~~+~~~~~+~~~~~+")
            print("|"+ "  "+ _7th + "  "+"|"+ "  "+ _8th + "  "+"|"+ "  "+ _9th + "  "+"|")
            print("+~~~~~+~~~~~+~~~~~+")
        else:
            _1st = self.board[int(_1st)]
            _2nd = self.board[int(_2nd)]
            _3rd = self.board[int(_3rd)]
            _4th = self.board[int(_4th)]
            _5th = self.board[int(_5th)]
            _6th = self.board[int(_6th)]
            _7th = self.board[int(_7th)]
            _8th = self.board[int(_8th)]
            _9th = self.board[int(_9th)]
            print("+~~~~~+~~~~~+~~~~~+")                                                    # Prints out the board layout with characters in place.
            print("|"+ "  "+ _1st + "  "+"|"+ "  "+ _2nd + "  "+"|"+ "  "+ _3rd + "  "+"|")
            print("+~~~~~+~~~~~+~~~~~+")
            print("|"+ "  "+ _4th + "  "+"|"+ "  "+ _5th + "  "+"|"+ "  "+ _6th + "  "+"|")
            print("+~~~~~+~~~~~+~~~~~+")
            print("|"+ "  "+ _7th + "  "+"|"+ "  "+ _8th + "  "+"|"+ "  "+ _9th + "  "+"|")
            print("+~~~~~+~~~~~+~~~~~+")
    
    
    def handle_message(self,msg):
        msg_strip = msg[:msg.find(",")]           # Strips the string to get the message before the comma
        if msg_strip == "new game":
            character = msg[-1]                   # Gets the characterer from the message
            print("New game,you'll be playing with the " +character+ " character.")
            self.display_board()                  # Displays the board to the players
        elif msg == "your move":
            print("It's your turn to move....")
            user_input_move = self.input_move()   # Gets input from the user
            self.send_message(user_input_move)    # Sends the input from the user to the server
            
        elif msg == "opponents move":
            print("It's your opponents turn to move....")
            
        elif msg_strip == "valid move":
            shape = msg[-3]                       # Gets the character from the message
            self.board[int(msg[-1])] = shape      # Sets the character to the given position on the board
            self.display_board()
            
        elif msg == "invalid move":
            print("Invalid move")
            
        elif  msg_strip == "game over":
            winning_character = msg[-1]           # Gets the character from the message
            if winning_character == "X" or winning_character == "O":
                print("Game over! The winner is " +winning_character+ "!")
            elif winning_character == "T":
                print(" Game over! There's no winner, it's a tie.")
                
        elif msg == "play again":
            user_reply = self.input_play_again()  # Asks the user if they want to play again
            self.send_message(user_reply)         # Sends the users input to the server
            if user_reply =="y":
                self.clear_board()                # Clears the board
            time.sleep(3)                         # Game pauses for 3 seconds
            
        elif msg == "exit game":
            print("Someone decided to exit the game.Game Over")
            
    def play_loop(self):
        while True:
            msg = self.receive_message()
            if len(msg): self.handle_message(msg)
            else: break
            
def main():
    otc = OXOTextClient()
    while True:
        try:
            otc.connect_to_server(otc.input_server())
            break
        except:
            print('Error connecting to server!')
    otc.play_loop()
    input('Press click to exit.')
        
main()


#for self.column in range(3):
            ## iterate at a range of 3 to allow 3 rows
            #for self.row in range(3):
                ## set board button
                #self.board_play_button = QToolButton()
                ## Fixed size of the button to 100 height and 100 widgth
                #self.board_play_button.setFixedSize(100, 100)
                ## Fixed size of the icon in the button to 150 height and 150 widgth
                #self.board_play_button.setIconSize(QSize(150, 150))
                ## put icon to the button
                ##self.board_play_button.setIcon(self.lst_choice)
                ## set text to Fasle to allow icon to be inserted to the button 
                #self.board_play_button.setText("")
                ## track each button by giving it, its object name 
                #self.board_play_button.setObjectName(str(self.counter))
                #self.board.addWidget(self.board_play_button, self.column, self.row)
                ## increment counter
                #self.counter += 1
        ## create widget for the board game
        #self.board_widget = QWidget()
        #self.board_widget.setLayout(self.board)
        ## get all the buttons in the board widget
        #self.allButtons = self.board_widget.findChildren(QToolButton)
        ## iterate each button
        #for button in self.allButtons:
            ## connect each button to report feedback when pressed
            #button.clicked.connect(self.buttons)
