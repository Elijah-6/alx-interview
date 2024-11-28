# Making Change

This project contains a Python script that determines the fewest number of coins needed to meet a given amount of money (`total`) when given a pile of coins of different values.

## File

- `0-making_change.py`: Contains the `makeChange` function.

## Function

### `makeChange(coins, total)`

This function calculates the minimum number of coins required to make up a given amount (`total`). If the amount cannot be met by any combination of the coins, it returns `-1`.

#### Parameters

- `coins` (list): A list of the values of the coins in your possession.
- `total` (int): The total amount of money to make change for.

#### Returns

- `int`: The fewest number of coins needed to make the change, or `-1` if it is not possible.

#### Example

```python
print(makeChange([1, 2, 5], 11))  # Output: 3 (5 + 5 + 1)
print(makeChange([2], 3))         # Output: -1
```

## Usage

To use the `makeChange` function, simply import it into your Python script and call it with the appropriate arguments.

```python
from 0-making_change import makeChange

coins = [1, 2, 5]
total = 11
print(makeChange(coins, total))  # Output: 3
```

## License

This project is licensed under the MIT License.