import turtle
import pandas

screen = turtle.Screen()
screen.title("Canada Provinces Game")
image = "canada_map.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("canada_provinces.csv")
all_provinces = data.province.to_list()
guessed = []


while len(guessed) < 50:
    answer = screen.textinput(title=f"{len(guessed)} / 12 Provinces Correct",
     prompt="What's another provinces's name? ").title()

    if answer == "Exit":
        missing = []
        for province in all_provinces:
            if province not in guessed:
                missing.append(province)
        new_data = pandas.DataFrame(missing)
        new_data.to_csv("provinces_to_learn.csv")
        break
    

    if answer in all_provinces:
        guessed.append(guessed)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        province_data = data[data.province == answer]
        t.goto(float(province_data.x), float(province_data.y))
        t.write(answer)


# turtle.mainloop()