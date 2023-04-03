from vector_drawing import *
from math import sqrt

dino_vectors = [(6,4), (3,1), (1,2), (-1,5), (2,5), (-3,4), (-4,4), 
    (-5,3), (-5,2), (-2,2), (-5,1), (-4,0), (-2,1), (-1,0), (0,-3), 
    (-1,-4), (1,-4), (2,-3), (1,-2), (3,-1), (5,1)
]

def add(*vectors):
    return (sum([v[0] for v  in vectors]), sum([v[1] for v  in vectors]))




def translate(translate, vectors):
        result =[];
        for i in vectors:
           result.append(add((2,2),i))

        return result




def length(v1):
   return  sqrt(v1[0]**2 + v1[1] **2)

#dino_vectors2 = [(0,0), add(dino_vectors)  ]

lets = translate((1,1), dino_vectors)
print(lets)

draw(
    Points(*dino_vectors),
    Polygon(*dino_vectors),
   # Polygon(*dino_vectors2),
    #Points(*[(x,x**2) for x in range(-10,11)]),
    #grid=(1,10),
   # nice_aspect_ratio=False
    Polygon(*lets),
 Points((2,2), (-1,3)),
    Segment((2,2), (-1,3), color=red)

)

