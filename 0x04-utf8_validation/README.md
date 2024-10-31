# UTF-8 Validation

## Description

This project involves creating a Python script to validate whether a given data set represents a valid UTF-8 encoding. UTF-8 is a variable-width character encoding used for electronic communication. The script will ensure that the data adheres to the UTF-8 encoding rules.

## Requirements

- Python 3.x

## Files

- `0-validate_utf8.py`: The main script that contains the function to validate UTF-8 encoding.

## Usage

To use the UTF-8 validation script, run the following command:

```bash
python3 0-validate_utf8.py
```

## Function

### `validUTF8(data)`

This function takes a list of integers and returns `True` if the data set represents a valid UTF-8 encoding, otherwise returns `False`.

#### Parameters

- `data` (list): A list of integers representing the data set to be validated.

#### Returns

- `bool`: `True` if the data set is valid UTF-8, `False` otherwise.

## Example

```python
data = [197, 130, 1]
print(validUTF8(data))  # Output: True

data = [235, 140, 4]
print(validUTF8(data))  # Output: False
```

## Explanation

The provided code snippet is part of a function that validates whether a given list of integers represents a valid UTF-8 encoded sequence. UTF-8 encoding uses one to four bytes for each character, and the number of bytes used is indicated by the leading bits of the first byte in each sequence.

The code begins by defining two masks, `mask1` and `mask2`, which are used to check the most significant bits of each byte. `mask1` is set to `1 << 7` (which is 128 in decimal, or `10000000` in binary), and `mask2` is set to `1 << 6` (which is 64 in decimal, or `01000000` in binary).

The main part of the code is a loop that iterates over each integer in the `data` list. For each integer, it initializes a `mask` variable to `1 << 7` to check the most significant bit. If `num_bytes` is zero, it means the current byte is the start of a new UTF-8 character. The code then counts the number of leading 1's in the current byte by shifting the `mask` to the right and incrementing `num_bytes` for each leading 1 found. This count determines how many bytes the current UTF-8 character spans.

If `num_bytes` is zero after counting the leading 1's, it indicates a 1-byte character, and the loop continues to the next byte. If `num_bytes` is 1 or greater than 4, it indicates an invalid UTF-8 sequence, and the function returns `False`.

If `num_bytes` is not zero, the code checks that the subsequent bytes in the sequence start with the bits `10` (which is required for continuation bytes in UTF-8). This is done using the `mask1` and `mask2` masks. If the check fails, the function returns `False`.

Finally, `num_bytes` is decremented by 1 to account for the current byte, and the loop continues to the next byte in the `data` list. This process ensures that each byte in the sequence conforms to the UTF-8 encoding rules.

## Author

Elijah

## License

This project is licensed under the MIT License.
