# QuaC

## Intro
Quilt as Code

This project was created as a little fun for a home project.

Ever needed to mock design a quilt but unsure as to the number of panels, the size of each panel and the disctribution of colours?

Me neither, until tonight!

Don't get caught up doing it via graphics software, just define your very own quilt and have python do the rest!

## Configurables:

### Colours
Define some colours for use in the patterns.  

Each colour should be in the form of <name> = <rgb> where <rgb> is in the format (r,g,b)
```python
b = (115, 156, 191)
n = (48, 53, 70)
y = (255, 168, 0)
w = (226, 224, 216)
r = (162, 0, 57)
```

Define the color of your border.
  
The color should be the name of on the colors you just defined.
  
```python
border_color = n
```
  
Now you need to define the pattern.
  
Each row should look like this:
```python
[ color, color, color ],
```
  
And all the rows should be inside a 
```python
[]
```
  
The end result should be something like this:
```python 
pattern = [
    [y, n, r, n, b], 
    [n, w, n, w, n], 
    [b, n, r, b, y],
    [n, w, n, w, n],
    [r, n, b, n, y],
    ]
```

Finally you set the ratios for the rectangle height to width and border the quilt border to cell width.
  
```python
rectangle_ratio = 1.3
border_ratio = 0.2
```
  
The script is preconfigured to output a lovely Harry Potter quilt, why even change it?
  
![Harry Potter Quilt](quilt.png?raw=true)
