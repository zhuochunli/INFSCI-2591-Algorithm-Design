import time
import matplotlib.pyplot as plt
import numpy as np

def bin(n,k):
    if k==0 or n==k:
        return 1
    else:
        return bin(n-1,k-1)+bin(n-1,k)


def bin2(n,k):
    b=[[0]*(k+1) for x in range(n+1)]
    for i in range(n+1):
        for j in range(min(i,k)+1):
            if j==0 or j==i:
                b[i][j]=1
            else:
                b[i][j]=b[i-1][j-1]+b[i-1][j]
    return b[n][k]

def plot(x,y):
    x1 = np.array(x)
    y1 = np.array(y)
    # plt.plot(x1, y1, 'ro-')
    plt.plot(x1,y1,'r')
    plt.title('The relationship of Time and K in Algorithm 3.2')
    plt.xlabel('K')
    plt.ylabel('Time')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    t=[]
    for k in range(0,151):
        start = time.process_time()
        bin2(300,k)
        end = time.process_time()
        re=end-start
        t.append('%.4f' % re)
        print(k)
    t=t+t[len(t)-2::-1]
    plot(range(0,301),t)