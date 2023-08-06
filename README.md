# ***This*** is Wordle Solver !
## Video Demo:  <https://youtu.be/MkUZapL8Qjs>
## Description:
This was my final project for Harvard University' s CS50p 2023 course on programming with Python: a ***Python program*** that provides possible solutions to a Wordle puzzle.
## Included files:
- ***project.py :*** Source code file.
- ***dict.txt :*** Text dictionary of English words - required ([source](https://github.com/dwyl/english-words/blob/master/words_alpha.txt)).
- ***README.md :*** What you' re reading right now.
## Overview:
The program prompts the user for a list of confirmed excluded and included letters respectively. Then requests permission to provide exact locations (or NOT locations). These lists are then fed into separate functions, each of which returns a regular expression pattern that is applied at different levels of the dictionary search, progressively narrowing the results.

## Technical stuff:
- The program makes extensive use of Python' s re module for regular expressions. User input is captured with the use of the **re.findall** method. This ensures the creation of a list of individual letters, regardless of the way they were input by the user. So, 'a, b, c, d' produces the same output as 'abcd' and 'a.b.c.d' -> ['a', 'b', 'c', 'd']. **Invalid input is ignored**, so 'ab23,#3' will yield ['a', 'b'].

- The duplicate function checks if the user has provided the same letter(s) in included and excluded groups and halts further execution of the program.

- Each of the functions pattern1, pattern2 and pattern3 return regular expression patterns that are applied in main with ***re.search***. Pattern1 returns a regex of the type **r'\b[^abcd..]{5}\b'** which ensures exclusion and word length of 5 letters. Pattern2 returns a regex pattern of type **r'\b(?=w*a)(?=w*b)...\w+\b'**, ensuring the inclusion of each letter using positive lookahead. Finally, pattern3 functions returns a tuple of regex patterns for defining NOT locations and exact locations respectively. Notice how each is used at a different nesting depth in the main program loop.

- Finally, the test_project.py file executes some test on the expected return values of some functions with the help of Pytest.
### Epilogue
I hope you find my project interesting and eventually useful. Thanks for reading!
