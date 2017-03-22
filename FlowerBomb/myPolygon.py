def polygon( t ,sides, distance):
    angle = 360 / sides
    t.begin_fill()
    for times in range(sides):
        t.forward(distance)
        t.left(angle)
    t.end_fill()
