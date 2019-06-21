from pip._vendor.distlib.compat import raw_input


class GroupNumbers:

    def __init__(self, input_list):
        self.input_list = input_list

    '''
    This method will return the first digit of the given number 
    which will be used as key for grouping the numbers
    '''
    def getFirstDigit1(self, number):
        while (number >= 10):
            number = number / 10
        return int(number)

    '''
    This method will group the numbers based on first digit 
    here the first digit of the number is used as key i.e 0 - 9
    if the dictionary already have the key value it will get
    the value(list object) for the key and appends the number to the list
    then updates the dictionary with new list object
    
    if the key is not found in the dictionary new list object will be 
    created and added to dictionary with corresponding key
    '''
	'''test'''
    def createGroupedNumberDict(self):
        myDict = {}
        for i in range(len(self.input_list)):
            number = self.input_list[i]
            index = self.getFirstDigit1(abs(int(number)))
            if index in myDict.keys():
                templist = myDict[index]
                templist.append(number)
                myDict.update({index: templist})
            else:
                templist = []
                templist.append(number)
                myDict.update({index: templist})
        return myDict


# main function
def main():
    # Getting comma seperated inputs from user
    input = raw_input("Enter the values seperated by comma ")

    '''
    Instantiate the GroupNumbers object by passing
    input list seperated by comma
    '''
    obj = GroupNumbers(input.split(','))

    '''
    Calling the method createGroupedNumberDict will return the dict object
    '''
    groupedDict = obj.createGroupedNumberDict()

    '''
    Print the values of the dictionary and keys were sorted in ascending 
    order so that grouped numbers will be printed in the ascending order
    '''
    for i in sorted(groupedDict.keys()):
        # values returned by keys were sorted and printed
        groupedDict[i].sort()
        print(groupedDict[i])


if __name__ == "__main__":
    main()
