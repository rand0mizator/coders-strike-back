import sys
import math

x_prev = 0 #coordinate x of pod in previous turn
y_prev = 0 #coordinate y of pod in previous turn
booster = 1 #booster counter, if == 1 -not used, if == 0 - allready used
i = 0 #turns counter
def clamp(num, min_value, max_value): #function limits multiplicators in thrust calculation to [0,1]
   return max(min(num, max_value), min_value)

# game loop
while True:
    # next_checkpoint_x: x position of the next check point
    # next_checkpoint_y: y position of the next check point
    # next_checkpoint_dist: distance to the next checkpoint
    # next_checkpoint_angle: angle between your pod orientation and the direction of the next checkpoint
    x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [int(i) for i in input().split()]
    opponent_x, opponent_y = [int(i) for i in input().split()]

    x_now = x #current coordinate x of pod
    y_now = y #current coordinate y of pod
    speed_x = x_now - x_prev #calculate position change between two consecutive turns
    speed_y = y_now - y_prev
    
    if i == 0:
        print(str(next_checkpoint_x) + " " + str(next_checkpoint_y) + " 100") #due to x_prev, y_prev = 0 in first turn,
                                                                              # pod targets point too far from next target
                                                                              # so in first turn(i==0) we always use full thrust
    else:    
        if (next_checkpoint_angle < -90) or (next_checkpoint_angle > 90): #if misalign too much - full stop
            thrust = 0
            print("BRAAAAAKE", file=sys.stderr, flush=True) #info print
        else:
            if (next_checkpoint_angle > -5) and (next_checkpoint_angle < 5) and (3000 < next_checkpoint_dist) and (booster == 1): #if looking at next point directly and it far - use BOOST
                thrust = 'BOOST'
                print("BOOOOOOOOOOOOOOOOOOOST", file=sys.stderr, flush=True) 
                booster = 0
            else:
                thrust = int(100 * clamp((1 - next_checkpoint_angle/90), 0, 1) * clamp((next_checkpoint_dist / 1500), 0, 1)) #thrust calculation, if angle to point too much - slow down
                                                                                                                             #if quite close to point (<1500) slow down
        print(str(next_checkpoint_x - 3 * speed_x) + " " + str(next_checkpoint_y - 3 * speed_y) + " " + str(thrust))
    i = i + 1
    x_prev = x_now
    y_prev = y_now