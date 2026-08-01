# 2048: Event-Driven Logic & Matrix Manipulation

A recreation of the classic 2048 puzzle game built using Python and the Turtle Graphics library. This project demonstrates the implementation of grid-based movement algorithms, state management, and event-driven programming.

---

## 🚀 Features

* **Matrix-Based Game Logic:** Utilizes nested lists to represent the $4 \times 4$ game board with $O(n^2)$ traversal for movement and merging.
* **State Tracking:** Implemented a secondary `grid_merged` boolean matrix to prevent illegal double-merges within a single turn.
* **Dynamic Win/Loss States:** Automated checks for game-over conditions (no empty cells and no valid adjacent merges) and win conditions (2048 tile reached).
* **Keyboard Event Mapping:** Responsive controls mapped dynamically using `wn.onkeypress` event listeners.

---

## 🛠️ Technical Implementation

The core challenge of this project was the **Recursive Move Logic**. To move tiles effectively:
1. **Directional Iteration:** The grid is iterated in the direction of the user's move.
2. **Shift Optimization:** Each tile is shifted to the furthest available empty cell.
3. **Collision Logic:** The system checks if the adjacent tile matches in value. If so, it doubles the leading tile, clears the trailing one, and flags the cell as merged for the remainder of the turn.

---

## 🗺️ Roadmap: Performance & UX Upgrades

Currently, the game uses a "Stamp & Refresh" rendering method. The next phases of development focus on the following upgrades:

| Feature | Description | Target Library |
| :--- | :--- | :--- |
| **Sprite-Based Animation** | Moving away from `turtle.stamp()` to individual Turtle objects to implement Linear Interpolation (Lerp) for smooth sliding animations. | `turtle` |
| **Audio Integration** | Utilizing the sound system to add diegetic audio feedback for tile movements and merges. | `pygame.mixer` |
| **Input Debouncing** | Implementing a "busy" flag to prevent system crashes caused by rapid-fire key inputs during animation cycles. | Core Python |

---

## 📦 How to Run

### Prerequisites
Ensure you have Python 3.x installed on your system.

### Installation & Execution
1. Clone the repository:
   ```bash
   git clone https://github.com/semiculine/2048_recreation.git
   ```

2. Navigate into project directory:
   ```bash
   cd 2048_recreation
   ```

4. Run the script:
   ```bash
   python main.py
   ```
