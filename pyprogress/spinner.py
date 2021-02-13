class ProgressSpinner():
    """
    Define a spinning progress indicator.
    """

    states = ['-', '\\', '|', '/']

    def __init__(self, description='', state=0):
        """Initialize starting position"""
        self.description = description
        self.state = state

    def next(self):
        """Advance spinner by one step and print bar"""
        self.state = (self.state + 1) % 4
        self.__print()

    def __print(self):
        """Calculate current spinner step"""
        print(f"{self.description}{' ' if self.description != '' else ''}{self.states[self.state]}", end='\r')