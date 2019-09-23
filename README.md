# TetrilingReassembly
Code for DE2 Computing 2 coursework. The goal was to design a program that could find a perfect tiling solution to an arbitrary target shape by using a given set of tetris pieces. The algorithm would be tested based on time performance and accuracy.

The final algorithm works by calculating a neighbours matrix from the target shape. It then creates a score matrix for all the possible placements for each shape, obtained by summing the total value of neighbours that the shape would contain when placed in each square of the neighbours matrix. Once the score matrix is generated for each shape, the algorithm will start placing the tetrominoes that encapsulate the lowest sum of neighbours.

The average running time for a 1000x1000 target shape with a 0.8 density was of 2.9 minutes, keeping a consistent accuracy of about 95% for the biggest target sizes and about 90% for very small instances of the problem.
