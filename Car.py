class Car:

    def __init__(self, make, model, year, price):
        self.make = make.upper()
        self.model = model.upper()
        self.year = year
        self.price = price
    
    def __gt__(self, rhs):
        if self.make == rhs.make:
            if self.model == rhs.model:
                if self.year == rhs.year:
                    if self.price == rhs.price:
                        return False
                    else:
                        return self.price > rhs.price
                else:
                    return self.year > rhs.year
            else:
                return self.model > rhs.model
        else:
            return self.make > rhs.make
        
    def __lt__(self, rhs):
        if self.make == rhs.make:
            if self.model == rhs.model:
                if self.year == rhs.year:
                    if self.price == rhs.price:
                        return False
                    else:
                        return self.price < rhs.price
                else:
                    return self.year < rhs.year
            else:
                return self.model < rhs.model
        else:
            return self.make < rhs.make
        
    def __eq__(self, rhs):
        if self.make == rhs.make:
            if self.model == rhs.model:
                if self.year == rhs.year:
                    if self.price == rhs.price:
                        return True
        return False
    
    def __str__(self):
        return "Make: {}, Model: {}, Year: {}, Price: ${}".format(self.make, self.model, self.year, self.price)
        
