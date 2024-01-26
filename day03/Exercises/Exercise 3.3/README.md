# Exercise 3.3 - Leap Year

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
