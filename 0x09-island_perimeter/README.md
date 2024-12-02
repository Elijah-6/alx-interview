# Island Perimeter

This project contains a Python function to calculate the perimeter of an island represented by 1s in a grid of 0s and 1s.

## Function

### `island_perimeter(grid)`

#### Description

The `island_perimeter` function calculates the perimeter of an island in a grid. The grid is a 2D list where `1` represents land and `0` represents water. The function iterates through each cell in the grid and checks its four neighbors (top, bottom, left, right). If a neighbor is water or the cell is on the boundary of the grid, it contributes to the perimeter.

#### Parameters

- `grid` (List[List[int]]): A 2D list representing the grid where `1`s are land and `0`s are water.

#### Returns

- `int`: The perimeter of the island.

#### Example

```python
grid = [
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0]
]
print(island_perimeter(grid))  # Output: 16
```

## Usage

To use the `island_perimeter` function, import it into your Python script and pass a 2D list representing the grid as an argument.

```python
from island_perimeter import island_perimeter

grid = [
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0]
]
print(island_perimeter(grid))  # Output: 16
```

## License

This project is licensed under the MIT License.