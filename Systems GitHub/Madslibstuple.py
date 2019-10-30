#!/usr/bin/python3
import random

noun=("John", "Braydon", "Deverie", "Corinna", "Ryan", "America", "China", \
        "Taj Mahal ", "Hair", "Ball")
verb=("Jump", "Run", "Walk", "Crawl", "Dance", "Go", "Slide", "Stand up")
adj=("Green", "Red", "Yellow", "Fat", "Skinny", "Amazing", "Hot", \
        "Sparkly", "Disgusting", "Clumsy", "Microscopic")
animal=("Whale", "Horse", "Narwhal", "Squirrel", "Dog", "Cat", "Elephant", \
        "Mouse", "Bird")
people=("President", "Brother", "Sister", "Weirdos", "Fireperson", "Nurse", \
        "Mailman", "Flight Attendant")
place=("Rocky Mountains", "Lake Ontario", "Ocean", "Colorado Springs", \
        "New Mexico", "Washington")
season=("Spring", "Summer", "Fall", "Autumn", "Winter")
superhero=("Batman", "Superman", "Wolverine", "Flash", "Speed Racer", \
        "Nightcrawler", "Aquaman")

def elem(tuple):
    value=random.randint(0,len(tuple)-1)
    return tuple[value]

if__name__=='main__':
    print(f"Every +elem(season)+","+elem(superhero) is joining forces with The \
{tup3[value3]} to defeat the forces of evil, by revealing their \ 
secret identity as {tup[value}]. They want to {tup1[value1]}, \
but can only {tup1[value1]} so they hide in {tup2[value2]}, \
{tup5[value5]} and become {tup2[value2}] {tup4[value4}] until \
the next {tup6[value6]}.")
