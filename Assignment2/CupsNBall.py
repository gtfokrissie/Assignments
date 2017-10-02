ball = [1, 0, 0]
for condition in list(input()):
	if (condition == "A"):
		ball[0], ball[1] = ball[1], ball[0]
	elif (condition == "B"):
		ball[1], ball[2] = ball[2], ball[1]
	elif (condition == "C"):
		ball[0], ball[2] = ball[2], ball[0]
print(ball.index(1)+1)
