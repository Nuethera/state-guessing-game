import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)

states_data = pandas.read_csv("50_states.csv")
states_name = states_data["state"]
state_list = states_name.to_list()





timmy = turtle.Turtle()
timmy.up()
timmy.ht()

def write_on_map(state):
    xcor = int(state.x)
    ycor = int(state.y)
    timmy.goto(xcor,ycor)
    name = state.state.item()
    timmy.write(arg=name, move=False, align='center', font=('Arial',10,'normal'))

i=0
while i <50:
    screen.update()
    ans_state = screen.textinput(title=f"{i}/50 Guess the state", prompt="Whats Another State Name")
    t = ans_state.title()
    if t in state_list:
        i+=1
        curr_state = states_data[states_name == t]
        write_on_map(curr_state)

screen.exitonclick()

