from email.mime import image
from turtle import Turtle,Screen
import pandas as pd

turtle=Turtle()
screen=Screen()
image='blank_states_img.gif'
screen.addshape(image)

turtle.shape(image)
state_data=pd.read_csv('50_states.csv')
is_guessing=True
states=[]
for state in state_data.state:
    states.append(state)

score=0
count=50
# df.reset_index(inplace=True) # Resets the index, makes factor a colu

while is_guessing:
    user_ans=screen.textinput(title=f'{score}/50 Guessed states',prompt='What is the state').title()
    for st in states:
        if st ==user_ans:
            score+=1
            x=state_data.x[state_data.state==user_ans]
            y=state_data.y[state_data.state==user_ans]
            turtle1=Turtle()
            turtle1.pu()
            turtle1.hideturtle()
            turtle1.goto(int(x),int(y))
            turtle1.write(user_ans)
            screen.title(f'{score}/50')
            if score==50:
                is_guessing=False


screen.exitonclick()
