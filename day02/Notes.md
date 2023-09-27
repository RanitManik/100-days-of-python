> # Notes

### Table of Contents

1. [uses of Underscore_](#uses-of-Underscore_)
2. [Type casting](#Type-casting)
3. [Type checking](#Type-checking)
4. [subscripting](#subscripting)
5. [operators](operators)
6. [PEMDASLR rule](PEMDASLR-rule)
7. [string is default datatype](string-is-default-datatype)
8. [round function](#round-function)
9. [f-String(f-String)]

---

## uses of Underscore_

the underscore character (`_`) serves a few specific purposes, and its use in a print statement can have a couple of
different meanings depending on the context.

1. **As a Placeholder for Unused Values**:

   The underscore can be used as a placeholder for a value that you don't intend to use. This is commonly seen when
   unpacking values from an iterable where you're only interested in certain elements.

   For example:

   ```python
   first_name, last_name, _ = ("John", "Doe", 30)
   print(f"Name: {first_name} {last_name}")
   ```

   In this example, we're unpacking a tuple, but we're only interested in the first two elements. The third element,
   which is the age, is assigned to `_` to indicate that we're not planning to use it. This is more of a convention to
   signal to other developers that the value isn't important in this context.

2. **As a Variable Name**:

   While it's not a Python keyword, `_` can be used as a valid variable name. However, it has a special convention
   associated with it. When you see `_` being used as a variable name, it's typically meant to indicate that the value
   stored there is intended to be ignored or is a throwaway value.

   For example:

   ```python
   for _ in range(5):
       print("Hello")
   ```

   In this loop, we're iterating five times, but we don't need the index variable. Using `_` as the variable name
   signals to others reading the code that the index is not relevant in this loop.

3. **In Internationalization**:

   In the context of internationalization, `_` is commonly used as a function name for translating text to different
   languages. For example:

   ```python
   def _(text):
       # Code for translating 'text' to the appropriate language
       # ...
       return translated_text
   ```

   This is a convention often used in web development and software projects where multi-language support is needed.

4. **In Interpreter Sessions**:

   In an interactive Python session (REPL), the `_` character has a special meaning. It stores the result of the last
   expression that was evaluated. This is useful if you want to refer to the result of a computation without storing it
   in a variable.

   For example:

   ```
   >>> 2 + 2
   4
   >>> print(_)
   4
   ```

5. **visual separator**:

   In Python, you can use underscores as a visual separator for large numbers to make them more readable. This is
   particularly useful when dealing with large numerical values.

   For example, if you have a large number like `234565562`, you can use underscores to make it more readable:

   ```python
   number = 234_565_562
   ```

   This does not affect the actual value of the number; it's purely for visual clarity. The underscores are ignored by
   the
   Python interpreter. This feature was introduced in Python 3.6.

   Using underscores in this way can make it easier to read and understand large numbers, especially when dealing with
   financial data, long numerical constants, or any situation where large numbers are used frequently.

   In this example, the last result, which is `4`, is stored in `_`. When you print `_`, it prints the value.

   Overall, the use of `_` in a print statement or in Python code in general is largely about conveying meaning to other
   developers. It's a way of indicating that a particular value or variable is intentionally being disregarded or isn't
   relevant in a given context.

---

## Type checking

In Python, type checking refers to the process of verifying the data type of a variable or value. This can be done using
various methods to ensure that the data you're working with is of the expected type. Here are some common ways to
perform type checking in Python:

1. **Using the `type()` Function**:

   The `type()` function allows you to determine the type of an object. It returns the type as a class object.

   ```python
   x = 42
   print(type(x))  # Output: <class 'int'>
   ```

2. **Using `isinstance()` Function**:

   The `isinstance()` function checks if an object belongs to a specific type or class. It can also handle inheritance.

   ```python
   x = 42
   print(isinstance(x, int))  # Output: True
   ```

3. **Using `type` Comparisons**:

   You can directly compare the type of an object with a known type.

   ```python
   x = 42
   print(type(x) == int)  # Output: True
   ```

4. **Using `assert` Statements**:

   The `assert` statement is a useful way to perform type checking, especially in testing scenarios. It raises an error
   if the condition is False.

   ```python
   x = 42
   assert isinstance(x, int), "x should be an integer"
   ```

5. **Using `Duck Typing`**:

   In Python, there's a saying: "If it walks like a duck and quacks like a duck, then it must be a duck." This means
   that Python doesn't require explicit type declarations. If an object supports the methods or attributes you expect,
   you can often work with it regardless of its actual type.

   ```python
   def print_length(obj):
       print(len(obj))

   my_list = [1, 2, 3]
   my_string = "hello"

   print_length(my_list)  # Output: 3
   print_length(my_string)  # Output: 5
   ```

6. **Using `__annotations__`**:

   You can use annotations to indicate the expected type of a function's arguments or return value. This is a form of
   documentation and doesn't enforce type checking at runtime by default. However, you can use tools like `mypy` to
   perform static type checking.

   ```python
   def greet(name: str) -> str:
       return f"Hello, {name}!"

   message = greet("Alice")
   ```

7. **Using `try` and `except`**:

   You can use try-except blocks to catch type errors. This can be useful when you expect that a specific operation may
   fail due to incompatible types.

   ```python
   try:
       result = "42" + 10  # This will raise a TypeError
   except TypeError as e:
       print(f"Error: {e}")
   ```

Remember that Python is a dynamically typed language, meaning that variables can hold values of any type, and their
types can change during runtime. However, it's good practice to perform type checking when necessary to ensure that your
code behaves as expected.

---

## Type casting

Type casting in Python refers to the process of converting a value from one data type to another. This can be useful
when you want to perform operations that require compatible data types, or when you want to represent data in a
different format.

Here are some common types of type casting in Python:

1. **int()**: This function is used to convert a value to an integer data type.

   ```python
   num_str = "42"
   num_int = int(num_str)
   ```

2. **float()**: This function is used to convert a value to a floating-point data type.

   ```python
   num_str = "3.14"
   num_float = float(num_str)
   ```

3. **str()**: This function is used to convert a value to a string data type.

   ```python
   num = 42
   num_str = str(num)
   ```

4. **bool()**: This function is used to convert a value to a boolean data type. In Python, any non-zero numeric value or
   non-empty container is considered `True`, while zero or empty containers are considered `False`.

   ```python
   num = 42
   is_true = bool(num)  # This will be True
   ```

5. **list()**, **tuple()**, **set()**: These functions are used to convert a value to a list, tuple, or set data type,
   respectively.

   ```python
   my_string = "hello"
   my_list = list(my_string)  # Converts the string to a list of characters
   ```

   ```python
   my_list = [1, 2, 3]
   my_tuple = tuple(my_list)  # Converts the list to a tuple
   ```

6. **dict()**: This function is used to convert a value to a dictionary data type.

   ```python
   key_value_pairs = [("a", 1), ("b", 2)]
   my_dict = dict(key_value_pairs)
   ```

7. **ord()** and **chr()**: These functions are used to convert characters to their ASCII values and vice versa.

   ```python
   char = 'A'
   ascii_value = ord(char)  # Converts 'A' to 65
   ```

   ```python
   ascii_value = 65
   char = chr(ascii_value)  # Converts 65 to 'A'
   ```

8. **complex()**: This function is used to convert a value to a complex number.

   ```python
   num = 3
   complex_num = complex(num, 4)  # Creates a complex number with real part 3 and imaginary part 4
   ```

It's important to note that not all type castings are valid or meaningful. For example, trying to convert a string that
doesn't represent a valid number to an integer will result in an error. Always ensure that the conversion makes sense in
the context of your program.

---

# subscripting

In Python, subscripting typically refers to accessing elements or characters within a data structure like a list, tuple,
or string using square brackets `[]`. It allows you to retrieve specific items based on their position or index.

Here are some examples of subscripting in Python:

1. **Lists**:
   ```python
   my_list = [1, 2, 3, 4, 5]
   print(my_list[0])  # Output: 1 (accessing the first element)
   print(my_list[2])  # Output: 3 (accessing the third element)
   ```

2. **Strings**:
   ```python
   my_string = "Hello, World!"
   print(my_string[0])  # Output: 'H' (accessing the first character)
   print(my_string[7])  # Output: 'W' (accessing the eighth character)
   ```

3. **Tuples**:
   ```python
   my_tuple = (1, 2, 3, 4, 5)
   print(my_tuple[2])  # Output: 3 (accessing the third element)
   ```

4. **Nested Data Structures**:
   ```python
   nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
   print(nested_list[0][1])  # Output: 2 (accessing the element at row 0, column 1)
   ```

5. **Negative Indices** (to access elements from the end of a sequence):
   ```python
   my_list = [1, 2, 3, 4, 5]
   print(my_list[-1])  # Output: 5 (accessing the last element)
   ```

6. **Slicing** (a way to get a subset of elements):
   ```python
   my_list = [1, 2, 3, 4, 5]
   print(my_list[1:4])  # Output: [2, 3, 4] (accessing elements at index 1, 2, and 3)
   ```

Remember that Python uses 0-based indexing, which means that the first element in a sequence has an index of 0.

If you try to access an index that doesn't exist (e.g., an index greater than the length of the sequence), Python will
raise an `IndexError`.

Keep in mind that subscripting works on sequences, so it won't apply to all data types. For example, you can't subscript
a number or a boolean.

---

## operators

Certainly! Here's a detailed explanation for each operator:

1. **Arithmetic Operators:**
    - `+` (Addition): Adds two operands together. For example, `3 + 5` equals `8`.
    - `-` (Subtraction): Subtracts the right operand from the left operand. For example, `7 - 4` equals `3`.
    - `*` (Multiplication): Multiplies two operands. For example, `2 * 6` equals `12`.
    - `/` (Division): Divides the left operand by the right operand. For example, `8 / 2` equals `4.0` in Python 3.x (
      returns a float).
    - `%` (Modulo): Returns the remainder of the division of the left operand by the right operand. For example, `7 % 3`
      equals `1`.
    - `**` (Exponentiation): Raises the left operand to the power of the right operand. For example, `2 ** 3`
      equals `8`.
    - `//` (Floor Division): Performs division and rounds down to the nearest whole number. For example, `7 // 2`
      equals `3`.

2. **Assignment Operators:**
    - `=` (Assignment): Assigns the value of the right operand to the left operand. For example, `x = 5` assigns `5` to
      the variable `x`.
    - `+=` (Addition Assignment): Adds the right operand to the left operand and assigns the result to the left operand.
      For example, `x += 3` is equivalent to `x = x + 3`.
    - `-=` (Subtraction Assignment): Subtracts the right operand from the left operand and assigns the result to the
      left operand. For example, `x -= 2` is equivalent to `x = x - 2`.
    - `*=` (Multiplication Assignment): Multiplies the left operand by the right operand and assigns the result to the
      left operand. For example, `x *= 4` is equivalent to `x = x * 4`.
    - `/=` (Division Assignment): Divides the left operand by the right operand and assigns the result to the left
      operand. For example, `x /= 2` is equivalent to `x = x / 2`.
    - `%=` (Modulo Assignment): Performs modulo operation and assigns the result to the left operand. For
      example, `x %= 3` is equivalent to `x = x % 3`.
    - `**=` (Exponentiation Assignment): Raises the left operand to the power of the right operand and assigns the
      result to the left operand. For example, `x **= 2` is equivalent to `x = x ** 2`.
    - `//=` (Floor Division Assignment): Performs floor division and assigns the result to the left operand. For
      example, `x //= 3` is equivalent to `x = x // 3`.

3. **Comparison Operators:**
    - `==` (Equal to): Checks if the left operand is equal to the right operand. For example, `3 == 3` returns `True`.
    - `!=` (Not equal to): Checks if the left operand is not equal to the right operand. For example, `4 != 3`
      returns `True`.
    - `<` (Less than): Checks if the left operand is less than the right operand. For example, `2 < 5` returns `True`.
    - `>` (Greater than): Checks if the left operand is greater than the right operand. For example, `7 > 3`
      returns `True`.
    - `<=` (Less than or equal to): Checks if the left operand is less than or equal to the right operand. For
      example, `3 <= 3` returns `True`.
    - `>=` (Greater than or equal to): Checks if the left operand is greater than or equal to the right operand. For
      example, `5 >= 2` returns `True`.

4. **Logical Operators:**
    - `and` (Logical AND): Returns `True` if both operands are `True`. Otherwise, returns `False`. For
      example, `True and False` returns `False`.
    - `or` (Logical OR): Returns `True` if at least one of the operands is `True`. Otherwise, returns `False`. For
      example, `True or False` returns `True`.
    - `not` (Logical NOT): Returns the opposite of the operand's truth value. For example, `not True` returns `False`.

5. **Identity Operators:**
    - `is` (Identity): Returns `True` if both operands refer to the same object. For example, `x is y` returns `True`
      if `x` and `y` point to the same object in memory.
    - `is not` (Not identity): Returns `True` if both operands do not refer to the same object. For
      example, `x is not y` returns `True` if `x` and `y` do not point to the same object in memory.

6. **Membership Operators:**
    - `in` (Membership): Returns `True` if the left operand is a member of the right operand (e.g., if a value is in a
      sequence like a list). For example, `3 in [1, 2, 3]` returns `True`.
    - `not in` (Not in membership): Returns `True` if the left operand is not a member of the right operand. For
      example, `4 not in [1, 2, 3]` returns `True`.

7. **Bitwise Operators:**
    - `&` (Bitwise AND): Performs a bitwise AND operation between the binary representations of the operands.
    - `|` (Bitwise OR): Performs a bitwise OR operation between the binary representations of the operands.
    - `^` (Bitwise XOR): Performs a bitwise XOR operation between the binary representations of the operands.
    - `~` (Bitwise NOT): Inverts the binary representation of the operand.
    - `<<` (Left Shift): Shifts the binary representation of the left operand to the left by the number of positions
      specified by the right operand.
    - `>>` (Right Shift): Shifts the binary representation of the left operand to the right by the number of positions
      specified by the right operand.

These operators are fundamental tools for performing various operations in Python. Remember to use them appropriately
based on the context of your code.

---

# PEMDASLR rule

The PEMDASLR rule stands for Parentheses, Exponents, Multiplication, Division, Addition, Subtraction (from
left to right). It's an extension of the PEMDAS rule that emphasizes the importance of performing operations in order
from left to right.

Let's use the expression `2/2-2*2+2` as an example:

1. **Parentheses**:
    - There are no parentheses in this expression.

2. **Exponents**:
    - There are no exponents in this expression.

3. **Multiplication and Division (from left to right)**:
    - `2 / 2` equals 1 (since 2 divided by 2 is 1).
    - `1 - 2` equals -1 (since 1 minus 2 is -1).
    - `2 * 2` equals 4 (since 2 times 2 is 4).

4. **Addition and Subtraction (from left to right)**:
    - `-1 + 4` equals 3 (since -1 plus 4 is 3).
    - `3 + 2` equals 5 (since 3 plus 2 is 5).

So, according to the PEMDASLR rule, the final result of the expression `2/2-2*2+2` is 5.

Now, let's apply the PEMDASLR rule to the more complex expression `3 * (4 + 2) - 8 / 2^2`:

1. **Parentheses**:
    - `4 + 2` equals 6.
    - `8 / 2` equals 4.

2. **Exponents**:
    - `2^2` equals 4 (since 2 raised to the power of 2 is 4).

3. **Multiplication and Division (from left to right)**:
    - `3 * 6` equals 18.
    - `18 - 4` equals 14.

4. **Addition and Subtraction (from left to right)**:
    - `14 - 4` equals 10.

So, using the PEMDASLR rule, the final result of the expression `3 * (4 + 2) - 8 / 2^2` is 10.

---

## string is default datatype

```python
height = input("enter your height in m: ")
```

In the provided code, the variable `height` is assigned the value returned by the `input()` function. The `input()`
function always returns a string, even if the user enters a number. This is because the function treats all user input
as text.

So, regardless of whether the user enters a number or any other characters, it will be interpreted as a string. If you
want to perform mathematical operations on the input, you'll need to convert it to a numerical type (like `float`
or `int`) using functions like `float()` or `int()`.

For example:

```python
height = input("enter your height in m: ")
height = float(height)  # Convert the input to a floating-point number
```

This way, `height` will be stored as a `float` data type, allowing you to perform numerical operations on it.

---

## round function

The `round()` function in Python is used to round a number to a specified number of decimal places. It takes two
arguments: the number you want to round and the number of decimal places you want to round it to.

Here's the basic syntax:

```python
rounded_number = round(number, ndigits)
```

- `number`: This is the number you want to round.
- `ndigits`: This is the number of decimal places to which you want to round the `number`.

Here are a few examples:

```python
# Example 1
num1 = 3.14159265359
rounded_num1 = round(num1, 2)
print(rounded_num1)  # Output: 3.14

# Example 2
num2 = 2.71828
rounded_num2 = round(num2, 3)
print(rounded_num2)  # Output: 2.718

# Example 3
num3 = 5.6789
rounded_num3 = round(num3)
print(rounded_num3)  # Output: 6
```

In Example 1, `round()` is used to round `num1` to 2 decimal places, resulting in `3.14`.

In Example 2, `round()` is used to round `num2` to 3 decimal places, resulting in `2.718`.

In Example 3, if you don't specify the `ndigits` argument (like in this case), `round()` will round the number to the
nearest integer.

Keep in mind that `round()` uses a specific rounding algorithm, so be aware of potential precision issues when dealing
with very large or very small numbers.

---

## f-String

In Python, an f-string, short for "formatted string literals," is a way to embed expressions inside string
literals, using curly braces `{}`. These expressions are evaluated at runtime and then formatted and inserted into the
string.

Here's a basic syntax of an f-string:

```python
variable = 42
f_string = f"The value of the variable is {variable}"
```

In this example, the value of the `variable` (which is `42`) will be inserted into the string, resulting
in `The value of the variable is 42`.

Here are some key points about f-strings:

1. **Expression Inside Curly Braces**:
    - You can place any valid Python expression inside the curly braces.

   ```python
   name = "Alice"
   age = 30
   f_string = f"My name is {name} and I am {age} years old."
   ```

2. **Formatted Output**:
    - You can apply formatting options to the expression inside the curly braces to control how the value is displayed.

   ```python
   pi = 3.14159265359
   f_string = f"The value of pi is approximately {pi:.2f}"
   ```

   In this example, `:.2f` formats the floating-point number to two decimal places.

3. **Accessing Variables and Attributes**:
    - You can access variables, attributes, and even call methods within an f-string.

   ```python
   class Person:
       def __init__(self, name, age):
           self.name = name
           self.age = age

   person = Person("Bob", 25)
   f_string = f"My name is {person.name} and I am {person.age} years old."
   ```

4. **Arithmetic Operations**:
    - You can perform arithmetic operations within an f-string.

   ```python
   x = 10
   y = 20
   f_string = f"The sum of {x} and {y} is {x + y}"
   ```

5. **Using Escaped Curly Braces**:
    - If you need to include literal curly braces in an f-string, you can double them up (`{{` for `{` and `}}`
      for `}`).

   ```python
   f_string = f"{{Hello}}"
   ```

6. **Supports Python 3.6 and Later**:
    - f-strings were introduced in Python 3.6, so make sure you're using a compatible version.

7. **Efficient and Readable**:
    - f-strings are considered efficient in terms of runtime performance and are often preferred for their readability
      and ease of use.

Overall, f-strings provide a concise and powerful way to create formatted strings in Python, making it easier to
generate output with dynamic or calculated values.

---