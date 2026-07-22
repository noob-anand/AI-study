import numpy as np

# making 2-D arr of 25 elements with 5 rows and 5 columns
img = np.arange(25).reshape(5, 5)
print(img)
print()

print(img[1:-1 ,1:-1])  # center
print()

print(img[ :-2 ,1:-1])  # top
print()

print(img[2:   ,1:-1])  # bottom
print()

print(img[1:-1 , :-2])  # left
print()

print(img[1:-1 ,2:  ])  # right
print()

avg_img =(img[1:-1 ,1:-1]  # center
        + img[ :-2 ,1:-1]  # top
        + img[2:   ,1:-1]  # bottom
        + img[1:-1 , :-2]  # left
        + img[1:-1 ,2:  ]  # right
     )/5.0
print(avg_img)