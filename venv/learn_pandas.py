import pandas as pd
import numpy as np


def one():
    groceries = pd.Series(data=[30, 4, 'Yes', 'No'], index=['eggs', 'apples', 'milk', 'bread'])
    print(groceries)
    print(groceries.shape)
    print(groceries.ndim)
    print(groceries.size)
    print(groceries.index)
    print(groceries.values)


def two():
    groceries = pd.Series(data=[30, 4, 'Yes', 'No'], index=['eggs', 'apples', 'milk', 'bread'])
    print(groceries)
    print(groceries[['milk', 'bread']])
    print(groceries[0])
    print(groceries[[0, 1]])
    print(groceries.loc[['eggs', 'milk']])
    # print(groceries.iloc[['eggs', 'apples']])
    groceries.drop("apples", inplace=True)
    print(groceries)


def three():
    fruits = pd.Series([10, 4, 3], ["apples", "oranges", "bananas"])
    groceries = pd.Series(data=[30, 4, 'Yes', 'No'], index=['eggs', 'apples', 'milk', 'bread'])
    print(fruits - 2)
    print(fruits + 2)
    print(fruits * 2)
    print(fruits % 2)
    print(fruits * 2)
    print(np.sqrt(fruits))
    print(np.exp(fruits))
    print(np.power(fruits, 2))
    print(fruits['bananas'] + 3)
    print(fruits.iloc[0] - 2)
    print(fruits[["apples", "oranges"]] * 4)
    print(groceries * 2)


def four():
    items = {
        "Bob": pd.Series((245, 45, 34), index=["bike", "pants", "watch"]),
        "Alice": pd.Series((40, 100, 500, 45), index=["book", "glasses", "bike", "pants"])
    }
    cart = pd.DataFrame(items)
    print(cart)
    print(cart.index)
    print(cart.shape)
    print(cart.size)
    print(pd.DataFrame(items, columns=["Bob"]))
    print(pd.DataFrame(items, index=["pants", "book"]))
    cart["shirt"] = [1, 2, 4, 5, 6]
    print(cart)
    new = [{"bikes": 20, "pants": 30, "watches": 45, "glasses": 4}]
    new_Store = pd.DataFrame(new, index=["store 3"])
    cart.append(new_Store)
    print(cart)


four()
