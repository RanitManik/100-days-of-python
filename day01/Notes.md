> # Notes

### Table of Contents

1. [length checking in python](#length-checking-in-python)
2. [concatenation](#concatenation)
3. [String Concatenation](#String-Concatenation)

---

<<<<<<< HEAD
## length checking in python
=======
## The "len()" Function
>>>>>>> 0da6e475124b7a55c5f6fd993367d3096fe15e7f

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

## concatenation

Concatenation in Python refers to the process of combining two or more strings, lists, or other sequences into a single
sequence. The `+` operator is commonly used for concatenation in Python.

Here are examples of concatenation with different data types:

1. **String Concatenation**:

   You can use the `+` operator to concatenate strings together.

   ```python
   str1 = "Hello, "
   str2 = "World!"
   result = str1 + str2
   print(result)  # Output: Hello, World!
   ```

2. **List Concatenation**:

   You can use the `+` operator to concatenate lists.

   ```python
   list1 = [1, 2, 3]
   list2 = [4, 5, 6]
   result = list1 + list2
   print(result)  # Output: [1, 2, 3, 4, 5, 6]
   ```

   Additionally, you can use the `extend()` method or the `+=` operator to concatenate lists.

   ```python
   list1.extend(list2)
   print(list1)  # Output: [1, 2, 3, 4, 5, 6]

   # or

   list1 += list2
   print(list1)  # Output: [1, 2, 3, 4, 5, 6]
   ```

3. **Tuple Concatenation**:

   While tuples are immutable and cannot be changed, you can create a new tuple by concatenating existing tuples.

   ```python
   tuple1 = (1, 2, 3)
   tuple2 = (4, 5, 6)
   result = tuple1 + tuple2
   print(result)  # Output: (1, 2, 3, 4, 5, 6)
   ```

4. **String and Number Concatenation**:

   When you want to concatenate a string with a number, you'll need to convert the number to a string first
   using `str()`.

   ```python
   str1 = "The answer is "
   num = 42
   result = str1 + str(num)
   print(result)  # Output: The answer is 42
   ```

5. **Using `join()` for Strings**:

   The `join()` method is a powerful way to concatenate a sequence of strings.

   ```python
   words = ["Hello", "World", "!"]
   result = " ".join(words)
   print(result)  # Output: Hello World !
   ```

Remember that concatenation creates a new object and does not modify the original sequences. It's important to be
mindful of performance, especially when dealing with large strings or lists. In such cases, using methods like `join()`
can be more efficient than repeated `+` operations.

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


