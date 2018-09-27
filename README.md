
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

def number_of_destinations():
    return len(travel_destinations)
```

> Below, remove the first `#` to uncomment the following line(s) of code and then press `shift` + `enter` to run the cell


```python
number_of_destinations() # 6
```

Now write another function called `next_up` that returns our first destination (the destination with the lowest index), in the `list_of_destinations` list.


```python
# define function here
def next_up():
    return list_of_destinations[0]
```

> Below, remove the first `#` to uncomment the following line(s) of code and then press `shift` + `enter` to run the cell


```python
list_of_destinations = ['finland', 'canada', 'croatia']
next_up() # 'argentina'
```


```python
list_of_destinations = ['argentina', 'mexico', 'italy']
next_up() # 'finland'
```

Ok, now write a function called `favorite_destination` that returns the string `'madagascar'`.


```python
# define function here
def favorite_destination():
    return 'madagascar'
```

> Below, remove the first `#` to uncomment the following line(s) of code and then press `shift` + `enter` to run the cell


```python
favorite_destination() # 'madagascar'
```

Again, let's declare a list called `favorite_destinations`. Write a new function called `add_favorite_destination` that also returns the string `'madagascar'`, but adds the string `'madagascar'` to the end of the list, `favorite_destinations`, as well.


```python
# define function here
def add_favorite_destination():
    favorite_destinations.append('madagascar')
    return 'madagascar'
```

> Below, remove the first `#` to uncomment the following line(s) of code and then press `shift` + `enter` to run the cell


```python
favorite_destinations = ['argentina', 'mexico', 'italy', 'finland', 'canada', 'croatia']
add_favorite_destination()
favorite_destinations[-1] # 'madagascar'
```

Now let's write another function called `capitalize_countries` which iterates through the list of `capitalized_destinations` and capitalizes the first letter of each word. It should return a list of capitalized destinations.


```python
capitalized_destinations = ['argentina', 'mexico', 'italy', 'finland', 'canada', 'croatia']
# define function here
def capitalize_countries():
    capitalized = []
    for country in capitalized_destinations:
        capitalized.append(country.capitalize())
    return capitalized
```

> Below, remove the first `#` to uncomment the following line(s) of code and then press `shift` + `enter` to run the cell


```python
capitalize_countries() # ['Argentina', 'Mexico', 'Italy', 'Finland', 'Canada', 'Croatia']
```

Great! Now if someone adds a country that is lowercased to our list of destinations, we can simply call our function again to capitalize each of the destinations in the list.

## Summary

Great job! In this lab we were able to get practice both writing and returning values from functions. We also practiced accessing variables not local to the function but in the global scope.
