class myClass():
    def __init__(self, myList):
        self.myList = myList

    def square(self):
        # Create a new list
        newList = []

        # Loop through each number in the list
        for num in self.myList:
            # Square each number
            num = num**2
            # Add the new numbers to the new list 
            newList.append(num)

        # Save the new list as output
        return newList
