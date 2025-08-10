```py title="add_numbers.py" linenums="1" hl_lines="2-3"
# Function to add two numbers
def add_two_numbers(num1, num2):
    return num1 + num2
    
# Example usage
result = add_two_numbers(5, 3)
print('the sum is:', result)
```

```sh title="search text on files" linenums="1"
grep -rn "pepito" . # (1)
```

1. Search text `pepito` recursively on current directory and shows the line number of each matching line.