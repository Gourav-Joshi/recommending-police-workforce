import math

def find_dict(x,y) :
    calculate = abs(x[0]-y[0])**2 +abs (x[1]-y[1])**2
    distance = math.sqrt(calculate)
    return distance

def update_centroid(centroid , data) :
    centroid[0] = (centroid[0] + data[0])/2
    centroid[1] = (centroid[1] + data[1])/2

def main() :
    data = {"A": [185, 72], "B": [170, 56], "C": [168, 60], "D": [179, 68], "E": [182, 72]}
    centroid = [[185, 72], [170, 56]]
    cluster = dict.fromkeys(data.keys())
    for i in data:
        distance_from_cluster1 = find_dict(centroid[0],data[i])
        distance_from_cluster2 = find_dict(centroid[1],data[i])
        if distance_from_cluster1 > distance_from_cluster2 :
            cluster[i] = 2
            update_centroid(centroid[1],data[i])
        elif distance_from_cluster1 < distance_from_cluster2 :
            cluster[i] = 1
            update_centroid(centroid[0],data[i])
    print(cluster)
    print(centroid)

if __name__ == "__main__":
    main()