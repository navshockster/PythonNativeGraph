# PythonNativeGraph
Native Graph in Python using spaces to plot x,y values. Can plot 1st and 2nd degree equations.

To plot, print command is used for elements in an array graphy. Graphy are all elements on y-axis, including the axis and integer markings themselves. The amount of elements in Graphy is determined by the maximum of the user-inputted equation.

The list yValues is then iterated through. Because graphy is an array of lists, these lists are appended with three spaces * the corresponding x value in list xValues and the character "x". 

Program also checks to see if there are any two points with the same y value, and when other point is found it is plotted using the same method but subtracting the amount of spaces used by previous point with same y value.
