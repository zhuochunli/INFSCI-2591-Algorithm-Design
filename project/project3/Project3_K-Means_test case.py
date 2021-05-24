import numpy as np
import pandas as pd
import math
import random
_ = inf = 999999  # inf


def euclDistance(point1, point2):
    dimension = len(point1)
    sum = 0.0
    for i in range(dimension):
        sum = sum+(point1[i]-point2[i])**2
    return math.sqrt(sum)


def kmeans(dataset, k, max_iteration):
    n = len(dataset)
    centroid = []  # the coordinates of each centroid
    belong_to = [-1]*n  # the centroid number each point belongs to
    loss = []  # store the losses after each iterating
    clusterChanged = True
    # init centroid
    index = random.sample(list(range(n)), k)
    for i in index:
        centroid.append(dataset[i])
    # start k-means
    epoch = 0  # the current epoch of clustering
    while clusterChanged and epoch < max_iteration:  # when cluster doesn't change or reaches the max iteration, stop
        clusterChanged = False
        tmp_loss = 0  # the loss after each epoch
        # for each point, find their closest centroid
        for p in range(n):  # each point
            min_dist = inf
            closest_centroid = 0
            for c in range(k):  # calculate the closest centroid
                tmp_dist = euclDistance(dataset[p], centroid[c])
                if tmp_dist < min_dist:
                    min_dist = tmp_dist
                    closest_centroid = c
            if belong_to[p] != closest_centroid:  # assign the closest centroid to each point
                belong_to[p] = closest_centroid
                clusterChanged = True
        # update centroids using k-means of points in each cluster
        for c in range(k):
            tmp_c = []
            for point_index, belong in enumerate(belong_to):
                if belong == c:
                    tmp_c.append(dataset[point_index])
            centroid[c] = np.mean(tmp_c, axis=0)
        # calculate loss
        for point_index in range(n):
            tmp_loss = tmp_loss+euclDistance(dataset[point_index], centroid[belong_to[point_index]])**2
        tmp_loss = tmp_loss/n
        loss.append(tmp_loss)
        epoch = epoch + 1
        print('After the {}th iteration, the loss is:'.format(epoch), tmp_loss)

    return centroid, belong_to, loss


if __name__ == '__main__':
    data = pd.read_csv('E:/学习资料/Pitt/algorithm/project/project3/Project3_Test_Case.csv')
    dataset = []
    for i in range(len(data)):
        dataset.append([float(data['X1'].values[i]), float(data['X2'].values[i])])
    centroid, belong_to, loss = kmeans(dataset, 2, 50)
    for c_index, centroid in enumerate(centroid):
        print('The coordinates of centroid {}:'.format(c_index+1), centroid)
        print(belong_to.count(c_index), 'points are assigned to centroid', c_index+1)