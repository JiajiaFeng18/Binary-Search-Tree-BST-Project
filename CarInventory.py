from Car import Car
from CarInventoryNode import CarInventoryNode


class CarInventory:
    def __init__(self):
        self.root = None
    
    def addCar(self, car):
        if self.root == None:
            self.root = CarInventoryNode(car)
        else:
            self._addCar(car, self.root)

    def _addCar(self, car, currentNode):
        if car.make == currentNode.make and car.model == currentNode.model:
            currentNode.cars.append(car)
        elif car < currentNode.cars[0]:
            if currentNode.left != None:
                self._addCar(car, currentNode.left)
            else:
                currentNode.left = CarInventoryNode(car)
                currentNode.left.parent = currentNode
        else:
            if currentNode.right != None:
                self._addCar(car, currentNode.right)
            else:
                currentNode.right = CarInventoryNode(car)
                currentNode.right.parent = currentNode

    def doesCarExist(self, car):
        return self._doesCarExist(car, self.root)
        
    def _doesCarExist(self, car, currentNode):
        if currentNode == None:
            return False
        elif car.make == currentNode.make and car.model == currentNode.model:
            for i in currentNode.cars:
                if car == i:
                    return True
            return False
        else:
            if car < currentNode.cars[0]:
                return self._doesCarExist(car, currentNode.left)

            else:
                return self._doesCarExist(car, currentNode.right)


    def inOrder(self):
        if self.root == None:
            return ""
        return self._inOrder(self.root)

    def _inOrder(self, currentNode):
        details = ""
        if currentNode == None:
            return details
        details += self._inOrder(currentNode.left)
        details += currentNode.__str__()
        details += self._inOrder(currentNode.right)
        return details
    
    def preOrder(self):
        if self.root == None:
            return ""
        return self._preOrder(self.root)

    def _preOrder(self, currentNode):
        details = ""
        if currentNode == None:
            return details
        details += currentNode.__str__()
        details += self._preOrder(currentNode.left)
        details += self._preOrder(currentNode.right)
        return details
    
    def postOrder(self):
        if self.root == None:
            return ""
        return self._postOrder(self.root)

    def _postOrder(self, currentNode):
        details = ""
        if currentNode == None:
            return details
        details += self._postOrder(currentNode.left)
        details += self._postOrder(currentNode.right)
        details += currentNode.__str__()
        return details
    
    def getBestCar(self, make, model):
        return self._getBestCar(make.upper(), model.upper(), self.root)

    def _getBestCar(self, make, model, currentNode):
        if currentNode == None:
            return None
        elif make == currentNode.make and model == currentNode.model:
            temp = [currentNode.cars[0]]
            for i in currentNode.cars:
                if i.year > temp[0].year:
                    temp = [i]
                elif i.year == temp[0].year:
                    temp.append(i)
            if len(temp) == 1:
                return temp[0]
            max = temp[0]
            for i in temp:
                if i.price > max.price:
                    max = i
            return max
        else:
            if make < currentNode.make or (make == currentNode.make and model < currentNode.model):
                return self._getBestCar(make, model, currentNode.left)
            else:
                return self._getBestCar(make, model, currentNode.right)

    def getWorstCar(self, make, model):
        return self._getWorstCar(make.upper(), model.upper(), self.root)

    def _getWorstCar(self, make, model, currentNode):
        if currentNode == None:
            return None
        elif make == currentNode.make and model == currentNode.model:
            temp = [currentNode.cars[0]]
            for i in currentNode.cars:
                if i.year < temp[0].year:
                    temp = [i]
                elif i.year == temp[0].year:
                    temp.append(i)
            if len(temp) == 1:
                return temp[0]
            min = temp[0]
            for i in temp:
                if i.price < min.price:
                    min = i
            return min
        else:
            if make < currentNode.make or (make == currentNode.make and model < currentNode.model):
                return self._getWorstCar(make, model, currentNode.left)
            else:
                return self._getWorstCar(make, model, currentNode.right)

    def getTotalInventoryPrice(self):
        return self._getTotalInventoryPrice(self.root)

    def _getTotalInventoryPrice(self, currentNode):
        total = 0
        if currentNode == None:
            return total
        total += self._getTotalInventoryPrice(currentNode.left)
        for i in currentNode.cars:
            total += i.price
        total += self._getTotalInventoryPrice(currentNode.right)
        return total


    def getSuccessor(self, make, model):
        make = make.upper()
        model = model.upper()

        currentNode = self._getSuccessor(make, model, self.root)

        if currentNode == None:
            return None
    
        if currentNode.right == None:
            current = currentNode.parent
            while current != None:
                if current.make > make or (current.make == make and current.model > model):
                    return current 
                current = current.parent
            return None
        else:
            current = currentNode.right
            while current.left != None:
                current = current.left
            return current

    def _getSuccessor(self, make, model, currentNode):
        if currentNode == None:
            return None
        
        elif make == currentNode.make and model == currentNode.model:
            return currentNode
        
        else:
            if currentNode.make < make:
                return self._getSuccessor(make, model, currentNode.right)
            elif currentNode.make == make and currentNode.model < model:
                return self._getSuccessor(make, model, currentNode.right)
            else:
                return self._getSuccessor(make, model, currentNode.left)
            

    def removeCar(self, make, model, year, price):
        make = make.upper()
        model = model.upper()

        car = Car(make, model, year, price)
        currentNode = self._getSuccessor(make, model, self.root)
       
        if currentNode == None:
            return False
        else:
            currentNode.cars.remove(car)
            if len(currentNode.cars) == 0:
                self._removeNode(make, model, currentNode)
                
            return True
        
    def _removeNode(self, make, model, currentNode):
        #Case 2: remove leaf node
        if currentNode.left == None and currentNode.right == None:
            if currentNode.parent == None:
                self.root = None
            elif currentNode.parent.left == currentNode:
                currentNode.parent.left = None
            else:
                currentNode.parent.right = None

        #Case 3: remove node with one child
        #left child
        elif currentNode.left != None and currentNode.right == None:
            if currentNode.parent == None:
                currentNode.left.parent = None
                self.root = currentNode.left
            #parent's left side
            elif currentNode.parent.left == currentNode:
                currentNode.parent.left = currentNode.left
                currentNode.left.parent = currentNode.parent
            #parent's right side
            else:
                currentNode.parent.right = currentNode.left
                currentNode.left.parent = currentNode.parent

        #right child
        elif currentNode.right != None and currentNode.left == None:
            if currentNode.parent == None:
                currentNode.right.parent = None
                self.root = currentNode.right
            #parent's left side
            elif currentNode.parent.left == currentNode:
                currentNode.parent.left = currentNode.right
                currentNode.right.parent = currentNode.parent
            #parent's right side
            else:
                currentNode.parent.right = currentNode.right
                currentNode.right.parent = currentNode.parent

        #Case 4: remove node with 2 children
        elif currentNode.right != None and currentNode.left != None:
            successor = self.getSuccessor(make, model)
            currentNode.cars = successor.cars
            currentNode.make = successor.make
            currentNode.model = successor.model
            self._removeNode(make, model, successor)



          