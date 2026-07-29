LIGHTNING MCQUEEN'S TODOLIST
Description:
This project is an interactive To Do List for Lightning McQueen and his team, in my mind also narrated by Mater. 
The app allows McQueen to add tasks to his list, view tasks with their respective status, change status from pending to done, or delete a task from list and finally being able to quit, all while saving each adjustment to a file so that it may be revisited at a later date.
Requirements:
Python 3, only built in functions and commands used in app code. Imported Library: OS, for saving file to wherever the script is.
Structure:
There is a main menu, on loop until the user decides to quit the program, where the numbered options of operations are displayed clearly for user to choose from. Once that choice is entered, there is a series of if-elif-else conditions that affirm user's choice and then call suitable, corresponding functions.
There is a created, flexible array/list that stores tasks already in the file, with proper enumeration and a default "pending status" and any new task is appended onto it.
Important Notes:
For the view_list() function, where no modifications will be made to list, the basic file functions are used. For add_task(), mark_as_done() and remove_task() f->lines functions are used because they are able of storing each line as an element in array which proved useful in all these three lines, and is considered the whole backbone of my structure.


Challenges:
1) Simplifying to myself the basics of python file handling/reading/writing even if I used little of the syntax. Most of it was very similar to C/C++, same concepts, different fonts.
 https://youtu.be/yRXIbRuJ7yQ?si=Gnee_Hkv9YejUXTP
2) At first, I was a bit lost on how to exactly track the status of each task. I contemplated a few options like "1. Fill up gas -- pending" or "P 1) Fill up gas" but each execution failed. It would require string manipulation like strcmp or strcpy version in python. I decided I would handle the entire list as if it was an array and each task would be followed by a status. It was then I discovered the f.readlines and f.writelines functions, which would read my file and store each line as an element in array. Because of that I was able to modify list very easily, whether it was adding, removing or changing the status.
3) After finishing my code and running it for the first time, I did not see the text file I made so I assumed I made a mistake and that nothing was being saved, seeing as I never had this problem before. But after searching in the file explorer, I found out that the file is being saved in the program files in the OS. First solution I tried was changing the file's name to a specific path in my laptop, just long enough to run test cases and make sure everything works. Then realized whoever will download my code will be unable to have the exact same path, so the code won't work.
I found a solution in a community blog, where importing a library called OS and specifying that the text file should always be saved with the script file made it easier for anyone using the code to have same results as I did.
4) Making sure that the progress is not overwritten each time
I used wrong identifiers in the file functions "a" instead of "w" or "r" until I gathered what was the problem and fixed that.



Resources:
https://peerlist.io/blog/engineering/python-switch-statement
https://imarticus.org/blog/file-handling-in-python/
https://www.geeksforgeeks.org/python/print-the-content-of-a-txt-file-in-python/
https://stackoverflow.com/questions/38105507/when-should-i-ever-use-file-read-or-file-readlines
https://stackoverflow.com/questions/3718657/how-do-you-properly-determine-the-current-script-directory


