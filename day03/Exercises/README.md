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

> # Exercise 3.3 - Leap Year

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

---

> # Exercise 3.4 - Pizza Order

## Instructions

Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.

Based on a user's order, work out their final bill.

```
Small Pizza: $15
```

```
Medium Pizza: $20
```

```
Large Pizza: $25
```

```
Pepperoni for Small Pizza: +$2
```

```
Pepperoni for Medium or Large Pizza: +$3
```

```
Extra cheese for any size pizza: + $1
```

## Example Input

```
size = "L"
```

```
add_pepperoni = "Y"
```

```
extra_cheese = "N"
```

## Example Output

```
Your final bill is: $28.
```

e.g. When you hit **run**, this is what should happen:


<img src="https://cdn.fs.teachablecdn.com/p1evEkwQxGNR4WlolIb4" alt="Exercise GIF" style="width: 100%;">

## Hint

1. Think about what you've learnt about multiple if statements and see if you can reduce the number of lines of code
   while having the same functionality.

---

> # Exercise 3.5 - Love Calculator

## Instructions

You are going to write a program that tests the compatibility between two people.

To work out the love score between two people:

> Take both people's names and check for the number of times the letters in the word TRUE occurs. Then check for the
> number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number.


For Love Scores **less than 10** or **greater than 90**, the message should be:

`"Your score is **x**, you go together like coke and mentos."`

For Love Scores **between 40** and **50**, the message should be:

`"Your score is **y**, you are alright together."`

Otherwise, the message will just be their score. e.g.:

`"Your score is **z**."`

e.g.

`name1 = "Angela Yu"`

`name2 = "Jack Bauer"`

T occurs 0 times

R occurs 1 time

U occurs 2 times

E occurs 2 times

Total = 5

L occurs 1 time

O occurs 0 times

V occurs 0 times

E occurs 2 times

Total = 3

Love Score = 53

Print: "Your score is 53."

## Example Input 1

```
name1 = "Kanye West"
```

```
name2 = "Kim Kardashian"
```

## Example Output 1

```
Your score is 42, you are alright together.
```

## Example Input 2

```
name1 = "Brad Pitt"
```

```
name2 = "Jennifer Aniston"
```

## Example Output 2

```
Your score is 73.
```

e.g. When you hit **run**, this is what should happen:

<img src="https://cdn.fs.teachablecdn.com/nfSILIPSNaIOwWhPR5vr" alt="Exercise GIF" style="width: 100%;">

The testing code will check for print output that is formatted like one of the lines below:

```
"Your score is 47, you are alright together."
"Your score is 125, you go together like coke and mentos."
"Your score is 54."
```

## Score Comparison

Not sure you're getting the correct score for the exercise? Use this table to check your code's score against mine.

| Name 1               | Name 2             | Score |
|----------------------|--------------------|-------|
 Catherine Zeta-Jones | Michael Douglas    | 99    
 Brad Pitt            | 	Jennifer Aniston	 | 73    
 Prince William	      | Kate Middleton	    | 67    
 Angela Yu	           | Jack Bauer	        | 53    
 Kanye West	          | Kim Kardashian	    | 42    
 Beyonce	             | Jay-Z	             | 23    
 John Lennon	         | Yoko Ono	          | 18    

## Hint

1. The `lower()` function changes all the letters in a string to lower case.

[https://stackoverflow.com/questions/6797984/how-do-i-lowercase-a-string-in-python](https://stackoverflow.com/questions/6797984/how-do-i-lowercase-a-string-in-python)

2. The `count()` function will give you the number of times a letter occurs in a string.

[https://stackoverflow.com/questions/1155617/count-the-number-occurrences-of-a-character-in-a-string](https://stackoverflow.com/questions/1155617/count-the-number-occurrences-of-a-character-in-a-string)

