# Challenge Story

A city’s skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Now suppose you are given the locations and height of all the buildings as shown on a cityscape photo (Input), write a program to output the skyline formed by these buildings collectively (Output)
Input:
[Li, Ri, Hi] = where Li and Ri are the x coordinates of the left and right edge of the ith building and Hi is the height. Assume that all the buildings are perfect rectangles grounded on an absolutely flat surface at height 0.
Could we add an example?
Output:
List of key points (red dots in the output figure) in the format of [ [x1,y1], [x2,y2] ] that uniquely defines a skyline. A key point is the left endpoint of a horizontal line segment.
Keep in mind:
The output list must be sorted by the X position and there must be no consecutive horizontal lines of equal height in the output skyline.


### Install Enviroment
Needs pip installed with python 3.65 or above
  ``` bash
  git clone git@github.com:Frans06/challenge-buildongs.git
  pip install pipenv
  pipenv install
  pipenv shell
  ```

### Running tests
  ``` bash
  python -m test-challenge
  ```