# Exercise 5.1 - Average Height

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
