# Ant Colony Optimization for Bin Packing Problem

## Insights and Applications
This project demonstrates advanced algorithmic design and optimization, applicable in logistics, resource allocation, and other domains requiring efficient packing solutions. The integration of probabilistic models and heuristic optimization showcases a powerful approach to solving NP-hard problems.

This repository implements an Ant Colony Optimization (ACO) algorithm to solve the **Bin Packing Problem (BPP)**, a classic combinatorial optimization problem. The BPP involves efficiently packing items of varying weights into a fixed number of bins while minimizing the weight difference between the heaviest and lightest bins. Two variants are supported: 
- **BPP1**: Standard item weights.  
- **BPP2**: Scaled item weights calculated as `(i * i) / 2`.

## Technical Summary

### Ant Colony Optimization (ACO)
The algorithm models a colony of ants searching for optimal paths through a graph. Each ant represents a potential solution, influenced by **pheromone trails** that are dynamically updated based on solution quality. Over time, pheromone evaporation prevents convergence to suboptimal solutions and encourages exploration.

### Key Features
1. **Pheromone Matrix**: A 3D matrix stores pheromone values for all graph edges. It is initialized randomly and updated iteratively based on solution quality (fitness).
2. **Ant Path Selection**: Ants probabilistically choose paths based on pheromone strengths, ensuring both exploitation of good solutions and exploration of new ones.
3. **Fitness Evaluation**: Solutions are evaluated by the weight difference between the heaviest and lightest bins.
4. **Pheromone Update and Evaporation**:
   - Pheromone trails are strengthened for paths that produce better solutions.
   - Global pheromone evaporation simulates natural decay, balancing exploration and exploitation.

### Algorithm Workflow
1. **Initialization**: 
   - Pheromone matrix created with random values.
   - Item weight matrix built for the chosen problem variant (BPP1 or BPP2).
2. **Ant Simulation**:
   - Ants traverse the graph, distributing items into bins based on pheromone strengths.
   - Each ant’s solution is recorded.
3. **Fitness Calculation**: The difference between the heaviest and lightest bins is used as the fitness metric.
4. **Batch Processing**:
   - A batch of ants runs iteratively, updating pheromone trails and identifying the best solution.
   - The average and best fitness values are computed for each batch.
5. **Pheromone Updates**: Trails are incremented based on the fitness of each path, with evaporation applied to simulate decay.
6. **Repeat**: The process iterates until a specified number of iterations or convergence.

### Technical Skills Demonstrated
1. **Optimization Techniques**:
   - Implementation of ACO for combinatorial optimization.
   - Fitness evaluation based on objective metrics.
2. **Data Structures**:
   - Efficient use of 3D matrices for pheromone management.
   - Probabilistic path selection with custom probability distributions.
3. **Algorithm Tuning**:
   - Configurable parameters for pheromone evaporation, batch size, and problem variants.
   - Dynamic adaptation to balance exploration and exploitation.
4. **Simulation and Batch Processing**:
   - Execution of multiple ant simulations per batch for robust performance assessment.
   - Aggregation of fitness metrics for iterative improvement.
5. **Code Design**:
   - Modular functions for initialization, pathfinding, fitness evaluation, and pheromone updates.
   - Clear separation of logic for different BPP variants.

## How to Use
1. **Select Problem Variant**: Modify function calls to toggle between `BPP1` (False) and `BPP2` (True). Update parameters in `buildPheramoneMatrix` and `buildItemWeightMatrix` accordingly.
2. **Adjust Batch Size**: Modify iteration counts in the main loop and batch functions to test larger or smaller datasets.
3. **Run the Simulation**: Execute `crawlMyAnts()` to run the ACO algorithm and observe outputs for best and average fitness.
