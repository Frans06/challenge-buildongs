from typing import List, Callable

def silhouette_extractor(buildings: List[list]) -> List[list]:
  # Silhouette extractor generates range functions for each building and then
  # aggregates all building functions. At the last, It detects height changes in order to
  # gets coordinates.
  silhouette = []
  silhouette_func = generate_silhouette_func(buildings)
  # Range of generation silhouettes
  min_range = min([i for i in zip(*buildings)][0])
  max_range = max([i for i in zip(*buildings)][1])
  # Defaul value to 0 height
  prev = 0
  # Itterating over the silhouettes buildings and detect changes in height
  for i in range(min_range, max_range + 2):
    if prev != silhouette_func(i):
      silhouette.append([i, silhouette_func(i)])
      prev = silhouette_func(i)
  return silhouette


def function_creator(x1: int, x2: int, y: int) -> Callable[[int], int]:
  # This function implements a range function on [x1, x2> = y
  return lambda x: y if x1 <= x <  x2 else 0


def function_aggregate(function1: Callable[[int], int], function2: Callable[[int], int]):
  # This function aggregate 2 range functions and return a new function 
  return lambda x: max(function1(x), function2(x))


def generate_silhouette_func(params: List[list]):
  # This function generate the silhouette function from the aggregation of all range functions 
  silhouette_function = lambda x: 0 
  for param in params:
    silhouette_function = function_aggregate(silhouette_function,function_creator(*param))
  return silhouette_function

