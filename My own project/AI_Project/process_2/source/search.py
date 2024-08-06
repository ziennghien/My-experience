import math
import random
import numpy as np
from fringes import *

class LocalSearchStrategy:
    def random_restart_hill_climbing(problem, num_trial):
        for i in range(num_trial):
            current =problem.random_restart()
            path = [str(current)]  # Convert current_node to string and add to the path
            while current.get_possible_node(problem.img):
                better = current.get_Z()
                neighbor = None
                successors = current.get_possible_node(problem.img)
                for successor in successors:
                    if better < successor.get_Z():
                        better = successor.get_Z()
                        neighbor = successor
                if better <= current.get_Z():
                    break
                current = neighbor
                path+=[str(current)]  # Add the string representation of the current node to the path
        return path
    
    def simulated_annealing_search(problem,schedule):
        current_node=problem.random_restart()
        path=[str(current_node)]
        for t in range(1,5000):
            T=schedule(t)
            if T == 0:
                break
            successors = current_node.get_possible_node(problem.img)
            if not successors:
                break
            successor = random.choice(successors)
            delta_E = np.subtract(successor.get_Z(), current_node.get_Z())
            if delta_E > 0 or random.random() < math.exp(delta_E / T):
                current_node = successor
                path+=[str(current_node)]
        return path

    def local_beam_search(problem, k):
        beams = PriorityQueue()
        visited=PriorityQueue()
        path=[]
        start_pos = problem.random_start_pos(k)
        start_str=[]
        for node in start_pos:
            beams.push((node),node.get_Z())
            start_str+=[str(node)]
        while not beams.isEmpty():
            temp = PriorityQueue()
            for i in range(beams.qSize()):
                current_node=beams.pop()
                visited.push((current_node),current_node.get_Z())
                neighbor=current_node
                max=current_node.get_Z()
                successors=current_node.get_possible_node(problem.img)
                if not successors:
                    continue
                for successor in successors:
                    if successor.get_Z() > max:
                        max=successor.get_Z()
                        neighbor=successor
                if(neighbor!=current_node):
                    temp.push((neighbor),neighbor.get_Z())
            beams.clear()
            for i in range(k):
                if temp.isEmpty():
                    break
                else:
                    comp = temp.pop()
                    beams.push((comp),comp.get_Z())
        local_max=visited.pop()
        path = []
        vs=[]
        while str(local_max) not in start_str:
            for i in range (visited.qSize()):
                if(vs.__contains__(i)):
                    continue
                successors=visited.get(i).get_possible_node(problem.img)
                for successor in successors:
                    if(str(successor)==str(local_max)):
                        vs.append(i)
                        path+=[str(successor)]
                        local_max=visited.get(i)
                        break
        path.reverse()
        return path
search = LocalSearchStrategy


rrhc = search.random_restart_hill_climbing
sas = search.simulated_annealing_search
lbs = search.local_beam_search

