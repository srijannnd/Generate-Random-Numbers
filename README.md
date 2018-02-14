# Generate-Random-Numbers

Randomness can be acheived with very small time delays and thus we can generate a random digit.

random_number.py contains a function random_num() which generates a random number between 1 and 10 with 70% bias on a greater number (i.e. bias on number greater than or equal to 5)

To achieve the bias, values generated are stored in text file and then the file is evaluated (using history as the source of bias).

Download both the scripts in a a single directory and run Random_numbers_test.py to verify the bias and randomness of the agorithm.
