> # Exercise 3.1 - Odd or Even

## Instructions

Write a program that works out whether if a given number is an odd or even number.

Even numbers can be divided by 2 with no remainder.

e.g. 86 is **even** because 86 ÷ 2 = 43

43 does not have any decimal places. Therefore the division is clean.

e.g. 59 is **odd** because 59 ÷ 2 = 29.5

29.5 is not a whole number, it has decimal places. Therefore there is a remainder of 0.5, so the division is not clean.

The **modulo** is written as a percentage sign (%) in Python. It gives you the remainder after a division.

e.g.

6 ÷ 2 = 3 with no remainder.

```
6 % 2 = 0
```

5 ÷ 2 = 2 x **2** + 1, remainder is 1.

```
5 % 2 = 1
```

14 ÷ 4 = 3 x **4** + 2, remainder is 2.

```
14 % 4 = 2
```

**Warning** your output should match the Example Output format exactly, even the positions of the commas and full stops.

## Example Input 1

```
43
```

## Example Output 1

```
This is an odd number.
```

## Example Input 2

```
94
```

## Example Output 2

```
This is an even number.
```

e.g. When you hit **run**, this is what should happen:

<img src="https://cdn.fs.teachablecdn.com/bkF9TKJSTGksvxNzOtba" alt="Exercise GIF" style="width: 100%;">

## Hint

1. All even numbers can be divided by 2 with 0 remainder.
2. Try some using the modulo with some odd numbers e.g.

```
3 % 2
```

```
5 % 2
```

```
7 % 2
```

Then try using the modulo with some even numbers e.g.

```
4 % 2
```

```
6 % 2
```

```
8 % 2
```

---

> # Exercise 3.2 - BMI Calculator 2.0

## Instructions

Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

It should tell them the interpretation of their BMI based on the BMI value.

- Under 18.5 they are underweight
- Over 18.5 but below 25 they have a normal weight
- Over 25 but below 30 they are slightly overweight
- Over 30 but below 35 they are obese
- Above 35 they are clinically obese.

[//]: # (<img src="https://cdn.fs.teachablecdn.com/qTOp8afxSkGfU5YGYf36" alt="Exercise GIF" style="width: 100%;">)

The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

**BMI** = (weight / (Height ** 2))

**Warning** you should **round** the result to the nearest whole number. The interpretation message needs to include the
words in bold from the interpretations above. e.g. **underweight, normal weight, overweight, obese, clinically obese**.

## Example Input

```
weight = 85
```

```
height = 1.75
```

## Example Output

85 ÷ (1.75 x 1.75) = 27.755102040816325

```
Your BMI is 28, you are slightly overweight.
```

e.g. When you hit **run**, this is what should happen:

<img src="https://cdn.fs.teachablecdn.com/mGRynIETXuVqoDk8unci" alt="Exercise GIF" style="width: 100%;">

The testing code will check for print output that is formatted like one of the lines below:

```
"Your BMI is 18, you are underweight."
"Your BMI is 22, you have a normal weight."
"Your BMI is 28, you are slightly overweight."
"Your BMI is 33, you are obese."
"Your BMI is 40, you are clinically obese."
```

## Hint

1. Try to use the **exponent** operator in your code.
2. Remember to **round** your result to the nearest whole number.
3. Make sure you include the words in **bold** from the interpretations.

---

> # Exercise 3.2 - Leap Year

## Instructions

Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366,
with an extra day in February. The reason why we have leap years is really fascinating, this video does it more justice:

[https://www.youtube.com/watch?v=xX96xng7sAE](https://www.youtube.com/watch?v=xX96xng7sAE)

This is how you work out whether if a particular year is a leap year.

> `on every year that is evenly divisible by 4
> **except** every year that is evenly divisible by 100
> **unless** the year is also evenly divisible by 400`

e.g. The year 2000:

2000 ÷ 4 = 500 (Leap)

2000 ÷ 100 = 20 (Not Leap)

2000 ÷ 400 = 5 (Leap!)

So the year 2000 is a leap year.

But the year 2100 is not a leap year because:

2100 ÷ 4 = 525 (Leap)

2100 ÷ 100 = 21 (Not Leap)

2100 ÷ 400 = 5.25 (Not Leap)

**Warning** your output should match the Example Output format exactly, even the positions of the commas and full stops.

## Example Input 1

```
2400
```

## Example Output 1

```
Leap year.
```

## Example Input 2

```
1989
```

## Example Output 2

```
Not leap year.
```

e.g. When you hit **run**, this is what should happen:

 <img src="https://cdn.fs.teachablecdn.com/AthNqKoSm6JD4sMom2X2" alt="Exercise GIF" style="width: 100%;">

## Hint

1. Try to visualise the rules by creating a flow chart on www.draw.io
2. If you really get stuck, you can see the [flow chart I created.](https://bit.ly/36BjS2D)



