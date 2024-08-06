from problem import *

'''problem = Problem("monalisa.jpg")
path = rrhc(problem,1)
problem.draw_path(path)
problem.show()'''


'''def schedule(t):
    return 1/(1000*t**2)
problem = Problem("monalisa.jpg")
path = sas(problem,schedule)
problem.draw_path(path)
problem.show()'''

problem = Problem("monalisa.jpg")
path = lbs(problem,3)
problem.draw_path(path)
problem.show()

