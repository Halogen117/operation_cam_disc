import math
import time
import turtle

def constantAcceleration(motionSegment, angularRange): 
    #MATH
    return 0

def simpleHarmonic(motionSegment, angularRange): 
    #MATH
    return 0

def cycloidal(motionSegment, angularRange): 
    #MATH
    return 0

def displacementCurve(motionSegment, angularRange, motionType):
    x = 0
    if motionType == 1:
        x = constantAcceleration(motionSegment, angularRange)
       
    elif motionType == 2:
        x = simpleHarmonic(motionSegment, angularRange)
        
    elif motionType == 3:
        x = cycloidal(motionSegment, angularRange)

    else:
        print("error")
    return x

def displacementCurveGraph(curve): 
    screenTurtle  =turtle.getScreen()
    turtleClass = turtle.Turtle()
    # Let's try a hard-coded value
    
    # Straight line first

    # Curve that goes up
    turtle.circle(120,180)

    # Curve that goes straight again

    # Curve that goes down

    # Curve that straightens again


    #TURTLE
    #build graph using turtle
    return 0

def camProfile(baseCircle, follower): 
    #MATH
    return 1



def main():
    running = True

    while(running):
        # Should this be automatically detected?
        inputType = input("Select type:\n1: Main\n2: Test\n")


        #MAIN
        if (inputType == "1"):
            #get user input on motion segment, angular range and type of motion
            #insert the 3 variables into displacement curve formula
            #generate and display graph using the curve with turtle
            #get user input for cam profile, radius of base circle and follower
            #genereate graph with cam profile
            running = False

        #TESTING
        elif (inputType == "2"):
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