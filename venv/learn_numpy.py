import numpy as np
import time


def first():
    x = np.array([1, 2, 3, 4, 5])
    print(x)
    print(type(x))
    print(x.dtype)
    print(x.shape)
    y = np.array([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]])
    print(y.size)
    z = np.array(["Hello", "Josteve"])
    print(z)
    print(type(z))
    print(z.dtype)
    k = np.array(["Josteve", 1, 2.3])
    print(k)
    k = np.array([1, 1, 2.3])
    print(k, k.dtype)
    p = np.array([3.4, 5.6], dtype=np.int64)
    print(p)
    np.save("my_array", x)
    y = np.load("my_array.npy")
    print(y)


def second():
    x = np.arange(25).reshape(5, 5)
    x[x <= 10] = -1
    print(x)

    x = np.array([1, 2, 3, 4, 5])
    y = np.array([6, 7, 8, 9, 1])

    print(np.intersect1d(x, y))
    print(np.setdiff1d(x, y))

    print(np.union1d(x, y))

    print(np.sort(np.unique(np.array([4, 5, 3, 4, 2, 1]))))
    print(np.sort(np.array([[4, 5, 3, 4, 2, 1], [4, 5, 3, 4, 2, 1]]), axis=1))


def third():
    n = np.zeros((3, 4), dtype=int)
    print(n)
    k = np.ones((3, 3))
    print(k)
    x = np.full((3, 3), 9)
    print(x)
    x = np.eye(3)
    print(x)
    x = np.diag([10, 20, 30])
    print(x)
    x = np.arange(10)
    print(x)
    x = np.arange(10, 15)
    print(x)
    x = np.arange(10, 15, 2)
    print(x)
    x = np.linspace(1, 3, 10)
    x = np.arange(10)
    x = np.reshape(x, (5, 2))
    print(x)
    x = np.random.random((4, 3))
    print(x)
    x = np.random.randint(4, 15, (3, 3))
    print(x)
    x = np.random.normal(0, 0.1, size=(1000, 1000))
    print(x)


def fourth():
    x = np.array([1, 2, 3, 4, 5])
    print(x)
    x[3] = 0
    print(x)
    x = np.arange(1, 7).reshape(3, 2)
    x[0, 0] = 10
    print(x)
    x = np.array([1, 2, 3, 4, 5])
    x = np.append(x, [7, 8])
    print(x)
    y = np.arange(1, 10).reshape(3, 3)
    print(y)
    # row
    y = np.append(y, [[6, 7, 4]], axis=0)
    print(y)
    # column
    y = np.append(y, [[6], [7], [4], [6]], axis=1)
    print(y)
    x = np.arange(7)
    print(x)
    x = np.insert(x, 1, 2)
    print(x)
    y = np.insert(y, 1, [4, 3, 2, 3], axis=0)
    print(y)
    y = np.insert(y, 1, 5, axis=1)
    print(y)
    j = np.array([1, 2, 3])
    k = np.array([3, 2, 1])
    x = np.hstack((j, k))
    print(x)


def fifth():
    x = np.arange(1, 21).reshape(4, 5)
    # First is row, second is column
    x = x[1:4, 2: 5]
    print(x[1:, 1:])
    print(x)

def last():
    #do the last part abeg
    pass


fifth()
