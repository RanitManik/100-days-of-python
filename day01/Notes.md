> # Notes

### Table of Contents

1. [The "len()" Function](#The-"len()"-Function)
2. [String Concatenation](#String-Concatenation)

## The "len()" Function

In Python, the `len()` function is used to get the length or the number of items in a sequence (like a string, list,
tuple, etc.). Here's how you use it:

```python
# Example with a string
my_string = "Hello, World!"
length_of_string = len(my_string)
print(length_of_string)  # Output: 13

# Example with a list
my_list = [1, 2, 3, 4, 5]
length_of_list = len(my_list)
print(length_of_list)  # Output: 5
```

In the first example, `len()` is used to find the length of a string, which is 13 characters. In the second example,
it's used to find the length of a list, which contains 5 elements.

---

## String Concatenation

String concatenation is the process of combining or joining two or more strings together to create a new string. In
Python, there are several ways to perform string concatenation.

1. **Using the `+` Operator**:

   You can use the `+` operator to concatenate strings. Here's an example:

   ```python
   str1 = "Hello, "
   str2 = "World!"
   result = str1 + str2
   print(result)  # Output: Hello, World!
   ```

   In this example, `str1` and `str2` are concatenated to form a new string `result`.


2. **Using the `str.join()` Method**:

   The `join()` method is used to concatenate a list of strings. It takes a list of strings as an argument and joins
   them with the string on which it's called. Here's an example:

   ```python
   words = ["Hello", "World"]
   result = " ".join(words)
   print(result)  # Output: Hello World
   ```

   In this example, the elements of the `words` list are joined with a space in between.


3. **Using f-strings (Formatted String Literals)**:

   With f-strings, you can embed expressions inside string literals, including variables. This allows for easy string
   interpolation and concatenation. Here's an example:

   ```python
   name = "Alice"
   greeting = f"Hello, {name}!"
   print(greeting)  # Output: Hello, Alice!
   ```

   In this example, the variable `name` is interpolated into the string using an f-string.


4. **Using `str.format()`**:

   The `str.format()` method allows you to embed expressions inside strings. It's similar to f-strings but is used in
   older versions of Python (prior to Python 3.6). Here's an example:

   ```python
   name = "Bob"
   greeting = "Hello, {}!".format(name)
   print(greeting)  # Output: Hello, Bob!
   ```

   In this example, the curly braces `{}` are used as placeholders for the value of `name`.


5. **Using `+=` Operator**:

   You can also use the `+=` operator to concatenate strings in-place. This is a shorthand way of combining strings.
   Here's an example:

   ```python
   str1 = "Hello, "
   str2 = "World!"
   str1 += str2
   print(str1)  # Output: Hello, World!
   ```

   In this example, `str1` is modified to contain the concatenated result.

String concatenation is a fundamental operation in programming, and it's used extensively in various applications, such
as building user interfaces, processing text data, and generating output messages.

---


