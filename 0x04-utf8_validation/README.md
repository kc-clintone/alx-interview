# UTF-8 Validation

## Overview

This Python script provides a function called `validUTF8(data)` that determines whether a given dataset represents a valid UTF-8 encoding. UTF-8 is a variable-width character encoding used for electronic communication. This function checks whether the provided data conforms to the UTF-8 encoding standard, which specifies how many bytes each character can have and how those bytes should be structured.

## Function Prototype

```python
def validUTF8(data)
```

### Parameters

- **`data`**: A list of integers where each integer represents one byte of data (i.e., only the 8 least significant bits are considered). This dataset can contain multiple characters, with each character being between 1 and 4 bytes long.

### Returns

- **`True`**: If the data represents a valid UTF-8 encoding.
- **`False`**: If the data does not represent a valid UTF-8 encoding.

## How It Works

The function follows these key steps:

1. **Byte Identification**:
    - The function iterates through the list of bytes (integers).
    - It identifies the start of a new character by examining the leading bits of each byte.
    - It determines how many bytes the character should contain based on the pattern of leading bits.

2. **Validation**:
    - The function ensures that continuation bytes follow the rules, specifically that they start with `10` (`10xxxxxx`).
    - If any byte does not conform to the expected pattern, the function returns `False`.

3. **Final Check**:
    - After processing all bytes, the function checks if any multi-byte characters were incomplete. If so, it returns `False`; otherwise, it returns `True`.

### UTF-8 Encoding Rules Recap

- **1-byte character**: `0xxxxxxx`
- **2-byte character**: `110xxxxx 10xxxxxx`
- **3-byte character**: `1110xxxx 10xxxxxx 10xxxxxx`
- **4-byte character**: `11110xxx 10xxxxxx 10xxxxxx 10xxxxxx`

## Example Usage

```python
# Valid UTF-8 encoding
print(validUTF8([197, 130, 1]))  # Output: True

# Invalid UTF-8 encoding
print(validUTF8([235, 140, 4]))  # Output: False
```

### Explanation of Example:

1. **`[197, 130, 1]`**:
    - The first byte `197` (`11000101`) indicates the start of a 2-byte character.
    - The next byte `130` (`10000010`) is a valid continuation byte.
    - The final byte `1` (`00000001`) is a valid 1-byte character.
    - Since all bytes are correctly formatted, the function returns `True`.

2. **`[235, 140, 4]`**:
    - The first byte `235` (`11101011`) indicates the start of a 3-byte character.
    - The next byte `140` (`10001100`) is a valid continuation byte.
    - However, the final byte `4` (`00000100`) is not a valid continuation byte, making the sequence invalid.
    - Therefore, the function returns `False`.

## Conclusion

This `validUTF8` function is a handy tool for checking if a list of integers (representing bytes) conforms to UTF-8 encoding standards. It's useful for validating data that should be UTF-8 encoded, ensuring that it will be correctly interpreted and displayed by systems that expect UTF-8 encoded text.
