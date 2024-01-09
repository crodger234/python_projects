import turtle 
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"

screen.addshape(image)

turtle.shape(image)

data = pd.read_csv("50_states.csv")
states = data.state.to_list()
number_correct = 0
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f" {len(guessed_states)}/50 States Correct", 
                                    prompt="What's another state").title()
    if answer_state == "Exit":
        incorrect_states = [state for state in states if state not in guessed_states]
        new_data = pd.DataFrame(incorrect_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
        t.write(answer_state)
        
        




turtle.exitonclick()
