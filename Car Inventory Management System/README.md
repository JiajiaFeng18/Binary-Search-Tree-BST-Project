# Car Inventory Management System

## Overview
This project is a Python-based **Car Inventory Management System** that utilizes a Binary Search Tree (BST) structure to manage a collection of cars. The system allows users to efficiently add, update, search for, and remove cars from the inventory based on key attributes such as make, model, year, and price. Additionally, the system supports multiple traversal methods to display the inventory in different orders.

## Features
- **Add Cars**: Insert new cars into the inventory while maintaining the Binary Search Tree structure for efficient searching.
- **Search for Cars**: Find cars by make, model, year, or price, and retrieve information about the best and worst options available.
- **Update Car Information**: Modify the details of a car, including make, model, year, and price.
- **Remove Cars**: Delete cars from the inventory while preserving the integrity of the BST.
- **Inventory Traversal**: Display the inventory using in-order, pre-order, or post-order traversal.
- **Calculate Total Price**: Calculate the total price of all cars in the inventory.

## File Structure
- **Car.py**: Defines the `Car` class, representing individual cars with attributes such as make, model, year, and price.
- **CarInventoryNode.py**: Implements the node structure for the Binary Search Tree (BST) used to store and manage cars.
- **CarInventory.py**: Contains the main class for managing the car inventory using a BST, with methods for adding, searching, removing, and traversing cars.
- **testFile.py**: Includes unit tests for validating key functionalities of the system, such as car comparisons, additions, removals, and traversals.

## How to Use
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/car_inventory_system.git
   ```
2. **Navigate to the Project Directory**:
   ```bash
   cd car_inventory_system
   ```
3. **Run the System**:
   You can create a script to interact with the `CarInventory` class or directly run the `CarInventory.py` file to add, update, or remove cars from the inventory.

4. **Unit Testing**:
   Run the test file to ensure that all functions behave as expected:
   ```bash
   python testFile.py
   ```

## Prerequisites
- **Python 3.x**: Ensure that Python is installed on your system.

## Future Enhancements
- **User Interface**: Implement a graphical or command-line interface to make the system more user-friendly.
- **Advanced Search**: Add functionality to search for cars using more complex filters, such as price range, mileage, or condition.
- **Data Persistence**: Allow the system to save and load car inventories from files, enabling data to persist across sessions.
