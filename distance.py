# we know that the distance between two points is AB = √([x2-x1]² + [y2-y1]²)
A = [2 , 3]   # declaring x1 and y1
B = [10 , 8]  # declaring x2 and y2

dx = B[0] - A[0]  # the difference of x co-ordinates
dy = B[1] - A[1]  # the difference of y co-ordinates

sdx = dx**2  # the square of the difference of x co-ordinates
sdy = dy**2  # the square of the difference of y co-ordinates

sum = sdx + sdy  # the sum of the differences of the co-ordinates

distance = sum**0.5  # the square root of the sum

print(distance)  # print the distance between point A and B