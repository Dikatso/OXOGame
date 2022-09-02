# Dikatso Moshweunyane
# 25 May 2020
# OXO GUI

import sys
from PyQt5.QtWidgets import* # imports PyQt5 modules
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from GameClient import*
import time
from PyQt5 import QtMultimedia as Media


class LoopThread(QThread):
    messageSignal = pyqtSignal(str)
    
    def __init__(self): 
        QThread.__init__(self)
        
    def run(self):
        while True:
            msg = abs_widget.receive_message()
            if len(msg): self.messageSignal.emit(msg)

class OXO_GUI(QWidget,GameClient):
    def __init__(self,parent = None):
        GameClient.__init__(self)
        QWidget.__init__(self, parent)
        self.setGeometry(250,100,600,300)
        self.setWindowTitle("OXO GAME")
        self.setWindowIcon(QIcon("tic-tac-toe"))
        
        
        # Click and gameover sound enhancements(NerdZone)
        self.click = QUrl.fromLocalFile("click.mp3")           
        self.click_content = Media.QMediaContent(self.click)
        self.click_player = Media.QMediaPlayer()
        self.click_player.setMedia(self.click_content)
        
        self.gameover = QUrl.fromLocalFile("gameover.mp3")      
        self.gameover_content = Media.QMediaContent(self.gameover)
        self.gameover_player = Media.QMediaPlayer()
        self.gameover_player.setMedia(self.gameover_content)        
        
        # Create QLabels
        self.heading_label = QLabel("~~~~~ O X O GAME ~~~~~")
        self.heading_label.setFont(QFont("Courier New Bold Italic",20,10))
        self.heading_label.setAlignment(Qt.AlignHCenter)
        
        self.grid_heading_label = QLabel("THE GAME")
        self.grid_heading_label.setAlignment(Qt.AlignHCenter)
        self.grid_heading_label.setFont(QFont("Courier New Bold",15,7))
        
        self.server_label = QLabel("SERVER :")
        self.server_label.setFont(QFont("Courier New Bold",13,5))
        
        self.shape_label = QLabel("YOUR SHAPE        ----------------------------->  ")
        self.shape_label.setAlignment(Qt.AlignVCenter)
        self.shape_label.setFont(QFont("Courier New Bold",13,5))
        
        self.server_messages_label = QLabel("SERVER MESSAGES ")
        self.server_messages_label.setAlignment(Qt.AlignHCenter)
        self.server_messages_label.setFont(QFont("Courier New Bold",13,5))
        
        
        #Create QLine Edit Box
        self.server_input = QLineEdit()
        self.server_input.setPlaceholderText("Enter Server Address ")                  # Nerd Zone Enhancement
        self.server_input.setToolTip("Example:'localhost' or '192.168.1.125'")            # Nerd Zone Enhancement
        
        
        # Create Pushbuttons and ToolButton
        self.connect_button = QPushButton("Connect")
        self.quit_button = QPushButton("Quit")
        
        self.shape_button = QLabel()
        self.shape_button.setPixmap(QPixmap("blank.png"))
        
        
        # Create QTextEdit for reading server messages 
        self.server_messages = QPlainTextEdit("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
        self.server_messages.setFont(QFont("Courier New Bold"))
        self.server_messages.setReadOnly(True)
        
        # Create Playing Board
        playing_board_layout = QGridLayout()
        
        self.button_0 = QToolButton()
        self.button_0.setFixedSize(95,95)
        
        self.button_1 = QToolButton()
        self.button_1.setFixedSize(95,95)
        
        self.button_2 = QToolButton()
        self.button_2.setFixedSize(95,95)
        
        self.button_3 = QToolButton()
        self.button_3.setFixedSize(95,95)
        
        self.button_4 = QToolButton()
        self.button_4.setFixedSize(95,95)
        
        self.button_5 = QToolButton()
        self.button_5.setFixedSize(95,95)
        
        self.button_6 = QToolButton()
        self.button_6.setFixedSize(95,95)
        
        self.button_7 = QToolButton()
        self.button_7.setFixedSize(95,95)
        
        self.button_8 = QToolButton()
        self.button_8.setFixedSize(95,95)
        
        # Disabling the buttons
        self.enable_disable("Disable Buttons")
        
        # Create ComboBox
        self.combo = QComboBox()
        self.combo.addItem("Black & Blue Theme")
        self.combo.addItem("Grey Theme")
        
        # Create Theme Label
        self.theme = QLabel("Theme :")
        self.theme.setFont(QFont("Courier New Bold",13,5))
        
        # Organising theme  label with combobox
        self.theme_layout = QHBoxLayout()
        self.theme_layout.addWidget(self.theme)
        self.theme_layout.addWidget(self.combo)
        
        self.theme_widget = QWidget()
        self.theme_widget.setLayout(self.theme_layout)
        
        
        # Organising QToolButtons(Playing grid buttons)
        playing_board_layout.addWidget(self.button_0,0,0,1,1)
        playing_board_layout.setHorizontalSpacing(0)
        playing_board_layout.addWidget(self.button_1,0,1,1,1)
        playing_board_layout.setHorizontalSpacing(0)
        playing_board_layout.addWidget(self.button_2,0,2,1,1)
        playing_board_layout.setHorizontalSpacing(0)
        playing_board_layout.addWidget(self.button_3,1,0,1,1)
        playing_board_layout.setHorizontalSpacing(0)
        playing_board_layout.addWidget(self.button_4,1,1,1,1)
        playing_board_layout.setHorizontalSpacing(0)
        playing_board_layout.addWidget(self.button_5,1,2,1,1)
        playing_board_layout.setHorizontalSpacing(0)
        playing_board_layout.addWidget(self.button_6,2,0,1,1)
        playing_board_layout.setHorizontalSpacing(0)
        playing_board_layout.addWidget(self.button_7,2,1,1,1)
        playing_board_layout.setHorizontalSpacing(0)
        playing_board_layout.addWidget(self.button_8,2,2,1,1)
                
        playing_board_widget =QWidget()
        playing_board_widget.setLayout(playing_board_layout)
        
        # Organising grid heading
        grid_heading_layout = QVBoxLayout()
        grid_heading_layout.addWidget(self.grid_heading_label)
        grid_heading_layout_widget = QWidget()
        grid_heading_layout_widget.setLayout(grid_heading_layout)
        
        # Organising grid heading and playing grid
        game_grid_layout = QVBoxLayout()
        game_grid_layout.addWidget(self.theme_widget)
        game_grid_layout.addWidget(grid_heading_layout_widget)
        game_grid_layout.addWidget(playing_board_widget)
        game_grid_layout_widget = QWidget()
        game_grid_layout_widget.setLayout(game_grid_layout)
        
        
        # Organising shape display
        shape_display_layout = QHBoxLayout()
        shape_display_layout.addWidget(self.shape_label)
        shape_display_layout.addWidget(self.shape_button)
        shape_display_widget = QWidget()
        shape_display_widget.setLayout(shape_display_layout)
        
        # Organising shape display and server messages
        server_messages_layout = QGridLayout()
        server_messages_layout.addWidget(self.server_messages_label,2,0)
        server_messages_layout.addWidget(self.server_messages,3,0)
        server_messages_widget = QWidget()
        server_messages_widget.setLayout(server_messages_layout)
        
        # Organising shape display and server messages
        bottom_info_layout = QVBoxLayout()
        bottom_info_layout.addWidget(shape_display_widget)
        bottom_info_layout.addWidget(server_messages_widget)
        bottom_info_widget = QWidget()
        bottom_info_widget.setLayout(bottom_info_layout)
        
        # Organising server connection label, QlineEdit and button
        top_info_layout = QGridLayout()
        top_info_layout.addWidget(self.server_label,0,0)
        top_info_layout.addWidget(self.server_input,0,1)
        top_info_layout.addWidget(self.connect_button,0,2)
        top_info_widget = QWidget()
        top_info_widget.setLayout(top_info_layout)
        
        # Organising grid with shape display and server messages
        horizonal_box = QHBoxLayout()
        horizonal_box.addWidget(bottom_info_widget)
        horizonal_box.addWidget(game_grid_layout_widget)
        horizonal_box_widget = QWidget()
        horizonal_box_widget.setLayout(horizonal_box)
        
        # Organising the quit button
        quit_layout = QVBoxLayout()
        quit_layout.addWidget(self.quit_button)
        quit_widget =QWidget()
        quit_widget.setLayout(quit_layout)
        
        # Inserting widgets to main window
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.heading_label)
        main_layout.addWidget(top_info_widget)
        main_layout.addWidget(horizonal_box_widget)
        main_layout.addWidget(quit_widget)
        
        self.setLayout(main_layout)
        
        self.loop_thread = LoopThread()
        self.loop_thread.messageSignal.connect(self.handle_message)
        
        # Creating Button group for the playing grid to receive signals
        self.button_group = QButtonGroup()
        self.button_group.addButton(self.button_0,0)
        self.button_group.addButton(self.button_1,1)
        self.button_group.addButton(self.button_2,2)
        self.button_group.addButton(self.button_3,3)
        self.button_group.addButton(self.button_4,4)
        self.button_group.addButton(self.button_5,5)
        self.button_group.addButton(self.button_6,6)
        self.button_group.addButton(self.button_7,7)
        self.button_group.addButton(self.button_8,8)
        
        
        # Connecting buttons to slots
        self.connect_button.clicked.connect(self.clicked_connect)
        self.quit_button.clicked.connect(self.clicked_quit)
        self.button_group.buttonClicked.connect(self.clicked_button)
        self.combo.currentTextChanged.connect(self.theme_changer)
        
    def clear_board(self):
        self.board = [' '] * BOARD_SIZE
        
    def theme_changer(self):                     # Theme changer enchancement(NerdZone)
        choice = self.combo.currentIndex()
        if choice == 0:
            app.setStyleSheet(blackAndBlueTheme_stylesheet)
            
        elif choice == 1:
            app.setStyleSheet(greyTheme_stylesheet)
            
    
    def handle_message(self,msg):
        msg_strip = msg[:msg.find(",")]           # Strips the string to get the message before the comma
        if msg_strip == "new game":
            self.enable_disable("Enable Buttons")
            self.clear_buttons()
            character = msg[-1]                  # Gets each player's character
            if character == "X":
                self.shape_button.setPixmap(QPixmap("cross_shapeDisplay.png"))
                
            else:
                self.shape_button.setPixmap(QPixmap("nought_shapeDisplay.png"))
                
            self.server_messages.appendPlainText("New game,you'll be playing with the " +str(character)+ " character.\n")
        
        elif msg == "your move":
            self.server_messages.appendPlainText("It's your turn to move....\n")
            self.enable_disable("Enable Buttons")
            
        elif msg == "opponents move":
            self.server_messages.appendPlainText("Wait for opponent to make a move....\n")
            self.enable_disable("Disable Buttons")
            
        elif msg_strip == "valid move":      # Sends to both
            shape = msg[-3]# Gets the character from the message
            position = msg[-1] # Gets the position from the message
            if position == "0":
                if shape == "X":
                    self.button_0.setIcon(QIcon("cross_gridDisplay.png"))
                    self.button_0.setIconSize(QSize(100,100))
                    self.button_0.setEnabled(False)
                    self.click_player.play()
                else:
                    self.button_0.setIcon(QIcon("nought_gridDisplay.png"))
                    self.button_0.setIconSize(QSize(100,100))
                    self.button_0.setEnabled(False)
                    self.click_player.play()
            
            elif position == "1":
                if shape == "X":
                    self.button_1.setIcon(QIcon("cross_gridDisplay.png"))
                    self.button_1.setIconSize(QSize(100,100))
                    self.button_1.setEnabled(False)
                    self.click_player.play()
                else:
                    self.button_1.setIcon(QIcon("nought_gridDisplay.png"))
                    self.button_1.setIconSize(QSize(100,100))
                    self.button_1.setEnabled(False)
                    self.click_player.play()
            
            elif position == "2":
                if shape == "X":
                    self.button_2.setIcon(QIcon("cross_gridDisplay.png"))
                    self.button_2.setIconSize(QSize(100,100))
                    self.button_2.setEnabled(False)
                    self.click_player.play()
                else:
                    self.button_2.setIcon(QIcon("nought_gridDisplay.png"))
                    self.button_2.setIconSize(QSize(100,100))
                    self.button_2.setEnabled(False)
                    self.click_player.play()
            
            elif position == "3":
                if shape == "X":
                    self.button_3.setIcon(QIcon("cross_gridDisplay.png"))
                    self.button_3.setIconSize(QSize(100,100))
                    self.button_3.setEnabled(False)
                    self.click_player.play()
                else:
                    self.button_3.setIcon(QIcon("nought_gridDisplay.png"))
                    self.button_3.setIconSize(QSize(100,100))
                    self.button_3.setEnabled(False)
                    self.click_player.play()
                    
            elif position == "4":
                if shape == "X":
                    self.button_4.setIcon(QIcon("cross_gridDisplay.png"))
                    self.button_4.setIconSize(QSize(100,100))
                    self.button_4.setEnabled(False)
                    self.click_player.play()
                else:
                    self.button_4.setIcon(QIcon("nought_gridDisplay.png"))
                    self.button_4.setIconSize(QSize(100,100))
                    self.button_4.setEnabled(False)
                    self.click_player.play()
                    
            elif position == "5":
                if shape == "X":
                    self.button_5.setIcon(QIcon("cross_gridDisplay.png"))
                    self.button_5.setIconSize(QSize(100,100))
                    self.button_5.setEnabled(False)
                    self.click_player.play()
                else:
                    self.button_5.setIcon(QIcon("nought_gridDisplay.png"))
                    self.button_5.setIconSize(QSize(100,100))
                    self.button_5.setEnabled(False)
                    self.click_player.play()
                    
            elif position == "6":
                if shape == "X":
                    self.button_6.setIcon(QIcon("cross_gridDisplay.png"))
                    self.button_6.setIconSize(QSize(100,100))
                    self.button_6.setEnabled(False)
                    self.click_player.play()
                else:
                    self.button_6.setIcon(QIcon("nought_gridDisplay.png"))
                    self.button_6.setIconSize(QSize(100,100))
                    self.button_6.setEnabled(False)
                    self.click_player.play()
                    
            elif position == "7":
                if shape == "X":
                    self.button_7.setIcon(QIcon("cross_gridDisplay.png"))
                    self.button_7.setIconSize(QSize(100,100))
                    self.button_7.setEnabled(False)
                    self.click_player.play()
                else:
                    self.button_7.setIcon(QIcon("nought_gridDisplay.png"))
                    self.button_7.setIconSize(QSize(100,100))
                    self.button_7.setEnabled(False)
                    self.click_player.play()
                    
            elif position == "8":
                if shape == "X":
                    self.button_8.setIcon(QIcon("cross_gridDisplay.png"))
                    self.button_8.setIconSize(QSize(100,100))
                    self.button_8.setEnabled(False)
                    self.click_player.play()
                else:
                    self.button_8.setIcon(QIcon("nought_gridDisplay.png"))
                    self.button_8.setIconSize(QSize(100,100))
                    self.button_8.setEnabled(False)
                    self.click_player.play()
        elif msg == "invalid move":
            self.server_messages.appendPlainText("!!! INVALID MOVE !!!\n")        
        
        elif msg_strip == "game over":
            self.gameover_player.play()
            winning_character = msg[-1]           # Gets the character from the message
            if winning_character == "X" or winning_character == "O":
                self.enable_disable("Disable Buttons")
                self.server_messages.appendPlainText("Game over! The winner is " +winning_character+ "!\n")
            elif winning_character == "T":
                self.server_messages.appendPlainText(" Game over! There's no winner, it's a tie.\n")
                self.enable_disable("Disable Buttons")
                
                
                
        elif msg == "play again":
            self.showdialog()
            
        elif msg == "exit game":
            self.server_messages.appendPlainText("Someone decided to exit the game.Press 'Quit' to leave the game")
            
            
            
    def clear_buttons(self):
        self.button_0.setIcon(QIcon(""))
        self.button_1.setIcon(QIcon(""))
        self.button_2.setIcon(QIcon(""))
        self.button_3.setIcon(QIcon(""))
        self.button_4.setIcon(QIcon(""))
        self.button_5.setIcon(QIcon(""))
        self.button_6.setIcon(QIcon(""))
        self.button_7.setIcon(QIcon(""))
        self.button_8.setIcon(QIcon(""))
            
    def enable_disable(self,sign):                      # Enhancement function which enables and disables the buttons as the game progresses for the players
        if sign == "Enable Buttons":
            self.button_0.setDisabled(False)
            self.button_1.setDisabled(False)
            self.button_2.setDisabled(False)
            self.button_3.setDisabled(False)
            self.button_4.setDisabled(False)
            self.button_5.setDisabled(False)
            self.button_6.setDisabled(False)
            self.button_7.setDisabled(False)
            self.button_8.setDisabled(False)
            
        
        elif sign == "Disable Buttons":
            self.button_0.setEnabled(False)
            self.button_1.setEnabled(False)
            self.button_2.setEnabled(False)
            self.button_3.setEnabled(False)
            self.button_4.setEnabled(False)
            self.button_5.setEnabled(False)
            self.button_6.setEnabled(False)
            self.button_7.setEnabled(False)
            self.button_8.setEnabled(False)
        
    def clicked_connect(self):
            try:
                self.connect_to_server(str(self.server_input.displayText()))
                self.server_messages.appendPlainText("Server Succesfully Connected\n")
                self.connect_button.setEnabled(False)
            except:
                self.server_messages.appendPlainText("Error connecting to server!\n")
                
            else:
                self.loop_thread.start()
    
    def clicked_quit(self):
        self.close()
        
    def clicked_button(self, btn):
        self.send_message(str(self.button_group.id(btn)))             # Sends a signal to server as to which button/position was pressed


    def showdialog(self):
        message= QMessageBox()
        message.setWindowTitle("OXO GAME")
        message.setWindowIcon(QIcon("tic-tac-toe"))
        message.setIcon(QMessageBox.Question)
        message.setText("Do You Want To Play Again?")
        message.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        message.buttonClicked.connect(self.message_button)
        
        message_execute = message.exec_()
    
    
    def message_button(self,reply):
        reply = str(reply.text())
        reply = reply[1].lower()
        if reply == "y":
            self.send_message(reply)
            self.clear_board()
        elif reply == "n":
            self.send_message(reply)
        
