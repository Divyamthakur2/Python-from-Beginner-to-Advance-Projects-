"""
================================================
 VARIABLE CHAPTER - Swap Glasses Exercise
================================================
 Author : Divyam Thakur
 Date   : November 2025
 Topic  : Variables & Swapping Values
================================================
"""

# ----------------------------------------
# WHAT IS A VARIABLE?
# ----------------------------------------
# Variables are containers for storing data values.
# Python has no command for declaring a variable.
# A variable is created the moment you first
# assign a value to it.


# ----------------------------------------
# PROBLEM STATEMENT
# ----------------------------------------
# We have two variables: glass1 and glass2.
# - glass1 contains "mango juice"
# - glass2 contains "apple juice"
#
# TASK: Swap the contents using only 3 lines of code.
# RULE: You cannot type the words "mango juice"
#       or "apple juice" again in the swap logic.
# HINT: You are allowed to use a third variable.


# ----------------------------------------
# SOLUTION
# ----------------------------------------
glass1 = "mango juice"
glass2 = "apple juice"

# Use glass3 as a temporary holder
glass3 = glass1     # Step 1: backup glass1
glass1 = glass2     # Step 2: overwrite glass1 with glass2
glass2 = glass3     # Step 3: overwrite glass2 with backup

# ----------------------------------------
# OUTPUT
# ----------------------------------------
print("After Swap:")
print("glass1 =", glass1)   # apple juice
print("glass2 =", glass2)   # mango juice