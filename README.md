Defeat-the-Wizard
-----------------

Hey guys, 

have fun with this little game. This kind of looping statement structure can be used for a billion things.



Original version published July 29, 2018 at 10:30pm
+ First commit

Version 1.0.1 published July 31, 2018 at 6pm
+ Add the ability for inputs to work regardless of capitalization
+ Removed 1 or 2 useless lines of code

Version 1.0.2 published on July 31, 2018 at 7:30pm
+ Made input arguments much simpler
+ Made the Defend ability actually do something
+ Fixed an error that was displaying the wrong values for player health and enemy health by using variables instead of hardcoding.
+ Used 2 exec functions to print out the user and enemy health after each turn instead of using print statements each time

Version 1.0.3 published on July 31, 2018 at 8:15pm
+ Added autorun line to the top of the program to make it easier to run the program
+ Added a missing single quote at the end of "print("What type of person are you?\n\nType either 'Wizard' or 'Warrior':")"

Version 1.0.4 published on July 31, 2018 at 11pm
+ Changed all concatenations in print statements to use function strings "f-strings {}" instead of plus signs +
+ f-strings don't allow the new line symbol \n in them, so I added a bunch of blank print() statements to create new lines for readability (I may not use f-strings forever because of this drawback)
+ Made variables for the inputs that correspond to attack and defend, in case I ever want to make them something other than 'A' or 'D'
+ Created another exec function to print out the statement when the enemy attacks you, in case I ever want to change the enemy attack dialogue
