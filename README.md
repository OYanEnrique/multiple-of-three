# multiple-of-three
A simple Python script that finds and prints all multiples of three within a user-specified range.

# 🔢 Multiple of Three Finder

This is a command-line program written in Python that iterates through a range of numbers provided by the user and identifies which of them are multiples of three.

The script prompts the user for a starting and an ending number. It then uses a `for` loop to check each number in that range (inclusive). If a number is perfectly divisible by three, a message is printed to the console. 

## How to Use

1.  Make sure you have Python installed on your system.
2.  Save the code as a `.py` file (e.g., `multiple_of_three.py`).
3.  Open your terminal or command prompt.
4.  Navigate to the directory where the file is located and run the script:
    ```sh
    python multiple_of_three.py
    ```
5.  Enter the initial number for the range and press Enter.
6.  Enter the final number for the range and press Enter. The script will then print a message for each number found to be a multiple of three.

## How It Works

* **User-Defined Range:** The program takes two integer inputs from the user, a `first_number` and a `second_number`, to establish the boundaries for the check.
* **Iteration:** It uses a `for` loop with `range(first_number, second_number + 1)` to ensure every number from the start to the end (inclusive) is evaluated.
* **Divisibility Check:** Inside the loop, an `if` statement with the modulo operator (`if number % 3 == 0`) checks if the current number has a remainder of 0 when divided by 3. If the condition is true, the number is identified as a multiple of three.

## Technologies Used

* Python 3
