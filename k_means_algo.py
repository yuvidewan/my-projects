import matplotlib.pyplot as plt

main_l = [[185,72],[170,56],[168,60],[179,68],[182,72],[188,77],[180,71],[180,70],[183,84],[180,88],[180,67],[177,76]]
k1 = [main_l[0]]
k2 = [main_l[1]]

k1_centroid = k1[0] #initialise centroids of clusters with initial values
k2_centroid = k2[0]

def calc_centroid():
    global k1_centroid,k2_centroid
    #calculate for k1
    xval = 0
    yval = 0
    n = len(k1)
    for i in k1:
        xval += i[0]
        yval += i[1]
    
    xval /= n
    yval /= n
    k1_centroid = [xval,yval]

    #calculate for k2
    xval = 0
    yval = 0
    n = len(k2)
    for i in k2:
        xval += i[0]
        yval += i[1]
    
    xval /= n
    yval /= n
    k2_centroid = [xval,yval]


def calc_distance(l):
    d1 = ((k1_centroid[0] - l[0])**2 + (k1_centroid[1] - l[1])**2)**(1/2)
    d2 = ((k2_centroid[0] - l[0])**2 + (k2_centroid[1] - l[1])**2)**(1/2)

    if(d1 < d2):
        return 1 # k1 cluster should be used
    else:
        return 0 # k2 cluster should be used

for i in range(2,len(main_l)):
    value = calc_distance(main_l[i])
    if(value == 1):#decide cluster and append lists
        k1.append(main_l[i])
    else:
        k2.append(main_l[i])
    
    calc_centroid()
print("points in K1 - ")
for i in k1:
    print(i,end=" ")

print("\npoints in K2 - ")   
for i in k2:
    print(i,end=" ")

# Unpack k1 and k2 into x and y
k1_x, k1_y = zip(*k1)
k2_x, k2_y = zip(*k2)

# Plot both clusters
plt.scatter(k1_x, k1_y, color='red', label='Cluster 1')
plt.scatter(k2_x, k2_y, color='blue', label='Cluster 2')

# Show plot
plt.legend()
plt.show()
