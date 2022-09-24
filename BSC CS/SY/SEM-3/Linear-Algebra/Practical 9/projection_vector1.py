import numpy as np
 
u = np.array([3, 1])
v = np.array([4, 2]) 

v_norm = np.sqrt(sum(v**2))    

proj_of_u_on_v = (np.dot(u, v)/v_norm**2)*v
 
print("Projection of Vector u on Vector v is: ", proj_of_u_on_v)