import math
import time
import turtle



def constant_acceleration(motion_segment, angular_range): 
    # Math calculation needed to find out y?
    y  = 0
    h = 0
    radian = 0
    b_curved = 0
    y = 2*h(radian/b_curved)^2


    screenTurtle  =turtle.getScreen()
    turtleClass = turtle.Turtle()
    # Let's try a hard-coded value
    
    # Straight line first
    turtle.forward(b_curved/2)
    turtle.upwards(h/2)
    # Curve that goes up
    turtle.circle(120,180)

    # Curve that goes straight again
    turtle.forward(b_curved/2)
    turtle.upwards(h/2)
    # Curve that goes up
    turtle.circle(120,180)

    # Curve that goes down

    # Curve that straightens again

    return 0

def simple_harmonic(motion_segment, angular_range): 
    #MATH
    return 0

def cycloidal(motion_segment, angular_range): 
    #MATH
    return 0

def displacement_curve(motion_segment, angular_range, motion_type):
    x = 0
    if motionType == 1:
        x = constant_acceleration(motion_segment, angular_range)
       
    elif motionType == 2:
        x = simpleHarmonic(motion_segment, angular_range)
        
    elif motionType == 3:
        x = cycloidal(motion_segment, angular_range)

    else:
        print("error")
    return x

def displacement_curve_graph(): 



    #TURTLE
    #build graph using turtle
    return 0

def cam_profile(base_circle, follower): 
    #MATH
    return 1


def main():
    running = True

    while(running):
        input_type = input("Select type:\n1: Main\n2: Test\n")

        #MAIN
        if (input_type == "1"):
            #get user input on motion segment, angular range and type of motion
            #insert the 3 variables into displacement curve formula
            #generate and display graph using the curve with turtle
            #get user input for cam profile, radius of base circle and follower
            #genereate graph with cam profile
            running = False

        #TESTING
        elif (input_type == "2"):
            try:
                data = open(input("Enter file directory here: \n"), "r")
            except:
                print("File not found! Exiting program...")
                exit()
            lists = []
            
            for line in data:
                value = line.splitlines()
                
                for row in value:
                    cellValue = row.split(',')
                    lists.append(cellValue)
            for x in lists:
                #generate displacement curve using x[0],x[1],x[2]
                #generate cam profile using x[3],x[4]
                
                input("press enter to continue.")\
                            
            running = False
            
        else:
            print("Please choose 1 or 2.")


if __name__ == "__main__":
    main()