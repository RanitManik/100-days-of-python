> # Exercise 5.1 - Average Height

## Instructions

You are going to write a program that calculates the average student height from a List of heights.

e.g. `student_heights = [180, 124, 165, 173, 189, 169, 146]`

The average height can be calculated by adding all the heights together and dividing by the total number of heights.

e.g.

180 + 124 + 165 + 173 + 189 + 169 + 146 = **1146**

There are a total of **7** heights in `student_heights`

1146 ÷ 7 = **163.71428571428572**

Average height rounded to the nearest whole number = **164**

**Important** You should not use the `sum()` or `len()` functions in your answer. You should try to replicate their
functionality using what you have learnt about for loops.

## Example Input

```
156 178 165 171 187
```

In this case, student_heights would be a list that looks like: [156, 178, 165, 171, 187]

## Example Output

```
171
```

e.g. When you hit **run**, this is what should happen:


<img src="https://cdn.fs.teachablecdn.com/Nzb8hUVsQJ6STAGnvDCP" alt="Exercise GIF" style="width: 100%;">

## Hint

1. Remember to use the `round()` function to round the average height before you print it.

---

> # Exercise 5.2 - Highest Score

## Instructions

You are going to write a program that calculates the highest score from a List of scores.

e.g. `student_scores = [78, 65, 89, 86, 55, 91, 64, 89]`

**Important** you are not allowed to use the max or min functions. The output words must match the example. i.e

> `The highest score in the class is: x`

## Example Input

```
78 65 89 86 55 91 64 89
```

In this case, student_scores would be a list that looks like: `[78, 65, 89, 86, 55, 91, 64, 89]`

## Example Output

```
The highest score in the class is: 91
```

e.g. When you hit **run**, this is what should happen:


<img src="https://cdn.fs.teachablecdn.com/DnSPgYNSTgeHRJ3MinHg" alt="Exercise GIF" style="width: 100%;">

## Hint

1. Think about the logic before writing code. How can you compare numbers against each other to see which one is larger?

---

> # Exercise 5.3 - Adding Evens

## Instructions

You are going to write a program that calculates the sum of all the even numbers from 1 to 100. Thus, the first even
number would be 2 and the last one is 100:

i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100

Important, there should only be 1 print statement in your console output. It should just print the final total and not
every step of the calculation.

## Hint

1. There are quite a few ways of solving this problem, but you will need to use the `range()` function in any of the
   solutions.

---

> # Exercise 5.4 - FizzBuzz

## Instructions

You are going to write a program that automatically prints the solution to the FizzBuzz game.

> `Your program should print each number from 1 to 100 in turn.`

> `When the number is divisible by 3 then instead of printing the number it should print "Fizz".`

>     `When the number is divisible by 5, then instead of printing the number it should print "Buzz".` 

>       `And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"`

e.g. it might start off like this:

```
`1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz`
```

`.... etc.`

## Hint

1. Remember your answer should start from 1 and go up to and including 100.

2. Each number/text should be printed on a separate line.

---