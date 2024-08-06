import os
import time
import copy
from searchAgents import * 
import argparse 


class Agent:
    def __init__(self, x, y) -> None:
        self.x, self.y = x, y

    def __str__(self) -> str:
        return 'P'

    def get_possible_actions(self, state, pos_agent=None):
        
        def is_valid(x, y):
            h, w = len(state), len(state[0])
            if (0<=y and y<h) and (0<=x and x<w): return True
            return False

        if pos_agent is None: pos_agent = (self.x, self.y)
        x, y = pos_agent
        possible_actions = []

        y_, x_ = y-1, x
        if is_valid(x_, y_) and state[y_][x_] != '%': possible_actions.append((0, -1))

        y_, x_ = y+1, x
        if is_valid(x_, y_) and state[y_][x_] != '%': possible_actions.append((0, 1))

        y_, x_ = y, x-1
        if is_valid(x_, y_) and state[y_][x_] != '%': possible_actions.append((-1, 0))

        y_, x_ = y, x+1
        if is_valid(x_, y_) and state[y_][x_] != '%': possible_actions.append((1, 0))
        return possible_actions
    
    def get_pos(self):
        return (self.x, self.y)

    def update_pos(self, pos_agent):
        x, y = pos_agent
        self.x, self.y = x, y

class Food:
    def __init__(self, x, y) -> None:
        self.x, self.y = x, y

    def __str__(self) -> str:
        return '.'

    def get_pos(self):
        return (self.x, self.y)
            
class Corner:
    def __init__(self, x, y) -> None:
        self.x, self.y = x, y

    def __str__(self) -> str:
        return ' '

    def get_pos(self):
        return (self.x, self.y)
class MultiFoodSearchProblem:
    
    def __init__(self, layout_path) -> None:
        self.agent = None
        self.foods = None
        self.corners= None
        self.init_state = self.read_layout(layout_path)
        self.current_state = self.init_state

    def read_layout(self, layout_path):
        state = []
        with open(layout_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                state.append([i for i in line])
            
            for i in range(len(state)):
                for j in range(len(state[i])):
                    if state[i][j] == 'P':
                        self.agent = Agent(j, i)
                        state[i][j] = self.agent
                    if (i==1 and j==1) or (i==len(state)-2 and j==1) or (i==1 and j==len(state[i])-2) or(i==len(state)-2 and j==len(state[i])-2):
                        if state[i][j]!= '.' and state[i][j]!='%' :
                            corner = Corner(j, i)
                            state[i][j] = corner
                            if self.corners == None: self.corners = [corner]
                            else: self.corners.append(corner)
                    if state[i][j] == '.':
                        food = Food(j, i)
                        state[i][j] = food
                        if self.foods == None: self.foods = [food]
                        else: self.foods.append(food)
            
        return state

    def is_goal(self, path):
        
        food_visited = {}
        corner_visited={}
        for i in range(len(self.foods)):
            food_visited[self.foods[i].get_pos()] = 0
        for i in range(len(self.corners)):
            corner_visited[self.corners[i].get_pos()] = 0
        x, y = self.agent.get_pos()
        if (x, y) in corner_visited: corner_visited[(x, y)] = 1
        for action in path:
            x, y = self.successor((x, y), action)
            if (x, y) in food_visited: food_visited[(x, y)] = 1
            if (x, y) in corner_visited: corner_visited[(x, y)] = 1
        print(food_visited)
        print(corner_visited)
        if 0 not in food_visited.values() and 0 not in corner_visited.values():return True
        return False

    def successor(self, pos_agent, action):
        x, y = pos_agent
        dx, dy = action 
        x_, y_ = x+dx, y+dy
        return (x_, y_)
        
    def get_cost_path(self, path):
        return len(path)
    
    def get_current_state(self, start_position, path):
        current_state_ = copy.deepcopy(self.init_state) 
        current_state_[self.agent.y][self.agent.x] = ' '
        x, y = start_position
        current_state_[y][x] = 'P'

        for action in path:
            x_, y_ = self.successor((x, y), action)
            current_state_[y_][x_] = 'P'
            current_state_[y][x] = ' '
            x, y = x_, y_
        return current_state_

    def animate(self, actions=[]):
        print(actions)
        for action in actions:
            x, y = self.agent.get_pos()
            x_, y_ = self.successor((x, y), action)
            self.agent.update_pos((x_, y_))
            self.current_state[y_][x_] = self.agent
            self.current_state[y][x] = ' '
            os.system('cls') #if you use Windows
            #os.system('clear') #if you use MacOS
            for i in range(len(self.current_state)):
                for j in range(len(self.current_state[i])):
                    print(self.init_state[i][j], end='')
                print()
            time.sleep(0.1)
            

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run Pac-Man game with specified layout and algorithm')
    parser.add_argument('--layout', type=str, required=True, help='Path to the layout file (with .lay extension)')
    parser.add_argument('-a', '--algorithm', type=str, default='aStarSearch', help='Search algorithm to use (ucs, aStarSearch, etc.)')
    args = parser.parse_args()  

    layout_file = args.layout
    game = MultiFoodSearchProblem(layout_file)

    if args.algorithm == 'aStarSearch':
        actions = astar(game)
    elif args.algorithm == 'ucs':
        actions = ucs(game)
    else:
        raise ValueError("Unsupported algorithm. Please use 'ucs' or 'aStarSearch'.")

    game.animate(actions)

    list_ = []
    map_actions = {(-1, 0): 'W', (1, 0): 'E', (0, 1): 'N', (0, -1): 'S'}
    for action in actions:
        list_.extend(map_actions[action])
    list_.append("Stop")
    print(list_)
    print(f'step to destination = {len(actions)}')

