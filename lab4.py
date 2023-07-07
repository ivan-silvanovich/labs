import random
import matplotlib.pyplot as plt
import time


def generate_points(n):
    count = 0
    points = []

    while count < n:
        point = {'X': random.randint(-n, n), 'Y': random.randint(-n, n)}
        if point not in points:
            points.append(point)
            count += 1

    return points


def f(x, A, B, C):
    return (-A * x - C) / B


begin = time.time()

# generating list of points
# random.seed(10)
N = 100
points = generate_points(N)

# sorting
points.sort(key=lambda arr: (arr['X'], arr['Y']))

# calculating mid point
mid_index = N // 2
X0 = points[mid_index]['X']
Y0 = points[mid_index]['Y']

# calculating X1
for i in points[mid_index:0:-1]:
    if i['X'] != X0:
        X1 = i['X']
        break
else:
    X1 = X0 - 1

# calculating X2
for i in points[mid_index:]:
    if i['X'] != X0:
        X2 = i['X']
        break
else:
    X2 = X0 + 1

# calculating Y1
if points[mid_index - 1]['X'] == X0:
    Y1 = Y0
else:
    Y1 = Y0 - 1

# calculating coordinates of 2 points to create equation of line
Ymax = max(points, key=lambda arr: arr['Y'])['Y']
Ymin = min(points, key=lambda arr: arr['Y'])['Y']
Z = min(X0-X1, X2-X0)
if N % 2 == 0:
    X2 = X0
    Y2 = (Y0 + Y1) / 2
    X3 = X0 + Z / 2
    Y3 = Y0 - Ymax + Ymin
else:
    X2 = X0
    Y2 = Y0
    X3 = X0 + Z / 2
    Y3 = Y0 - Ymax + Ymin

# printing found equation of line
A = Y2 - Y3
B = X3 - X2
C = X2 * Y3 - X3 * Y2
print(f'{A}x + {B}y + {C} = 0')
print(f'time: {time.time() - begin}')

# building graph of points and line
X = list(map(lambda arr: arr['X'], points))
Y = list(map(lambda arr: arr['Y'], points))

# adding x and y lines
ax = plt.gca()
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')

# adding frames for showing plot
plt.xlim(-N*1.1, N*1.1)
plt.ylim(-N*1.1, N*1.1)

# showing plot and points
plt.scatter(X, Y)
plt.plot([-N, N], [f(-N, A, B, C), f(N, A, B, C)])
# plt.plot([X2, X3], [Y2, Y3])
plt.show()
