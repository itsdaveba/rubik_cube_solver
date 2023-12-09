import rubik_solver as rs
import time


start_time = time.time()

cube = rs.Cube(5)
solver = rs.Solver(cube)
print('Scramble:', cube.scramble)
print('Solution:', solver.solve())

print("--- %s seconds ---" % (time.time() - start_time))