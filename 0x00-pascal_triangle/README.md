# Pascal's Triangle

This project contains a Python script that generates Pascal's Triangle.

## File

- `0-pascal_triangle.py`: This script contains a function `pascal_triangle(n)` that returns a list of lists of integers representing Pascal's Triangle of size `n`.

## Usage

To use the `pascal_triangle` function, you can import it into your Python script and call it with the desired size of the triangle.

```python
from 0-pascal_triangle import pascal_triangle

n = 5
triangle = pascal_triangle(n)
for row in triangle:
    print(row)
```

## Example

For `n = 5`, the output will be:

```  none
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
```

## License

This project is licensed under the MIT License.
