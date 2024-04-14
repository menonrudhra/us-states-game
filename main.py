import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "assets/images/blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

state_text = turtle.Turtle()
state_text.penup()
state_text.hideturtle()

game_over = False

data = pandas.read_csv("assets/files/50_states.csv")
state_list = data.state.to_list()
guessed_states = []
score = 0

while not game_over:
    if score < 50 :
        answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name")
        answer_state = answer_state.title()
        if answer_state == "Exit":
            game_over = True
        if answer_state in state_list:
            guessed_states.append(answer_state)
            x_cor = int(data[data.state == answer_state].x)
            y_cor = int(data[data.state == answer_state].y)
            state_text.goto(x_cor, y_cor)
            state_text.write(answer_state, align='left', font=('Arial', 10, 'normal'))
            score += 1
    else:
        game_over_text = turtle.Turtle()
        game_over_text.penup()
        game_over_text.hideturtle()
        state_text.goto(0,0)
        state_text.write("GAME OVER", align='left', font=('Arial', 20, 'normal'))
        game_over = True

# States to learn.csv
if score < 50:
    states_to_learn = [state for state in state_list if state not in guessed_states]
    df = pandas.DataFrame.from_dict(states_to_learn)
    df.to_csv("assets/files/states_to_learn.csv")



