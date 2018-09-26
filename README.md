
# Creating Functions - Lab

## Introduction
As we know, we can use functions to name sequences of our code, thus making our code more expressive. We can also use functions to allow us to reuse our code. In this lab we will practice using functions for these purposes.

## Objectives
You will be able to:
* Create and use their own custom functions

## Instructions: 
### Writing our first functions

Imagine we are working on our list of travel destinations -- which can really turn out to be a full time job if we like to travel. We have our list of `travel_destinations` which we assign below. Write a function called `number_of_destinations` that returns the number of destinations we have on our list.


```python
travel_destinations = ['argentina', 'mexico', 'italy', 'finland', 'canada', 'croatia']
# define function here
```


```python
number_of_destinations() # 6
```

Now write another function called `next_up` that returns our first destination (the destination with the lowest index), in the `travel_destinations` list.


```python
# define function here
```


```python
travel_destinations = ['argentina', 'mexico', 'italy']
next_up() # 'argentina'
```


```python
travel_destinations = ['finland', 'canada', 'croatia']
next_up() # 'finland'
```

Ok, now write a function called `favorite_destination` that returns the string `'madagascar'`.


```python
# define function here
```


```python
favorite_destination() # 'madagascar'
```

Again, let's declare an array called `travel_destinations`. Write a new function called `add_favorite_destination` that also returns the string `'madagascar'`, but adds the string `'madagascar'` to the end of the list, `travel_destinations`, as well.


```python
travel_destinations = ['argentina', 'mexico', 'italy', 'finland', 'canada', 'croatia']
favorite_destination()
travel_destinations[-1] # 'madagascar'
```

Now let's write another function called `capitalize_countries` which iterates through the list of `travel_destinations` and capitalizes the first letter of each word. It should return a list of capitalized destinations.


```python
travel_destinations = ['argentina', 'mexico', 'italy', 'finland', 'canada', 'croatia']
# define function here
```


```python
capitalize_countries() # ['Argentina', 'Mexico', 'Italy', 'Finland', 'Canada', 'Croatia']
```

Great! Now if someone adds a country that is lowercased to our list of destinations, we can simply call our function again to capitalize each of the destinations in the list.


```python
travel_destinations = ['argentina', 'mexico', 'italy', 'finland', 'canada', 'croatia']
capitalize_countries() # ['Argentina', 'Mexico', 'Italy', 'Finland', 'Canada', 'Croatia']
travel_destinations.append('japan')
capitalize_countries() # ['Argentina', 'Mexico', 'Italy', 'Finland', 'Canada', 'Croatia', 'Japan']
```

## Summary

Great job! In this lab we were able to get practice both writing and returning values from functions. We also practiced accessing variables not local to the function but in the global scope.
