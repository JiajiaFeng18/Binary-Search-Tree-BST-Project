import pytest
from Car import Car
from CarInventoryNode import CarInventoryNode
from CarInventory import CarInventory

def test_Car():
    c1 = Car("Honda", "CRV", 2007, 8000)
    c2 = Car("Toyota", "RAV4", 2022, 37000)
    c3 = Car("Honda", "CRV", 2018, 26000)
    c4 = Car('Toyota', 'Camry', 2021, 25000)
    c5 = Car("Honda", "CRV", 2007, 8000)
    assert c1 < c3
    assert c2 > c1
    assert c3 < c2
    assert not c2 < c4 
    assert c1 == c5


def test_CarInventoryNode():
    car = Car("Honda", "CRV", 2007, 8000)
    node = CarInventoryNode(car)

    assert node.getMake() == "HONDA"
    assert node.getModel() == "CRV"

    assert node.getParent() == None

    car_parent = Car("Toyota", "RAV4", 2022, 37000)
    node_parent = CarInventoryNode(car_parent)
    node.setParent(node_parent)
    assert node.getParent() == node_parent

    car_left = Car("Ford", "Fusion", 2010, 9000)
    node_left = CarInventoryNode(car_left)
    node.setLeft(node_left)
    assert node.getLeft() == node_left

    car_right = Car("Tesla", "Model 3", 2022, 50000)
    node_right = CarInventoryNode(car_right)
    node.setRight(node_right)
    assert node.getRight() == node_right

    assert str(node) == "Make: HONDA, Model: CRV, Year: 2007, Price: $8000\n"

def test_CarInventory1():
    bst = CarInventory()
    car1 = Car("Toyota", "Prius", 2017, 18000)
    car2 = Car("Tesla", "ModelS", 2022, 65000)
    car3 = Car("BMW", "X3", 2021, 42000)
    car4 = Car("BMW", "X3", 2013, 20000)
    car5 = Car("Chevrolet", "Silverado", 2021, 28000)

    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)

    car6 = Car("Chevrolet", "Silverado", 1999, 10000)

    assert bst.doesCarExist(car6) == False

    assert bst.getBestCar("Toyota", "Prius") == car1
    assert bst.getBestCar("BMW", "X3") == car3
    assert bst.getBestCar("Honda", "Accord") == None

    assert bst.getWorstCar("Toyota", "Prius") == car1
    assert bst.getWorstCar("BMW", "X3") == car4
    assert bst.getWorstCar("Honda", "Accord") == None

    assert bst.inOrder() == \
"""\
Make: BMW, Model: X3, Year: 2021, Price: $42000
Make: BMW, Model: X3, Year: 2013, Price: $20000
Make: CHEVROLET, Model: SILVERADO, Year: 2021, Price: $28000
Make: TESLA, Model: MODELS, Year: 2022, Price: $65000
Make: TOYOTA, Model: PRIUS, Year: 2017, Price: $18000
"""
    assert bst.preOrder() == \
"""\
Make: TOYOTA, Model: PRIUS, Year: 2017, Price: $18000
Make: TESLA, Model: MODELS, Year: 2022, Price: $65000
Make: BMW, Model: X3, Year: 2021, Price: $42000
Make: BMW, Model: X3, Year: 2013, Price: $20000
Make: CHEVROLET, Model: SILVERADO, Year: 2021, Price: $28000
"""
    assert bst.postOrder() == \
"""\
Make: CHEVROLET, Model: SILVERADO, Year: 2021, Price: $28000
Make: BMW, Model: X3, Year: 2021, Price: $42000
Make: BMW, Model: X3, Year: 2013, Price: $20000
Make: TESLA, Model: MODELS, Year: 2022, Price: $65000
Make: TOYOTA, Model: PRIUS, Year: 2017, Price: $18000
"""

    assert bst.getTotalInventoryPrice() == 173000


def test_CarInventory2():
    bst = CarInventory()
    car1 = Car("Nissan", "Leaf", 2018, 18000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("Mercedes", "Sprinter", 2022, 40000)
    car4 = Car("Mercedes", "Sprinter", 2014, 25000)
    car5 = Car("Ford", "Ranger", 2021, 25000)

    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)

    car6 = Car("Ford", "Ranger", 2000, 25000)

    assert bst.doesCarExist(car6) == False

    assert bst.getBestCar("Nissan", "Leaf") == car1
    assert bst.getBestCar("Mercedes", "Sprinter") == car3
    assert bst.getBestCar("Honda", "Accord") == None

    assert bst.getWorstCar("Nissan", "Leaf") == car1
    assert bst.getWorstCar("Mercedes", "Sprinter") == car4
    assert bst.getBestCar("Honda", "Accord") == None

    assert bst.inOrder() == \
"""\
Make: FORD, Model: RANGER, Year: 2021, Price: $25000
Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000
Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000
Make: NISSAN, Model: LEAF, Year: 2018, Price: $18000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
"""
    assert bst.preOrder() == \
"""\
Make: NISSAN, Model: LEAF, Year: 2018, Price: $18000
Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000
Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000
Make: FORD, Model: RANGER, Year: 2021, Price: $25000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
"""
    assert bst.postOrder() == \
