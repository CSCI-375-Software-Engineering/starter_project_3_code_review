# Code Review Summary Report

## Overview
The goal of this assignement was to simulate a software engineering workflow with the inclusion of code reviewing and linting. This was done with the boggle programs developed before.

## Recieved Feedback
For my code I received overall positive feedback with a few critiques targeting edge cases and redunancy for good maintainability. My original code was said to be a strong and well-structured implementation with clear validation, thoughtful state management, and an efficient DFS with proper backtracking and prefix pruning. I was  given  feedback that my usage of setter methods and my 8 direction traversal were well implemented, clean, and readable. Specific critiques were made regarding where I should raise value errors for easier debugging (42) or where addressing the edge cases by raising an error would maybe be a cleaner approach than what I had (17, 22, 32). I also got other suggestions like checking my grid for numeric or symbol elements to clear that edge case and clearing up _self.dictionary_ (41) as well as _self.words_ redundancies (92).

py.orig line suggestions:
17, 22, 32, 41, 42, 92

## Given Feedback
I reviewed Jasmine's code and I gave it an overall good review and it checked all the requirements of the boggle program. I also thought it was very readable and had good maintainability. My critiques were to improve the prefix optimization where _find_all_words_ iterates through the entire dictionary to check _startswith(word)_ which can affect runtime negatively. I suggested using a trie/prefix tree which could reduce runtime problems. There was a Qu edge case that I suggested could be added in. Grid initialization could include a check to make sure all q's are qu's unless specifically intended otherwise. I suggested making _find_all_words_ a private helper method (_find_all_words, *key: _ in the front) which would enhance code style and signal to other coders that it's an internal tool and not main public code to enhance maintainability. My final suggestion was reduce redundancy in certain places (moving certain _self.(...)_ into the constructor, also since grid and _fast_dictionary_ are already stored as properties of the class _(self.grid)_, the recursive method can get them directly using self so _self.find_all_words(y + dy, x + dx, word, grid, fast_dictionary, visited, solution)_ could become _def _find_all_words(self, y, x, word, visited):_  which makes the code cleaner.

## Implemented Improvements
Besides changing the code to account for the critiques I got on my original boggle code, I also added docstrings and inline comments to make the code easier to understand and follow to enhance maintainability of the program. I added the value error flags for the edge cases pointed out in the review in order to pass potential test scenarios, and also removed the redundancies that were present for __self.dictionary_ and __self.words_ so that my code was cleaner.

## Static Analysis Results
Lint and style issues were found when I ran my boggle code and my unit testing code. Mostly, it was spacing issues or line length. I had to shorten and organize/align alot of lines of code that were too long (>79) and also some my docstrings and inline comments (>72). There were spaces I had to makes sure I removed like in my grid and dictionary. Final thing I had to change was adding 2 empty lines instead of one before a line like _class Boggle:_ or the if statement that calls main at the end.

## Regression Testing
After the changes, I used the provided testing check program and all the tests passed successfully.

## Reflection
The code review excersice was very informative because I could see where I could improve my own code while reviewing someone else's program and seeing how they approached it. I like that the critiques I had to give and the ones I got back were specific so I knew exactly what to fix. This simulated professional workflow and reviewing activity definitely made me more aware about PEP8 guidelines and conventions for readability and maintainability because the linting errors were annoying to fix. Also made me more keen about adding in edge case handling for even niche problems you wouldn't really think about when designing a baseline program.

