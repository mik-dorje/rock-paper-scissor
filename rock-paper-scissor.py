import random
import PySimpleGUI as sg #for GUI 
import pyttsx3 #for text to speech 

sg.theme("dark")
HS=0
CS=0
possible_action = ['rock', 'paper', 'scissor']

def rockclick():
    global HS
    global CS
    human_action="rock"
    computer_action = random.choice(possible_action)
    if computer_action=='rock':
        sg.Window("RESULT", [[sg.Text("IT'S A TIE")],
                             [
                sg.Text("Human Score: "+str(HS),text_color="red"),
                sg.Text("CPU Score: "+str(CS),text_color="red")
            ]]).read()
    if computer_action=='paper':
        CS += 1
        sg.Window("RESULT",[
            [sg.Text("Paper covers Rock")],
            [sg.Text("CPU wins")],
            [
                sg.Text("Human Score: "+str(HS),text_color="red"),
                sg.Text("CPU Score: "+str(CS),text_color="red")
            ]
        ]).read()

    if computer_action=='scissor':
        HS += 1
        sg.Window("RESULT",[[sg.Text("Rock smashes Scissor")],
                            [sg.Text("Human wins")],
                            [
                                sg.Text("Human Score: "+str(HS),text_color="red"),
                                sg.Text("CPU Score: "+str(CS),text_color="red")
                            ]
                            ]).read()

def paperclick():
    global HS
    global CS
    human_action="paper"
    computer_action = random.choice(possible_action)
    if computer_action=='paper':
        sg.Window("RESULT", [[sg.Text("IT'S A TIE")],[
                sg.Text("Human Score: "+str(HS),text_color="red"),
                sg.Text("CPU Score: "+str(CS),text_color="red")
            ]]).read()
    if computer_action=='rock':
        HS += 1
        sg.Window("RESULT",[
            [sg.Text("Paper covers Rock")],
            [sg.Text("Human wins")],
            [
                sg.Text("Human Score: "+str(HS),text_color="red"),
                sg.Text("CPU Score: "+str(CS),text_color="red")
            ]
        ]).read()
    if computer_action=='scissor':
        CS += 1
        sg.Window("RESULT",[[sg.Text("Scissor cuts Paper")],
                            [sg.Text("CPU wins")],
                            [
                                sg.Text("Human Score: " + str(HS),text_color="red"),
                                sg.Text("CPU Score: " + str(CS),text_color="red")
                            ]
                            ]).read()
def scissorclick():
    global HS
    global CS
    human_action="scissor"
    computer_action = random.choice(possible_action)
    if computer_action=='scissor':
        sg.Window("RESULT", [[sg.Text("IT'S A TIE")],[
                                sg.Text("Human Score: " + str(HS),text_color="red"),
                                sg.Text("CPU Score: " + str(CS),text_color="red")
                            ]]).read()
    if computer_action == 'rock':
        CS += 1
        sg.Window("RESULT",[[sg.Text("Rock smashes Scissor")],
                            [sg.Text("CPU wins")],
                            [
                                sg.Text("Human Score: " + str(HS),text_color="red"),
                                sg.Text("CPU Score: " + str(CS),text_color="red")
                            ]
                            ]).read()
    if computer_action == 'paper':
        HS += 1
        sg.Window("RESULT",[[sg.Text("Scissor cuts Paper")],
                            [sg.Text("Human wins")],
                            [
                                sg.Text("Human Score: " + str(HS),text_color="red"),
                                sg.Text("CPU Score: " + str(CS),text_color="red")
                            ]
                            ]).read()
def resetscore():
    global HS,CS
    del HS,CS
    HS=CS=0
    layout=[
        [sg.Text("ScoreBoard Cleared!!!")],
        [
            sg.Text("Human Score: "+str(HS),text_color="red"),
            sg.Text("Computer Score: "+str(CS),text_color="red")
        ]
    ]
    sg.Window(title="OUTCOME", layout=layout).read()



#WELCOME SCREEN
welcome_layout=[
    [sg.Text("Enter player name !",text_color='red')],
    [sg.Input(key="-PLAYER_NAME-",do_not_clear=True,size=(30,1))],
    [sg.Button("PLAY",button_color="green")],
    [sg.Text("--Created by MikDorje",pad=[50,0],text_color='cyan')]
]
welcome_window=sg.Window("WELCOME",welcome_layout,margins=(50,30))
pyttsx3.speak("Welcome to the rock, paper and scissor game")

while True:
    event,values=welcome_window.read()

    if event=="PLAY":
        username=(values['-PLAYER_NAME-'])
        playername=username.upper()
    elif event == sg.WIN_CLOSED:
        break
    welcome_window.close()

game_layout=[
    [sg.Text(playername+", PICK A WEAPON!!!")],
    [sg.Button("ROCK",button_color="orange")],
    [sg.Button("PAPER",button_color="orange")],
    [sg.Button("SCISSOR",button_color="orange")],
    [sg.Button("RESET SCORE",button_color="GREEN"),
     sg.Button("EXIT",button_color="RED")]
]
game_window=sg.Window("RPS GAME",game_layout,margins=(50,30),right_click_menu_background_color="white")


while True:
    event,values=game_window.read()
    if event=="ROCK":
        rockclick()
    elif event=="PAPER":
        paperclick()
    elif event=="SCISSOR":
        scissorclick()
    elif event=="RESET SCORE":
        pyttsx3.speak("Resetting the scoreboard")
        resetscore()

    elif event == "EXIT" or event == sg.WIN_CLOSED:
        break
