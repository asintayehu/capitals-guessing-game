try:
    import turtle
    import pandas as pd

    screen = turtle.Screen()
    screen.title("U.S. States Game")
    img = "blank_states_img.gif"
    screen.addshape(img)
    turtle.shape(img)

    data = pd.read_csv("50_capitals.csv")
    states = data.state.to_list()

    correct_guesses = []
    states_to_learn = {"States": []}

    while len(correct_guesses) < 50:
        answer_state = screen.textinput(title="Guess the capital", prompt="What's another state's capital?").title()
        if answer_state in states:
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data.state == answer_state]
            t.goto(int(state_data.x), int(state_data.y))
            t.write(answer_state)
            correct_guesses.append(answer_state)
        if answer_state == "Quit".title() or answer_state == "exit".title():
            screen.bye()
            for state in states:
                if state not in correct_guesses:
                    states_to_learn["States"].append(state)
            states_to_learn_df = pd.DataFrame(states_to_learn)
            states_to_learn_df.to_csv("capitals_to_learn.csv")
            raise "You Quit!"
except TypeError:
    print("That's all!")


