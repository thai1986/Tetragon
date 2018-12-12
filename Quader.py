# Status:
#   0: unset
#   1: left
#   2: right
#   3: set
#   4: set and print
class Quader:
    def __init__(self, index):
        self.Index = index
        self.LeftPos = index*4 + 1
        self.RightPos = index*4 + 3
        self.LeftBraille = [0,0,0]
        self.RightBraille = [0,0,0]
        self.Status = 0

    def updateStatus(self,status):
        if self.Status == 0 or self.Status == 3 or self.Status == 4:
            self.Status = status
        elif self.Status == 1 and status == 2:
            self.Status = 3
        elif self.Status == 2 and status == 1:
            self.Status = 3
        return

    def setBraille(self,braille, pos):
        if pos == 1:
            for i in range(0,3):
                if braille[i] == 1:
                    self.LeftBraille[i] = 1
        if pos == 2:
            for i in range(0,3):
                if braille[i] == 1:
                    self.RightBraille[i] = 1
        return

