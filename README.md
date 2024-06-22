# Delivery Route Optimization

This project implements an algorithm to optimize delivery routes for a mailing company. The objective is to minimize the sum of load percentages across all trucks used in a delivery path, ensuring efficient utilization of available capacity.


## Features
- Parses input to build graphs representing transportation capacities and current loads.
- Implements a modified Dijkstra’s algorithm to find the optimal delivery path.
- Ensures trucks at capacity are not used in the path.
- Outputs the sequence of cities from the start city to the destination city.

## Installation and Use
1. Clone the repository:
   ```sh
   git clone https://github.com/mo-austin/delivery-route-optimization.git
   cd delivery-route-optimization
2. Run main script:
   ```sh
   python main.py

## Input Format For Custom Input
Your input should include the following parameters:
1. numCities: The number of total cities.
2. capacities: A list of strings representing the capacities of each truck. Each string contains a comma-separated list of integer values: starting city, destination city, and carrying capacity.
3. loads: A list of strings representing the current loads of each truck. Each string contains a comma-separated list of integer values: starting city, destination city, and current load.
4. start: The start city.
5. end: The destination city.

## Example Input Format
  ```
  numCities = 5
  capacities = ["0,3,100", "0,1,15", "0,2,100", "1,3,15", "2,3,100"]
  loads = ["0,3,100", "0,1,10", "0,2,60", "1,3,10", "2,3,60"]
  start = 0
  end = 4







