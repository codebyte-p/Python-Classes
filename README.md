# Python Classes

Practice programs from my Python learning sessions.

## Files

### `firstprogram.py`
Variables, user input, and string formatting.
- Multiple assignment in one line with `input()` and type casting (`int`, `str`)
- Four ways to build strings: concatenation (`+`), f-strings, `%` formatting, and `str.format()`
- Single-line and multi-line comments
- Why casting matters: adding two `input()` values joins them as text (`"2" + "3"` → `"23"`), while adding `int` values does arithmetic (`2 + 3` → `5`)

### `boolean.py`
Logical operators, truthiness, and character codes.
- `or` returns the first truthy value, `and` returns the first falsy value (or the last value)
- `not` and `bool()` for truthiness
- `ord()` converts a character to its Unicode code, `chr()` does the reverse

## Running

Requires Python 3.

```bash
python firstprogram.py
python boolean.py
```
