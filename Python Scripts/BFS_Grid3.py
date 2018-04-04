# Import a library of functions called 'pygame'
import pygame
from math import pi
import numpy as np

#------------------This function Moving the block (0 element) to the Right, if possible--------------------------

def right(node):
    copyR = list(node[:])
    copyR[0] = abs(copyR[0] + 1)
    copyR = tuple(copyR)
    return copyR

#------------------This function Moving the block (0 element) to the Left, if possible--------------------------
def left(node):
    copyL = list(node[:])
    copyL[0] = abs(copyL[0] - 1)
    copyL = tuple(copyL)
    return copyL

#------------------This function Moving the node Upward, if possible--------------------------
def up(node):
    copyU = list(node[:])
    copyU[1] = abs(copyU[1] + 1)
    return tuple(copyU)

#------------------This function Moving the node Downward, if possible--------------------------
def down(node):
    copyD = list(node[:])
    copyD[1] = abs(copyD[1] - 1)
    return tuple(copyD)
 
#------------------This function Moving the node upward and to the right, if possible--------------------------
def upR(node):
    copyUpR = list(node[:])
    copyUpR[0] = abs(copyUpR[0] + 1)
    copyUpR[1] = abs(copyUpR[1] + 1)
    
    return tuple(copyUpR)
 
#------------------This function Moving the node upward and to the Left, if possible--------------------------
def upL(node):
    copyUpL = list(node[:])
    copyUpL[0] = abs(copyUpL[0] - 1)
    copyUpL[1] = abs(copyUpL[1] + 1)
    return tuple(copyUpL)

#------------------This function Moving the node downward and to the Left, if possible--------------------------
def downL(node):
    copyDownL = list(node[:])
    copyDownL[0] = abs(copyDownL[0] - 1)
    copyDownL[1] = abs(copyDownL[1] - 1)
    return tuple(copyDownL)

#------------------This function Moving the node downward and to the Right, if possible--------------------------
def downR(node):
    copyDownR = list(node[:]) 
    copyDownR[0] = abs(copyDownR[0] + 1)
    copyDownR[1] = abs(copyDownR[1] - 1)

    return tuple(copyDownR)


Q = []
path = []

cost = 0
x1 = (15, 15)
G = (120,15)
visited = []
nodesInfo = []

def BFS(obstaclePoints, finalSquare):

    if (G in obstaclePoints) or (x1 in obstaclePoints):
        print("The point you chose is in the obstacle space, Choose another point")
        return 0

    Q.append(x1)     #Putting first state in Q
    visited.append(x1)     #Putting x1 in Visited

    print(" ")
    print("Q initial: ", Q, "visited initial: ", visited)
    print("Goal : ", G)
    print(" ")
    QSize = len(Q)



    while QSize != 0:       #Runs until Q is empty
        x = Q[0]

        if len(visited) >= 100000:  #Stop the computation if more than 100,000 nodes are visited
            print("Cannot find solution in finite time")
            print("x: ", x)
            print("visited Nodes: ", visited)
            break

        if x == G :     #Stop the computation if result is found
            visited.append(x)
            nodesInfo.append((visited.index(x), visited.index(x), cost))
            print("SUCCESS")
            break
    
        else:
            xDash = right(x)  #Now adding the result of moving right into the xDash            
            if (xDash not in visited) and (xDash not in obstaclePoints):   #Checking if unvisited
                visited.append(xDash)
                Q.append(xDash)
                nodesInfo.append((visited.index(xDash), visited.index(x), cost))


            xDash = left(x)       #Now adding the result of moving left into the xDash
            if (xDash not in visited) and (xDash not in obstaclePoints):   #Checking if unvisited
                visited.append(xDash)
                Q.append(xDash)
                nodesInfo.append((visited.index(xDash), visited.index(x), cost))


            xDash = up(x)         #Now adding the result of moving up into the xDash
            if (xDash not in visited) and (xDash not in obstaclePoints):   #Checking if unvisited
                visited.append(xDash)
                Q.append(xDash)
                nodesInfo.append((visited.index(xDash), visited.index(x), cost))


            xDash = down(x)       #Now adding the result of moving Down into the xDash
            if (xDash not in visited) and (xDash not in obstaclePoints):   #Checking if unvisited
                visited.append(xDash)
                Q.append(xDash)
                nodesInfo.append((visited.index(xDash), visited.index(x), cost))


            xDash = upL(x)       #Now adding the result of moving Down into the xDash
            if (xDash not in visited) and (xDash not in obstaclePoints):   #Checking if unvisited
#                path.append("UL")
                visited.append(xDash)
                Q.append(xDash)
                nodesInfo.append((visited.index(xDash), visited.index(x), cost))
    
            xDash = upR(x)       #Now adding the result of moving Down into the xDash
            if (xDash not in visited) and (xDash not in obstaclePoints):   #Checking if unvisited
#                path.append("UR")
                visited.append(xDash)
                Q.append(xDash)
                nodesInfo.append((visited.index(xDash), visited.index(x), cost))

            xDash = downL(x)       #Now adding the result of moving Down into the xDash
            if (xDash not in visited) and (xDash not in obstaclePoints):   #Checking if unvisited
                visited.append(xDash)
                Q.append(xDash)
                nodesInfo.append((visited.index(xDash), visited.index(x), cost))

            xDash = downR(x)       #Now adding the result of moving Down into the xDash
            if (xDash not in visited) and (xDash not in obstaclePoints):   #Checking if unvisited
                visited.append(xDash)
                Q.append(xDash)
                nodesInfo.append((visited.index(xDash), visited.index(x), cost))

        Q.pop(0)        #Pop the node whose all the childrens are computed and stored
        
    return x