# Stylesheet to help describe the style of the GUI
greyTheme_stylesheet = """
QWidget{
        background-color: #3a3a3a;
        color: #fff;
        selection-background-color: #b78620;
        selection-color: #000;
        }

QLabel{
        background-color: transparent;
        color: #fff;
        }

QToolBar{
        background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(69, 69, 69, 255),stop:1 rgba(58, 58, 58, 255));
        border-top: none;
        border-bottom: 1px solid #4f4f4f;
        border-left: 1px solid #4f4f4f;
        border-right: 1px solid #4f4f4f;        
        background-color: transparent;
        color: #fff;
        padding: 5px;
        padding-left: 8px;
        padding-right: 8px;
        margin-left: 1px;
        }


QToolBar::separator{
        background-color: #2e2e2e;
        width: 1px;
        }



QToolButton:hover{
        background-color: rgba(183, 134, 32, 20%);
        border: 1px solid #b78620;
        color: #fff;
        }


QToolButton:pressed{
        background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(57, 57, 57, 255),stop:1 rgba(50, 50, 50, 255));
        border: 1px solid #b78620;
        }


QToolButton:checked{
        background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(57, 57, 57, 255),stop:1 rgba(50, 50, 50, 255));
        border: 1px solid #222;
        }
QPushButton{
        background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(84, 84, 84, 255),stop:1 rgba(59, 59, 59, 255));
        color: #ffffff;
        min-width: 80px;
        border-style: solid;
        border-width: 1px;
        border-radius: 3px;
        border-color: #051a39;
        padding: 5px;
        }


QPushButton::flat{
        background-color: transparent;
        border: none;
        color: #fff;
        }


QPushButton::disabled{
        background-color: #404040;
        color: #656565;
        border-color: #051a39;
        }


QPushButton::hover{
        background-color: rgba(183, 134, 32, 20%);
        border: 1px solid #b78620;
        }


QPushButton::pressed{
        background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(74, 74, 74, 255),stop:1 rgba(49, 49, 49, 255));
        border: 1px solid #b78620;
        }


QPushButton::checked{
        background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(74, 74, 74, 255),stop:1 rgba(49, 49, 49, 255));
        border: 1px solid #222;
        }



QLineEdit{
        background-color: #131313;
        color : #eee;
        border: 1px solid #343434;
        border-radius: 2px;
        padding: 3px;
        padding-left: 5px;
        }
        
QTextEdit{
        background-color: #131313;
        color : #eee;
        border: 1px solid #343434;
        border-radius: 2px;
        padding: 3px;
        padding-left: 5px;
        }
"""

