class Node:
    def __init__(self, state=None, parent=None, steps=None, energy=None, treasure=None, unwanted=None):
        self.state = state
        self.parent = parent
        self.steps = steps
        self.energy = energy
        self.treasure = treasure
        self.unwanted = unwanted
       

#Function to expand and return childnode
def expandAndReturnChildren(virtual_map, node):
    children = []

    for [a, b, s, e, tr, u] in virtual_map:
        if a == node.state:
            childnode = Node(b, node, s, e, tr, u)
            children.append(childnode)

    return children

#Function to calculate energy
def pathenergy(node):
    energy = 0
    while node.parent is not None:

        energy += node.energy
        node = node.parent

    return energy

#Function to calculate amount of treasure 
def checktreasureAmount(node):
    treasure = 0
    while node.parent is not None:

        treasure += node.treasure
        node = node.parent

    return treasure


def ucs(virtual_map, initial_state, goal_amount):
    explored = []
    frontier = []
    totalcost = 0

    TRamount = 0
    number = 0
    #append the first node or the entry node
    frontier.append(Node(initial_state, None, 0, 0, 0, False))

    expandlist.append(initial_state)
    #if Treasure collected is not 4 then continue to run
    while TRamount != goal_amount:

        if initial_state == 'TR':
            TRamount += 1
        # Sort based on the total energy used for the path
        frontier.sort(key=lambda x: pathenergy(x))

        
        # After sorting to get the lowest total energy used, expand them and append
        # into explore
        children = expandAndReturnChildren(virtual_map, frontier[0])
        explored.append(frontier[0])

        del frontier[0]

        for child in children:
            #Condition to check if a state had been explored or not
            #Condition to filter out unwanted objects during expansion
            if (child.unwanted == False) and not (child.state in [e.state for e in explored]):
                
                
                totalcost += pathenergy(child)
                TRamount=checktreasureAmount(child)
                
                queue.append(totalcost)

              
                #Check if collected all four treasures
                if TRamount == goal_amount:
                    goal_node = child

                    break
                
                frontier.append(child)

                expandlist.append(child.state)
                #Check if any of the queue is more than total cost
                #In order word totalcost is less than the numbers in queue
                #Then replace queue with this number
                if (q > totalcost for q in queue):
                    queue.sort()
                    totalcost = queue[0]
                    del queue[0]

                totalcost = 0

    solution = [goal_node.state]
    trace_node = goal_node
    #Backtrack to return solution after reaching goal amount
    while trace_node.parent is not None:
        solution.insert(0, trace_node.parent.state)

        trace_node = trace_node.parent

    return solution


