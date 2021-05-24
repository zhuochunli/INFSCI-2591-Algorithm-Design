def robot(remain_dist):
    if promising(steps, remain_dist):
        if remain_dist == 0:
            result.append(steps[:])
        else:
            for x in range(1, 4):
                steps.append(x)
                robot(remain_dist-x)
                steps.pop()


def promising(steps, remain_dist):
    if remain_dist < 0:
        return False
    for i in range(len(steps)-1):
        if steps[i] > steps[i+1]:
            return False
    return True


if __name__ == "__main__":
    num = [1, 2, 3, 4, 5]
    for n in num:
        steps = []
        result = []
        robot(n)
        print(result)