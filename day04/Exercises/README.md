# Day 4 Exercises

1. [Exercise 4.1 - Heads or Tails](#exercise-41---heads-or-tails)
2. [Exercise 4.2 - Who's Paying](#exercise-42---whos-paying)
3. [Exercise 4.3 - Treasure Map](#exercise-43---treasure-map)

---

## Exercise 4.1 - Heads or Tails

### Instructions

You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".

**Important**, the first letter should be capitalised and spelt exactly like in the example e.g. Heads, not heads.

There are many ways of doing this. But to practice what we learnt in the last lesson, you should generate a random
number, either 0 or 1. Then use that number to print out Heads or Tails.

e.g.
1 means Heads
0 means Tails

### Example Output

```
Heads
```

or

```
Tails
```

---

## Exercise 4.2 - Who's Paying

### Instructions

You are going to write a program which will select a random name from a list of names. The person selected will have to
pay for everybody's food bill.

**Important**: You are not allowed to use the `choice()` function.

**Line 8** splits the string `names_string` into individual names and puts them inside a **List** called `names`. For
this to work, you must enter all the names as name followed by comma then space. e.g. name, name, name

### Example Input

```
Angela, Ben, Jenny, Michael, Chloe
```

Note: notice that there is a space between the comma and the next name.

### Example Output

```
Michael is going to buy the meal today!
```

### Hint

1. You might need the help of the `len()` function.
2. Remember that Lists start at index 0!

---

## Exercise 4.3 - Treasure Map

### Instructions

You are going to write a program which will mark a spot with an X.

In the starting code, you will find a variable called ```map```.

This ```map``` contains a nested list.
When ```map``` is printed this is what the nested list looks like:

```
['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']
```

In the starting code, we have used new lines (```\n```) to format the three rows into a square, like this:

```
['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
```

This is to try and simulate the coordinates on a real map.

[//]: # (![]&#40;https://res.cloudinary.com/dk-find-out/image/upload/q_80,w_1440,f_auto/Co-ordinates_oggjzg.jpg&#41;)

Your job is to write a program that allows you to mark a square on the map using a two-digit system. The first digit for
the input will specify the column (the position on the horizontal axis). The second digit in the input will specify the
row number (the position on the vertical axis).

First your program must take the user input and convert it to a usable format.

Next, you need to use it to update your nested list with an "x".

### Example Input 1

column 2, row 3 would be entered as:

```
23
```

### Example Output 1

```
['⬜️', '⬜️', '⬜️']

['⬜️', '⬜️', '⬜️']

['⬜️', 'X', '⬜️']
```

### Example Input 2

column 3, row 1 would be entered as:

```
31
```

### Example Output 2

```
['⬜️', '⬜️', 'X']

['⬜️', '⬜️', '⬜️']

['⬜️', '⬜️', '⬜️']
```

e.g. When you hit **run**, this is what should happen:

<img src="https://cdn.fs.teachablecdn.com/5hliFjyIR96LdestyfPd" alt="Exercise GIF" style="width: 100%;">

### Hint

1. Remember that Lists start at index 0!
2. ```map``` is just a variable that contains a nested list. It's not related to the map function in Python.

