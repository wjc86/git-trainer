"""
What if the print() function was less useful? Let's make that dream a reality
"""

p=print #copy the built in print function for our uses


class print:
    """
    Our overloaded fancy printer
    """

    def __init__(self):
        """
        Put variables you'll need here
        """
        self.call_count = 0
        print=self

    def __call__(self,x):
        """
        put behaviors you want to add here, be careful not to interrupt someone else's segments
        """
        if x='Hello There' # If Obi-Wan is programming, we should respond appropriately
            p('General Kenobi')

        if self.call_count%2 !=0: #If the function has been called an odd number of times
            """
            This wonderful overloaded print function only prints every other call, and condescends to you when it does
            """
            p("You're an odd one") #use p() instead of print to avoid recursion issues
            p(x)

        self.call_count+=1
print = print()


if __name__ == "__main__":
    """if you run this file directly, it'll do this
    """
    for i in range(0,7):
        print(i)
