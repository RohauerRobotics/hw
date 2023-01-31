# Program for calculating position of Car A and Car B for Quiz #4
import numpy as np

def arc_length(t):
    val = (260*np.pi)/6 + ((72*10**3)/3600)*t + (0.5*2*t**2)
    return val

def a_position(t):
    x = ((108*10**3)/3600)*t - (0.5*t**2)
    y = 260
    return [x, y]


def a_velocity(t):
    x = ((108*10**3)/3600) - t
    y = 0
    return [x, y]

def b_velocity(t):
    s = arc_length(t)
    theta = s/260
    # print("Angle: ", np.degrees(theta))
    # x = 260*np.sin(theta) + 260*np.cos(np.radians(30)) - 260
    x = 260*np.sin(theta) 
    y = 260*np.cos(theta)
    return [x, y]

def b_position(t):
    s = arc_length(t)
    theta = s/260
    print("Angle: ", np.degrees(theta))
    # x = 260*np.sin(theta) + 260*np.cos(np.radians(30)) - 260
    x = 260 - 260*np.cos(theta) - (260 - 260*np.cos(np.radians(30)))
    y = 260*np.sin(theta)
    return [x, y]

times = np.linspace(0,9,10)

for i in times:
    pos_b = b_position(i)
    print(f"\nTime: {i} sec \nx position B: {pos_b[0]} \ny position B: {pos_b[1]}")
    pos_a = a_position(i)
    print(f"x position A: {pos_a[0]} \ny position A: {pos_a[1]}")
    dist = np.sqrt((pos_a[0]-pos_b[0])**2+(pos_a[1]-pos_b[1])**2)
    print(f"Distance from A to B: {dist} m")
    vel_a = a_velocity(i)
    print(f"x velocity A: {vel_a[0]} \ny velocity A: {vel_a[1]}")
    vel_b = b_velocity(i)
    print(f"x velocity B: {vel_b[0]} \ny velocity B: {vel_b[1]}")
