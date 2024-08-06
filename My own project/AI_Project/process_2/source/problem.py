import matplotlib.pyplot as plt
import numpy as np
import cv2
from search import *

class Node:
    def __init__(self, X, Y, Z):
        self.X = X
        self.Y = Y
        self.Z = Z
    def __str__(self):
        return '%d %d %d' %(self.X,self.Y,self.Z)
    def print(self):
        print(str(self))
    def get_X(self):
        return self.X
    
    def get_Y(self):
        return self.Y
    
    def get_Z(self):
        return self.Z
    def get_possible_node(self,img):
        possible_nodes = []
        h, w = img.shape
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                new_x = self.X + dx
                new_y = self.Y + dy
                if 0 <= new_x < w and 0 <= new_y < h:
                    new_node = Node(new_x, new_y, img[new_y, new_x])
                    possible_nodes.append(new_node)
        return possible_nodes
        

        

class Problem:
    def __init__(self,filename):
        self.nodes = []
        self.img = None
        self.state = self.load_state_space(filename)
        self.start_pos = Node(0,0,0)
        self.fig = plt.figure(figsize=(8,6))
        self.ax = plt.axes(projection='3d')
        
    def load_state_space(self,filename):
        state=[]
        img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
        img = cv2.GaussianBlur(img, (5, 5), 0)
        h, w = img.shape
        X = np.arange(w)
        Y = np.arange(h)
        Z=img
        self.img=img
        X, Y = np.meshgrid(X, Y)
        state={'X':X,'Y':Y,'Z':Z}
        for x, y in zip(X.flatten(), Y.flatten()):
            z = img[y, x]
            node= Node(x,y,z)
            self.nodes.append(node)
        return state
    
    def show(self):
        self.ax.plot_surface(self.state['X'], self.state['Y'], self.state['Z'], rstride=1, cstride=1, cmap='viridis', edgecolor='none')
        plt.show()
        
    def draw_path(self, path):
        x_values = [int(point.split(' ')[0]) for point in path]
        y_values = [int(point.split(' ')[1]) for point in path]
        z_values = [int(point.split(' ')[2]) for point in path]
        self.ax.plot(x_values, y_values, z_values, 'r-', zorder=3, linewidth=0.5)
        
    def random_restart(self):
        rd=np.random.choice(self.nodes)
        return rd
    def random_start_pos(self,k):
        rp=np.random.choice(self.nodes,k)
        return rp

