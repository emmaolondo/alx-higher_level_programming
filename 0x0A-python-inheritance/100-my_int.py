#!/usr/bin/python3
""" Defining MyInt class that inherites from int """


class MyInt(int):
    """" MyInt that inherites from int """
    def __int__(self, myint):
        """ Initializizing myint variable """
        self.myint = myint

    @property
    def myint(self):
        """ getting the int value using getter method """
        return self.myint

    @myint.setter
    def myint(self, myint):
        if type(myint) is not int:
            raise TypeError("the value must be an integer")
        else:
            self.myint = myint

    def __eq__(self, other):
        """ using the equal method """
        if self.myint == other:
            return False
        else:
            return True

    def __ne__(self, other):
        """ The not eaual method """
        if self.myint != other:
            return False
        else:
            return True
