
<h1 align="center">🧩 Sokoban AI Solver</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/AI_Search-FF6F00?style=for-the-badge&logo=artificial-intelligence&logoColor=white" alt="AI Search Algorithms" />
  <img src="https://img.shields.io/badge/PyGame-82C341?style=for-the-badge&logo=python&logoColor=white" alt="PyGame" />
</p>

> An intelligent, search-based solver for the classic puzzle game **Sokoban**. This project models the game as a state-space search problem and implements various informed and uninformed artificial intelligence algorithms to compute the optimal sequence of box-pushing moves while avoiding deadlocks.

---

## 🎮 The Core Environment

The solver navigates a grid-based environment ($N \times M$) consisting of walls, empty spaces, the player, boxes, and designated target cells.

* **State Representation:** Defined precisely by the current coordinate positions of the player and all boxes.
* **Action Model:** The player can move in four cardinal directions and push boxes (pulling is not allowed).
* **Transition Function:** Generates valid successor states based on movement rules and collision detection.
* **Goal Test:** The state is recognized as a terminal success when every box rests on a target cell.
* **Cost Function:** Step-based (uniform) cost applies to search expansions.

---

## 🧠 Implemented Search Algorithms

This project compares the efficiency, optimality, and performance of several classic AI search algorithms:

* **Uninformed Search:**
  * 🔹 **Breadth-First Search (BFS):** Guarantees the shortest path in terms of steps.
  * 🔹 **Uniform Cost Search (UCS):** Expands the cheapest path node first.
  * 🔹 **Iterative Deepening Search (IDS):** Balances spatial efficiency of DFS with the completeness of BFS.
* **Informed Search:**
  * 🔸 **A* Search (A-Star):** Utilizes custom, consistent, and admissible heuristic functions to drastically reduce the search space and find optimal solutions efficiently.

---

## 🎯 Learning Objectives

By developing this solver, the following core AI concepts were achieved:
- [x] Modeling real-world physical puzzles into formal state-space search frameworks.
- [x] Implementing, debugging, and comparing foundational uninformed and informed search algorithms.
- [x] Designing mathematically sound admissible and consistent heuristic functions.
- [x] Analyzing algorithm performance bottlenecks (time vs. space complexity).

---

## ⚙️ Requirements & Installation

### Tech Stack
* **Python 3.x**
* **Pygame** (Used for dynamic visual rendering of the search process and solution playback)

### Quick Start
1. Clone this repository:
   ```bash
   git clone [https://github.com/amirkhedri/sokoban-ai-solver.git](https://github.com/amirkhedri/sokoban-ai-solver.git)
   cd sokoban-ai-solver

```

2. Install the required dependencies:

pip install pygame

```


3. Run the solver:
```bash
python main.py

```



---

## 🎓 Academic Context

This project was developed for the **Fundamentals and Applications of Artificial Intelligence** course.

* **University:** Faculty of Computer Engineering, University of Isfahan
* **Semester:** Spring 2026 (1404-1405)



