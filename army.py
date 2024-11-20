"""
This file will contain logic for the army system. This includes movement  
"""

class Army:
    def __init__(self, size):
        self.size = 0
        self.owner = 0
        self.power = 0

    def get_legal_moves(self):
        """
        Return all the possible legal moves the army can go from this position
        """
        raise NotImplementedError
    
    def move(self):
        """
        Move the army
        """
        raise NotImplementedError
