Fatmata Kanu - Starter Project 3 Code Review Summary


This assignment was basically a way to introduce us to a real software engineering workflow, improve readability, and get a feel for peer code reviews and using static analysis tools. The goal of the assignment was to create a boggle solver finds as many valid words as possible in an NxN grid of letters while following the specific Boggle rules. I decided to approach the solver using recursion because it felt like the most easiest way to explore all the different paths on the board without writing a ton of nested loops. I also added a prefix set to cut off searches early when the letters being built could not get a real word. Overall, I wanted to have my solver be as readable and easy to follow while still making sure I followed everything on the rubric. 

My partner gave me a bunch of helpful feedback as one of the most important thing he pointed out were my indentation errors as if I didn't fix those I would not get very far on passing the tests!! 
He also mentioned adding a docustring to describe my Boggle class and the other feedback was more about style and readability such as having better ways to write comments, helping me follow the style guidelines and moving around my code so it was easier to understand.
His feedback was very very helpful!


Reviewing my partners code, I suggested a way to reset his Hashtable so the size count could stay accurate, and mentioning just small changes for  better readability also gave a different solution for the square grid check so it could also check every row length so an uneven row grid does not pass if only the first one matches. My overall summary was that his solver was put really well together and easy to follow and I only added small tweaks. 

After going through my partners comments and added in all the suggestions they said to make and fixed all indentation issues. During testing I found another issue where my solver had an error because of an empty grid to I added a checker to handle the case and return empty, other than that everything ran pretty smoothly. 

As I finished my changes and ran the pycodestyle, I got a bunch of errors, such as my lines being too long or comments not having the correct spacing, and blank lines with hidden whitespace, so I worked through each section of the errors I was getting and was able to fix everything after running the command a couple times.

Once I corrected all my code and ran the auto grader test, it failed 2 times but it was just small errors so I fixed them and all 26 tests passed.


After completing this assignment, I learned way more about what a code review actually looks like, how the process goes, and how much it can imporve readability by making sure the code is good enough for people to understand and work with it. I liked getting feedback from my partner as it was helpful because he was able to catch things that I might have looked past and vice versa with reviewing his code. Overall this was a pretty insightful assignment 





