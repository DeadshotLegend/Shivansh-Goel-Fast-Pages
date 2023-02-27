---
toc: true
base: post
description: LessonPlanning
categories: [markdown, Week 13]
title: LessonPlanning
---

### Nested Conditional Statements
- Nested Conditional Statements consist of conditional statemetns within conditional statements.
- Flow Chart of a Nested Conditional Statement includes: 
<img src='{{ "/images/nestedconditional.PNG" | relative_url }}' width='480' alt='Here is the the 3 quizes that I took'>
- Example for Nested Conditionals include:
if conditionA:
    # Code here executes when 'conditionA' is True
else:
    # Code that runs when 'conditionA' is False

    if conditionB:
        # Code that runs when 'conditionA' is False
        # and 'conditionB' is True
- Example of code:
age = 19
isGraduated = False
hasLicense = True

# Look if person is 18 years or older
if age >= 18:
    print("You're 18 or older. Welcome to adulthood!")

    if isGraduated:
        print('Congratulations with your graduation!')
    if hasLicense:
        print('Happy driving!')
- If Else Statements can be put inside of another if else statement using this layout for psuedo code.

if (condition 1)
    if (condition 2)
        first block of statement
    else 
        second block of statement
else
    if (condition 3)
        third block of statement
    else 
        fourth block of statement

### Quick Easy Challenge
