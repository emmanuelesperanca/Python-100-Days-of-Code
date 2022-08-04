import turtle
import pandas

screen = turtle.Screen()
screen.title('US States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('50_states.csv')
states = data['state'].to_list()
guessed_states = []
game_on = True

while game_on:
    answer = screen.textinput(title=f'{len(guessed_states)}/50 States Correct', prompt="What's the state's name?").\
        title()
    if answer == 'Exit':
        missing_states = [state for state in states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('states_missed.csv')

        break

    if answer in states:
        guessed_states.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data['state'] == answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer)
