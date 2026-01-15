from circle import Circle

print("Testing Circle Class")


#create some circles
print("test 1: creating circles")
circle1 = Circle(radius=10, weight=50)
circle2 = Circle(radius=15, weight=75)

print(f"Circle1: {circle1}")
print(f"Circle1: {circle2}")

#place circles check distance
print("test 2: placing circles")
circle1.set_position(0,0)
circle2.set_position(30,0)

print(f"circle 1 after placement: {circle1}")
print(f"circle 2 after placement: {circle2}")
print(f"Distance between them: {circle1.distance_to(circle2):.2f}")
print(f"Do they overlap? {circle1.overlaps(circle2)}")

print("test 3: testing overlap")
circle3 = Circle(radius=10, weight = 40)
circle3.set_position(20,0)

print(f"Circle 3: {circle3}")
print(f"Circle 2 and Circle 3 overlap? {circle2.overlaps(circle3)}")

print("tests complete")
