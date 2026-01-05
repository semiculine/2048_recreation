2048: Event-Driven Logic & Matrix Manipulation:
A recreation of the classic 2048 puzzle game built using Python and the Turtle Graphics library. This project demonstrates the implementation of grid-based movement algorithms, state management, and event-driven programming.

Features Matrix-Based Game Logic: 
Utilizes nested lists to represent the $4 \times 4$ game board with $O(n^2)$ traversal for movement and merging.

State Tracking: Implemented a secondary grid_merged boolean matrix to prevent illegal double-merges within a single turn.

Dynamic Win/Loss States: Automated checks for game-over conditions (no empty cells and no valid adjacent merges) and win conditions (2048 tile reached).

Keyboard Event Mapping: Responsive controls using the wn.onkeypress event listeners.

Technical Implementation
The core challenge of this project was the Recursive Move Logic. To move tiles effectively: The grid is iterated in the direction of the move.Each tile is shifted to the furthest available empty cell.Collision logic checks if the adjacent tile matches in value; if so, it doubles the leading tile and clears the trailing one.

Roadmap: Performance & UX Upgrades
Currently, the game uses a "Stamp & Refresh" rendering method. My next phase of development focuses on: Sprite-Based Animation: Moving away from turtle.stamp() to individual Turtle objects to implement Linear Interpolation (Lerp) for smooth sliding animations. 

Audio Integration: Utilizing the pygame.mixer library to add diegetic sound feedback for tile movements and merges. 

Input Debouncing: Implementing a "busy" flag to prevent system crashes caused by rapid-fire key inputs during animation cycles.

How to Run
Ensure you have Python 3.x installed.
Clone the repository: Bashgit clone https://github.com/yourusername/2048-python.git
Run the script: Bashpython main.py
