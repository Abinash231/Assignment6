# Assignment6

Topic: CALCULATOR USING TKINTER:

How the Code Works:

1. Setup and Imports
  tkinter is imported for GUI creation.
  messagebox from tkinter is used to display error messages.
2. Click Function (click(event)):
  Captures the button text when clicked.
  If "=" is clicked:
    Evaluates the expression entered using eval().
    Displays the result in the entry box.
    If an error occurs (like invalid syntax), an error message is shown.
  If "C" is clicked:
    Clears the entire entry box.
  For other buttons:
    The button text is appended to the current input.
3. GUI Components:
  Root Window: Created with a fixed size (300x400) and titled "Simple Calculator".
  Entry Widget: For displaying the input and output.
  Button Frame: Organized buttons (0-9, operators, C, =) into a grid-like layout using nested frames.
4. Button Arrangement:
  Buttons are arranged in rows:
[7] [8] [9] [/]
[4] [5] [6] [*]
[1] [2] [3] [-]
[C] [0] [=] [+]
  Each button binds the click event to the click function.
5. Application Loop:
  The root.mainloop() keeps the window open and responsive.