"""\
Make: FORD, Model: RANGER, Year: 2021, Price: $25000
Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000
Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
Make: NISSAN, Model: LEAF, Year: 2018, Price: $18000
"""

    assert bst.getTotalInventoryPrice() == 158000

def test_getSuccessor():
    bst = CarInventory()

    car1 = Car("Mazda", "CX-5", 2022, 25000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("BMW", "X5", 2022, 60000)
    car4 = Car("BMW", "X5", 2020, 58000)
    car5 = Car("Audi", "A3", 2021, 25000)

    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)

    assert bst.getSuccessor("Mazda", "CX-5").__str__() == car2.__str__()+"\n"
    assert bst.getSuccessor("Tesla", "Model3") == None
    assert bst.getSuccessor("BMW", "X5").__str__() == car1.__str__()+"\n"

def test_getSuccessor_new():
    bst = CarInventory()

    car1 = Car("Ford", "Fiesta", 2021, 20000)
    car2 = Car("Toyota", "Camry", 2020, 25000)
    car3 = Car("Honda", "Civic", 2022, 22000)
    car4 = Car("Hyundai", "Elantra", 2019, 18000)
    car5 = Car("Chevrolet", "Cruze", 2021, 21000)

    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)

    assert bst.getSuccessor("Ford", "Fiesta").__str__() == car3.__str__()+"\n"
    assert bst.getSuccessor("Toyota", "Camry") == None
    assert bst.getSuccessor("Honda", "Civic").__str__() == car4.__str__()+"\n"
    assert bst.getSuccessor("Hyundai", "Elantra").__str__() == car2.__str__()+"\n"
    assert bst.getSuccessor("Chevrolet", "Cruze").__str__() == car1.__str__()+"\n"




def test_removeCar():
    bst = CarInventory()
    car1 = Car("Ford", "Fiesta", 2021, 20000)
    car2 = Car("Toyota", "Camry", 2020, 25000)
    car3 = Car("Honda", "Civic", 2022, 22000)
    car4 = Car("Hyundai", "Elantra", 2019, 18000)
    car5 = Car("Chevrolet", "Cruze", 2021, 21000)

    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)

    bst.removeCar("Ford", "Fiesta", 2021, 20000)
    assert bst.inOrder() == \
"""\
Make: CHEVROLET, Model: CRUZE, Year: 2021, Price: $21000
Make: HONDA, Model: CIVIC, Year: 2022, Price: $22000
Make: HYUNDAI, Model: ELANTRA, Year: 2019, Price: $18000
Make: TOYOTA, Model: CAMRY, Year: 2020, Price: $25000
"""
    assert bst.preOrder() == \
"""\
Make: HONDA, Model: CIVIC, Year: 2022, Price: $22000
Make: CHEVROLET, Model: CRUZE, Year: 2021, Price: $21000
Make: TOYOTA, Model: CAMRY, Year: 2020, Price: $25000
Make: HYUNDAI, Model: ELANTRA, Year: 2019, Price: $18000
"""
    assert bst.postOrder() == \
"""\
Make: CHEVROLET, Model: CRUZE, Year: 2021, Price: $21000
Make: HYUNDAI, Model: ELANTRA, Year: 2019, Price: $18000
Make: TOYOTA, Model: CAMRY, Year: 2020, Price: $25000
Make: HONDA, Model: CIVIC, Year: 2022, Price: $22000
"""

    bst.removeCar("Chevrolet", "Cruze", 2021, 21000)
    assert bst.inOrder() == \
"""\
Make: HONDA, Model: CIVIC, Year: 2022, Price: $22000
Make: HYUNDAI, Model: ELANTRA, Year: 2019, Price: $18000
Make: TOYOTA, Model: CAMRY, Year: 2020, Price: $25000
"""
    assert bst.preOrder() == \
"""\
Make: HONDA, Model: CIVIC, Year: 2022, Price: $22000
Make: TOYOTA, Model: CAMRY, Year: 2020, Price: $25000
Make: HYUNDAI, Model: ELANTRA, Year: 2019, Price: $18000
"""
    assert bst.postOrder() == \
"""\
Make: HYUNDAI, Model: ELANTRA, Year: 2019, Price: $18000
Make: TOYOTA, Model: CAMRY, Year: 2020, Price: $25000
Make: HONDA, Model: CIVIC, Year: 2022, Price: $22000
"""

    bst.removeCar("Toyota", "Camry", 2020, 25000)
    assert bst.inOrder() == \
"""\
Make: HONDA, Model: CIVIC, Year: 2022, Price: $22000
Make: HYUNDAI, Model: ELANTRA, Year: 2019, Price: $18000
"""
    assert bst.preOrder() == \
"""\
Make: HONDA, Model: CIVIC, Year: 2022, Price: $22000
Make: HYUNDAI, Model: ELANTRA, Year: 2019, Price: $18000
"""
    assert bst.postOrder() == \
"""\
Make: HYUNDAI, Model: ELANTRA, Year: 2019, Price: $18000
Make: HONDA, Model: CIVIC, Year: 2022, Price: $22000
"""






