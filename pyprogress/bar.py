class ProgressBar():
    """
    Define a fixed length progress bar.
    Can be advanced one step at a time or to a given position.
    Inverse allows to count remaining steps instead of current progress.
    """

    def __init__(self, max_value, length=20, description='',
                 inverse=False, bar_char='█', empty_char=' '):
        """Initialize values and optional parameters"""
        self.current = 0
        self.total = max_value
        self.length = length
        self.description = description
        self.inverse = inverse
        self.bar_char = bar_char
        self.empty_char = empty_char
    
    def next(self):
        """Advance current one step and print bar"""
        if not self.inverse:
            self.current += 1
        else:
            self.current -= 1
        self.__print()
    
    def set_current(self, current):
        """Advance current to a set position and print bar"""
        self.current = current
        self.__print()
    
    def finalize(self):
        """Print bar without carriage return"""
        self.__print(final=True)
    
    def __print(self, final=False):
        """Calculate progress and print a bar"""
        progress = int((self.current / self.total) * 100)
        if self.inverse:
            progress = 100 - progress
        step = int(progress * self.length / 100)
        bar = self.bar_char * step + self.empty_char * (self.length - step)
        if not final:
            print(f"{progress:>3}% |{bar}|{' ' if self.description != '' else ''}{self.description}", end='\r')
        else:
            print(f"{progress:>3}% |{bar}|{' ' if self.description != '' else ''}{self.description}")