if __name__ == '__main__':
    #Initialize
    initial_state = "1"
    expandlist = []
    explore = []
    #Queue is for printing energy
    queue = []
    goal_amount = 4
    TRamount = 0
    # TR=Treasure
    # T1=Trap 1
    # T2=Trap 2
    # T3=Trap 3
    # T4=Trap 4
    # OB=Obstacle
    # R1=Reward 1
    # R2=Reward 2
    # Virtualmap format:(State,parent,steps,energy,treasure,unwanted,skipped)
    # 0 means no treasure, 1 means got treasure
    # Unwanted refers to traps and obstacles and skipped path.
    # Skipped path means the node cannot back track if missed treasure is skipped due to the direction and map structure
    # 18b means the direction is from the BACK Direction or the LEFT side of the map
    # 18RR means the route got Double R1 Rewards, only for special occasions
    # RR would not be used much
    # R1B means bottom reward1 and U means up. If didn't write anything then it is top 
    # The direction is not important, most important are the numbers and the characters,
    # For example, 18RR just means going through 18, you can based on the drawings that I gave to go through the direction
    
    virtual_map = [
        ['1', '2', 1, 1, 0, False],
        ['1', 'T2', 1, 1, 0, True],
        ['1', '8', 1, 1, 0, False],
        ['2', 'T2', 1, 1, 0, True],
        ['2', '3', 1, 1, 0, False],
        ['3', '4', 1, 1, 0, False],
        ['3', '11', 1, 1, 0, False],
        ['3', 'T4', 1, 1, 0, True],
        ['4', 'T4', 1, 1, 0, True],
        ['4', 'R1', 1, 1, 0, False],
        ['R1', '5', 1, 0.5, 0, False],
        ['R1', 'TR', 1, 0.5, 1, False],
        ['R1', '13', 1, 0.5, 0, False],
        ['R1U', 'TR1b', 0.25, 0.25, 1, False],
        ['5', '13', 1, 0.5, 0, False],
        ['5', '14', 1, 0.5, 0, False],
        ['5b', 'R1U', 0.25, 0.5, 0, False],
        ['14', '6', 1, 0.5, 0, False],
        ['14', '15', 1, 0.5, 0, False],
        ['14', 'T3', 1, 0.5, 0, True],
        ['14b', '13b', 0.25, 1, 0, False],
        ['6', '16', 1, 0.5, 0, False],
        ['6', '15', 1, 0.5, 0, False],
        ['16', '7', 1, 0.5, 0, False],
        ['16', '17', 1, 0.5, 0, False],
        ['16', 'OB', 1, 0.5, 0, True],
        ['7', '17', 1, 0.5, 0, False],
        ['17', 'OB', 1, 0.5, 0, True],
        ['17', '20', 1, 0.5, 0, False],
        ['20', 'T1', 1, 0.5, 0, True],
        ['20', 'TR4', 1, 0.5, 1, False],
        ['20b', 'T1b', 0.5, 0.5, 0, True],
        ['TR4b', 'T1b', 0.5, 0.5, 0, True],
        ['TR4b', '37b', 0.5, 0.5, 0, False],
        ['T2', '3', 1, 1, 0, True],
        ['8', '10', 1, 1, 0, False],
        ['8', '9', 1, 1, 0, False],
        ['8', 'T2', 1, 1, 0, True],
        ['9', '10', 1, 1, 0, False],
        ['9', 'OB', 1, 1, 0, True],
        ['9', 'R1B', 1, 1, 0, False],
        ['10', '11', 1, 1, 0, False],
        ['10', 'R1B', 1, 1, 0, False],
        ['11', '3', 1, 1, 0, False],
        ['11', '12', 1, 1, 0, False],
        ['11', 'OB', 1, 1, 0, True],
        ['12', 'T4', 1, 1, 0, True],
        ['12', 'TR', 1, 1, 1, False],
        ['12', 'OB', 1, 1, 0, True],
        ['12', 'OB', 1, 1, 0, True],
        ['TR', 'R1', 1, 0.5, 0, False],
        ['TR', '13', 1, 1, 0, False],
        ['TR', '18', 1, 0.5, 0, False],
        ['TR', 'OB', 1, 1, 0, True],
        ['13', '18', 1, 1, 0, False],
        ['13', '18', 1, 0.5, 0, False],
        ['13', '14', 1, 1, 0, False],
        ['13', '14', 1, 0.5, 0, False],
        ['13', 'T3', 1, 1, 0, True],
        ['13b', 'TR1b', 1, 1, 1, False],
        ['13b', 'R1U', 0.25, 0.5, 0, False],
        ['R1U', 'TR1b', 0.25, 0.25, 1, False],
        ['18', 'T3', 1, 0.5, 0, True],
        ['18', 'T3', 1, 1, 0, True],
        ['18', '19', 1, 0.5, 0, False],
        ['18', '19', 1, 1, 0, False],
        ['18b', 'TR1b', 0.25, 0.5, 1, False],
        ['18b', '13b', 0.25, 0.5, 0, False],
        ['19', 'T3', 1, 0.5, 0, True],
        ['19', 'T3', 1, 1, 0, True],
        ['19', 'R2U', 1, 0.5, 0, False],
        ['R2U', '19', 0.5, 0.5, 0, False],
        ['19', 'TR3', 1, 0.5, 1, False],
        ['19', 'OB', 0.5, 0.5, 0, True],
        ['19b', '18b', 0.25, 0.5, 0, False],
        ['19b', '18b', 0.5, 0.5, 0, False],
        ['TR3', 'T1', 1, 1, 0, True],
        ['TR3', '37', 1, 0.5, 0, False],
        ['TR3', 'OB', 1, 0.5, 0, True],
        ['TR3b', '19b', 0.5, 0.5, 0, False],
        ['TR3b', 'R2U', 0.25, 0.5, 0, False],
        ['37', 'TR4', 1, 0.5, 0, False],
        ['TR4', '36', 1, 0.5, 0, False],
        ['37b', 'TR3b', 0.5, 0.5, 1, False],
        ['37b', 'T1b', 0.5, 0.5, 0, True],
        ['37b', 'OB', 0.5, 0.5, 0, True],
        ['36', '35b', 1, 0.5, 0, False],
        ['36', '34b', 1, 0.5, 0, False],
        ['36b', 'TR4b', 0.5, 0.5, 1, False],
        ['34', '36b', 1, 0.5, 0, False],
        ['34', '35', 0.5, 0.5, 1, False],
        ['34b', '35b', 1, 0.5, 1, False],
        ['34b', '33b', 0.5, 0.5, 0, False],
        ['35', '36b', 0.5, 0.5, 0, False],
        ['35', 'OB', 0.5, 0.5, 0, True],
        ['35b', '32b', 0.5, 0.5, 0, False],
        ['35b', '33b', 0.5, 0.5, 0, False],
        ['33b', '32b', 0.5, 0.5, 0, False],
        ['33', '34', 0.5, 0.5, 0, False],
        ['33', '35', 0.5, 0.5, 0, False],
        ['32', '33', 0.5, 0.5, 0, False],
        ['32', '35', 0.5, 0.5, 0, False],
        ['32', 'OB', 0.5, 0.5, 0, True],
        ['32b', '31b', 0.5, 0.5, 0, False],
        ['31', 'OB', 0.5, 0.5, 0, True],
        ['31', '32', 0.5, 0.5, 0, False],
        ['31b', 'R2B', 0.5, 0.5, 0, False],
        ['R2B', 'OB', 0.5, 0.5, 0, True],
        ['R2B', '31', 0.5, 0.5, 0, False],
        ['R2B', '25b', 0.5, 0.5, 0, False],
        ['R2B', 'OB', 0.5, 0.5, 0, True],
        ['R2B', '30b', 0.5, 0.5, 0, False],
        ['R2B', '30', 0.5, 0.5, 0, False],
        ['30', 'OB', 1, 0.5, 0, True],
        ['30', 'R2B', 1, 0.5, 0, False],
        ['30b', 'OB', 0.5, 0.5, 0, True],
        ['30b', '29b', 0.5, 0.5, 0, False],
        ['29b', 'TR2b', 0.5, 0.5, 1, False],
        ['25', 'OB', 1, 0.5, 0, True],
        ['25', 'OB', 1, 0.5, 0, True],
        ['25', 'R2B', 1, 0.5, 0, False],
        ['25b', 'OB', 1, 0.5, 0, True],
        ['25b', '24b', 0.5, 0.5, 0, False],
        ['24b', 'TR2b', 0.5, 0.5, 1, False],
        #
        ['9','R1R',1,1,0,False],
        ['R1B','OB',1,0.5,0,True],
        ['R1B','OB',1,0.5,0,True],
        ['R1B','22',1,0.5,0,False],
        ['R1B','23',1,0.5,0,False],
        ['22','OB',1,0.5,0,True],
        ['22','27',1,0.5,0,False],
        ['22','23',1,0.5,0,False],
        ['22','T2',1,0.5,0,True],
        ['21','OB',1,0.5,0,True],
        ['21','22',1,0.5,0,False],
        ['21','26',1,0.5,0,False],
        ['21','27',1,0.5,0,False],
        ['23','OB',1,0.5,0,True],
        ['23','OB',1,0.5,0,True],
        ['23','TR2',1,0.5,1,False],
        ['23','T2',1,0.5,0,True],
        ['27','T2',1,0.5,0,True],
        ['27','28',1,0.5,0,False],
        ['28','T2',1,0.5,0,True],
        ['28','29',1,0.5,0,False],
        ['29','TR2',1,0.5,1,False],
        ['29','OB',1,0.5,0,True],
        ['29','30',1,0.5,0,False],
        ['TR2','24',1,0.5,0,False],
        ['TR2','OB',1,0.5,0,True],
        ['TR2','29',1,0.5,0,False],
        ['24','OB',1,0.5,0,True],
        ['24','T3',1,0.5,0,True],
        ['24','25',1,0.5,0,False],
        ['24','OB',1,0.5,0,True],
        #
        #Double R1 Route, One R means one R1 
        ['R1R','10R',1,0.5,0,False],
        ['10R','11R',1,0.5,0,False],
        ['10R','OB',1,0.5,0,True],
        ['10R','T2',1,0.5,0,True],
        ['11R','3R',1,0.5,0,False],
        ['11R','T4',1,0.5,0,True],
        ['11R','12R',1,0.5,0,False],
        ['11R','OB',1,0.5,0,True],
        ['12R','TR',1,0.5,0,False],
        ['3R','4R',1,0.5,0,False],
        ['3R','T4',1,0.5,0,True],
        ['3R','11R',1,0.5,0,False],
        ['4R','R1RR',1,0.5,0,False],
        ['4R','T4',1,0.5,0,True],
        ['R1RR','TRRR',1,0.25,1,False],
        ['R1RR','13RR',1,0.25,0,False],
        ['TRRR','18RR',1,0.25,0,False],
        ['13RR','TRRR',1,0.25,1,False],
        ['13RR','T3',1,0.25,0,True],
        ['13RR','18RR',1,0.25,0,False],
        ['18RR','T3',1,0.25,0,True],
        ['18RR','19RR',1,0.25,0,False],
        ['18RR','T3',1,0.25,0,True],
        ['19RR','R2URR',1,0.25,0,False],
        ['19RR','TR3RR',1,0.25,1,False],
        ['19RR','OB',1,0.25,0,True],
        ['R2URR','OB',0.5,0.25,0,True],
        ['R2URR','T1',0.5,0.25,0,True],
        ['R2URR','TR3RR',0.5,0.25,1,False],
        ['TR3RR','T1',1,0.25,0,True],
        ['TR3RR','37RR',1,0.25,0,False],
        ['TR3RR','OB',1,0.25,0,True],
        ['37RR','TR4RR',1,0.25,1,False],
        ['TR4RR','36RR',1,0.25,0,False],
        ['36RR','35RR',1,0.25,0,False],
        ['36RR','34RR',1,0.25,0,False],
        ['34RR','35RR',1,0.25,0,False],
        ['34RR','33RR',1,0.25,0,False],
        ['35RR','OB',1,0.25,0,True],
        ['35RR','32RR',1,0.25,0,False],
        ['35RR','33RR',1,0.25,0,False],
        ['33RR','32RR',1,0.25,0,False],
        ['32RR','OB',1,0.25,0,True],
        ['32RR','OB',1,0.25,0,True],
        ['32RR','31RR',1,0.25,0,False],
        ['31RR','OB',1,0.25,0,True],
        ['31RR','R2BRR',1,0.25,0,False],
        ['R2BRR','25RR',0.5,0.25,0,False],
        ['R2BRR','OB',0.5,0.25,0,True],
        ['R2BRR','30RR',0.5,0.25,0,False],
        ['25RR','OB',0.5,0.25,0,True],
        ['25RR','24RR',0.5,0.25,0,False],
        ['24RR','TR2RR',0.5,0.25,1,False],
        ['24RR','OB',0.5,0.25,0,True],
        ['30RR','OB',0.5,0.25,0,True],
        ['30RR','29RR',0.5,0.25,0,False],
        ['29RR','OB',0.5,0.25,0,True],
        ['29RR','TR2RR',0.5,0.25,1,False],
        ['37RR','36RR',0.5,0.25,0,True],
        ['37RR','35RR',0.5,0.25,0,True]
        
    ]
    print('Solution: ' + str(ucs(virtual_map,initial_state, goal_amount))+" "+" Total energy: "  +str(queue[0]))
