memetics-sim
============

An visual simulation of evolution through color

To try it out, you need to install pygame (the graphics tool I used), which can be found at:

http://www.pygame.org/download.shtml


Then, download my source, unzip it, and run

python simulation.py 100

in the folder that the source is in.


Unfortunately, for now you cannot interact with the pygame window while it is running - just watch!



Explanation of what is going on:

This simulation uses changing colors to simulate the evolution of ideas.

The window displays a grid of colored squares. Each square is an 'agent'(representing a person), which has a color (an idea).
Collectively, the agents go through an evolutionary process through which they change their colors (ideas).
This evolutionary process happens in rounds.
During each round an agent may 
  a) slightly randomize their color (innovate)
  -or-
  b) take the best color they see one of their neighbors with (imitate).
"But what," you ask, "makes a color 'good'?".
Good question; for this simulation, white and black are defined to be the best colors, and colors get better the closer they are to one of these extremes.
We could, however, do the simulation with a different judge of how 'good' color is.

As the simulation runs, you see how 'good' colors appears through semi-random change (innovation), and then spread accross the board through copying (immitation)
