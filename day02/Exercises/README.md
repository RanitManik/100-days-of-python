# Day 2 Exercises

1. [Exercise 2.1 - Data Types](#exercise-21---data-types)
2. [Exercise 2.2 - BMI Calculator](#exercise-22---bmi-calculator)
3. [Exercise 2.3 - Your Life in Weeks](#exercise-23---your-life-in-weeks)

---

## Exercise 2.1 - Data Types

### Instructions

Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

**Warning.** Do not change the code on lines 1-3. Your program should work for different inputs. e.g. any two-digit
number.

### Example Input

```
39
```

### Example Output

3 + 9 = 12

```
12
```

e.g. When you hit **run**, this is what should happen:

<img src="https://cdn.fs.teachablecdn.com/iyJTPDDRRJCB1gmdVQMS" alt="Exercise GIF" style="width: 100%;">

### Hint

1. Try to find out the data type of two_digit_number.
2. Think about what you learnt about subscripting.
3. Think about type conversion.

---

## Exercise 2.2 - BMI Calculator

### Instructions

Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

The BMI is a measure of some's weight taking into account their height. e.g. If a tall person and a short person both
weigh the same amount, the short person is usually more overweight.

The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

**BMI** = (weight / (Height ** 2))

**Warning** you should convert the result to a whole number.

### Example Input

```
weight = 80
```

```
height = 1.75
```

### Example Output

80 ÷ (1.75 x 1.75) = 26.122448979591837

```
26
```

e.g. When you hit **run**, this is what should happen:

<img src="https://cdn.fs.teachablecdn.com/wmjVjddeSmGj0QVtOUrE" alt="Exercise GIF" style="width: 100%;">

### Hint

1. Check the data type of the inputs.
2. Try to use the exponent operator in your code.
3. Remember PEMDAS.
4. Remember to convert your result to a whole number (int).

---

## Exercise 2.3 - Your Life in Weeks

### Instructions

I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.

[https://waitbutwhy.com/2014/05/life-weeks.html](https://waitbutwhy.com/2014/05/life-weeks.html)

Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90
years old.

It will take your current age as the input and output a message with our time left in this format:

> You have x days, y weeks, and z months left.

Where x, y and z are replaced with the actual calculated numbers.

**Warning** your output should match the Example Output format exactly, even the positions of the commas and full stops.

### Example Input

```
56
```

### Example Output

```
You have 12410 days, 1768 weeks, and 408 months left.
```

e.g. When you hit **run**, this is what should happen:

<img src="https://cdn.fs.teachablecdn.com/RjqBViZQpyVTv7XY6cfA" alt="Exercise GIF" style="width: 100%;">

### Hint

1. There are 365 days in a year, 52 weeks in a year and 12 months in a year.
2. Try copying the example output into your code and replace the relevant parts so that the sentence is formated the
   same way.


