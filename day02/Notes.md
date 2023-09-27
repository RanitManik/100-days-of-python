> # Notes

### Table of Contents

1. [Underscore_ in Python](#Underscore_-in-Python)
2. [Type casting in Python](#Type-casting-in-Python)
3. [Type checking in Python](#Type-checking-in-Python)

---

## Underscore_ in Python

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

3. **In Internationalization (i18n)**:

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

   In this example, the last result, which is `4`, is stored in `_`. When you print `_`, it prints the value.

Overall, the use of `_` in a print statement or in Python code in general is largely about conveying meaning to other
developers. It's a way of indicating that a particular value or variable is intentionally being disregarded or isn't
relevant in a given context.

---

## Type checking in Python

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

5. **Using `Duck Typing`:

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

## Type casting in Python

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