blackAndBlueTheme_stylesheet = """ 

QWidget{
        background-color: #121212;
        color: #ffffff;
        border-color: #051a39;
        }



QLabel{
        background-color: transparent;
        color: #ffffff;
        }

QLabel::disabled{
        background-color: transparent;
        color: #656565;
        }

QPushButton{
        background-color: #607cff;
        color: #ffffff;
        min-width: 80px;
        border-style: solid;
        border-width: 1px;
        border-radius: 3px;
        border-color: #051a39;
        padding: 5px;
        }


QPushButton::disabled{
        background-color: #404040;
        color: #656565;
        border-color: #051a39;
        }


QPushButton::hover{
        background-color: #8399ff;
        color: #ffffff;
        border-style: solid;
        border-width: 1px;
        border-radius: 3px;
        border-color: #051a39;
        padding: 5px;
        }


QPushButton::pressed{
        background-color: #4969ff;
        color: #ffffff;
        border-style: solid;
        border-width: 1px;
        border-radius: 3px;
        border-color: #051a39;
        padding: 5px;
        }



QToolButton{
        background-color: #607cff;
        color: #ffffff;
        padding: 5px;
        padding-left: 8px;
        padding-right: 8px;
        margin-left: 1px;
        }


QToolButton::disabled{
        background-color: #404040;
        color: #656565;
        border-color: #051a39;
        }


QToolButton::hover{
        background-color: #8399ff;
        color: #ffffff;
        border-width: 1px;
        border-radius: 3px;
        border-color: #051a39;
        padding: 3px;
        }


QToolButton::pressed{
        background-color: #4969ff;
        color: #ffffff;
        border: 1px solid #b78620;
        }



QComboBox{
    background-color: #607cff;
    border: 1px solid;
    border-radius: 3px;
    padding-left: 6px;
    color: #ffffff;
    height: 20px;
    }


QComboBox::disabled{
        background-color: #404040;
        color: #656565;
        border-color: #051a39;
        }


QComboBox:hover{
    background-color: #8399ff;
    }


QComboBox:on{
    background-color: #4969ff;}


QComboBox QAbstractItemView{
    background-color: #383838;
    color: #ffffff;
    border: 1px solid black;
    selection-background-color: #4969ff;
    selection-color: #ffffff;
    outline: 0;
    }


QComboBox::drop-down{
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 15px;
    border-left-width: 0px;
    border-left-color: darkgray;
    border-left-style: solid; 
    border-top-right-radius: 3px; 
    border-bottom-right-radius: 3px;
    }


QComboBox::down-arrow{
    image: url(://arrow-down.png);
    width: 8px;
    height: 8px;
    }

QLineEdit{
        background-color: #525251;
        color: #ffffff;
        border: 1px solid #343434;
        border-radius: 2px;
        padding: 3px;
        padding-left: 5px;
        }


QLineEdit::disabled{
        background-color: #404040;
        color: #656565;
        border: 1px solid #343434;
        border-radius: 2px;
        padding: 3px;
        padding-left: 5px;
        }



QTextEdit{
        background-color: #ffffff;
        color: #010201;
        border-color: #051a39;
        }


QTextEdit::disabled{
        background-color: #404040;
        color: #656565;
        border-color: #051a39;
        }

"""


app = QApplication(sys.argv)
abs_widget = OXO_GUI()
def main():
    app.setStyleSheet(blackAndBlueTheme_stylesheet)
    abs_widget.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()