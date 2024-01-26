# Exercise 4.3 - Treasure Map

## Instructions

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

## Example Input 1

column 2, row 3 would be entered as:

```
23
```

## Example Output 1

```
['⬜️', '⬜️', '⬜️']

['⬜️', '⬜️', '⬜️']

['⬜️', 'X', '⬜️']
```

## Example Input 2

column 3, row 1 would be entered as:

```
31
```

## Example Output 2

```
['⬜️', '⬜️', 'X']

['⬜️', '⬜️', '⬜️']

['⬜️', '⬜️', '⬜️']
```

e.g. When you hit **run**, this is what should happen:

<img src="https://cdn.fs.teachablecdn.com/5hliFjyIR96LdestyfPd" alt="Exercise GIF" style="width: 100%;">

## Hint

1. Remember that Lists start at index 0!
2. ```map``` is just a variable that contains a nested list. It's not related to the map function in Python.
