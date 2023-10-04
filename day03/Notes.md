> # Notes

### Table of Contents

1. [Count Function](#count-function)
2. [Using length Function in a String](#Using-length-Function-in-a-String)

---

## count Method

In Python, the `count()` function is used to count the number of occurrences of a specific element in a list,
tuple, or any other iterable object.

Here's the basic syntax of the `count()` function:

```python
iterable.count(element)
```

- `iterable`: This is the iterable (e.g., list, tuple, etc.) in which you want to count occurrences of an element.
- `element`: This is the element you want to count.

For example, let's say you have a list of numbers:

```python
numbers = [1, 2, 3, 4, 2, 2, 3, 5, 2]
```

If you want to count how many times the number `2` appears in this list, you would use the `count()` function like this:

```python
count_of_twos = numbers.count(2)
```

After executing this code, `count_of_twos` will be equal to `4` because `2` appears four times in the list.

Keep in mind that if the element is not present in the iterable, `count()` will return `0`.

Additionally, it's worth noting that `count()` is a method specific to lists, tuples, and some other iterable types. Not
all objects support this method.

---

## Using length Function in a String

in Python, you can use the `len()` function to get the length of a string. Here's an example:

```python
my_string = "Hello, World!"
length = len(my_string)

print(length)  # This will print the length of the string (in this case, 13)
```

In this example, `my_string` is the string you want to find the length of. The `len()` function is used to determine how many characters are in the string, and the result is stored in the variable `length`. Finally, `print(length)` will display the length of the string.

---