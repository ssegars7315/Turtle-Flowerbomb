from myPolygon import *
#This is taking all functions from myPolygon and importing them all in the code.

import turtle
bob=turtle.Turtle()
sally=turtle.Turtle()
susan=turtle.Turtle()
#Import turtle imports all the turtles that been created.

sally.left(90)
#This first turns sally to the left 90 degrees.
#susan.left(180)
#After it turns sally 90 degrees.It then turns susan left 180 degrees.

turtle.colormode(255)
#This allows any user to use Red, Green, and Blue.

bob.speed(0)
sally.speed(0)
susan.speed(0)
#this allows all of the turtles created to form the design faster.

turtle.bgcolor("red")
#This allows you to change the background color.

for times in range(256):
#This creates a loop, in addition 256 means the total amount of colors

    c=(times,0,125)
    bob.color(c)
    polygon(bob,3,40)
    bob.left(23)
    bob.forward(times*2)
#This creates a spiral with the turtle bob which is a triangle with a distance of 40 and changes the color from blue to magenta.
#It also turns bob to the left 23 degrees, and then forward times *2.

    c=(times,255,150)
    sally.color(c)
    polygon(sally,3,60)
    sally.right(45)
    sally.forward(times*4)
    # This creates a spiral with the turtle sally which is a triangle with a distance of 60, and changes it to cyan.
    #It also turns sally right 45 degrees,and then forward times*4.

    c=(times,0,255)
    susan.color(c)
    polygon(susan,5,50)
    susan.left(23)
    susan.forward(times)
    #This also creates a spiral with the turtle susan which is a pentagon which a distance of 50, and changes the color blue to magenta.
#This also turns susan to the left 23 degrees, and forward times. 



