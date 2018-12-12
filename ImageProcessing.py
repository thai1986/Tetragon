import numpy as np
class ImageProcessing:
    def __init__(self, array, SIZE, LINE, THRESHOLD, GRAY_CODE_SIZE):
        self.G1Pos = 134
        self.G2Pos = 158
        self.G3Pos = 186
        self.G4Pos = 496
        self.G5Pos = 518
        self.G6Pos = 542
        self.G7Pos = 568
        self.B1Pos = 266
        self.B2Pos = 360
        self.B3Pos = 446
        self.G1Val = 0 if np.mean(array[(LINE-SIZE):(LINE+SIZE),(self.G1Pos-SIZE):(self.G1Pos+SIZE)]) < THRESHOLD else 1
        self.G2Val = 0 if np.mean(array[(LINE-SIZE):(LINE+SIZE),(self.G2Pos-SIZE):(self.G2Pos+SIZE)]) < THRESHOLD else 1
        self.G3Val = 0 if np.mean(array[(LINE-SIZE):(LINE+SIZE),(self.G3Pos-SIZE):(self.G3Pos+SIZE)]) < THRESHOLD else 1
        self.G4Val = 0 if np.mean(array[(LINE-SIZE):(LINE+SIZE),(self.G4Pos-SIZE):(self.G4Pos+SIZE)]) < THRESHOLD else 1
        self.G5Val = 0 if np.mean(array[(LINE-SIZE):(LINE+SIZE),(self.G5Pos-SIZE):(self.G5Pos+SIZE)]) < THRESHOLD else 1
        self.G6Val = 0 if np.mean(array[(LINE-SIZE):(LINE+SIZE),(self.G6Pos-SIZE):(self.G6Pos+SIZE)]) < THRESHOLD else 1
        self.G7Val = 0 if np.mean(array[(LINE-SIZE):(LINE+SIZE),(self.G7Pos-SIZE):(self.G7Pos+SIZE)]) < THRESHOLD else 1
        self.B1Val = 0 if np.mean(array[(LINE-SIZE):(LINE+SIZE),(self.B1Pos-SIZE):(self.B1Pos+SIZE)]) < THRESHOLD else 1
        self.B2Val = 0 if np.mean(array[(LINE-SIZE):(LINE+SIZE),(self.B2Pos-SIZE):(self.B2Pos+SIZE)]) < THRESHOLD else 1
        self.B3Val = 0 if np.mean(array[(LINE-SIZE):(LINE+SIZE),(self.B3Pos-SIZE):(self.B3Pos+SIZE)]) < THRESHOLD else 1
        self.GRAY_CODE_SIZE = GRAY_CODE_SIZE
        self.GrayCode = [self.G1Val,self.G2Val,self.G3Val,self.G4Val,self.G5Val,self.G6Val,self.G7Val]
        self.BrailleCode = [self.B1Val,self.B2Val,self.B3Val]
        self.array = array
        self.SIZE = SIZE
        self.LINE = LINE

    def grayToBinary(self):
        gray = [self.G7Val,self.G6Val,self.G5Val,self.G4Val,self.G3Val,self.G2Val,self.G1Val]
        binary = [0,0,0,0,0,0,0]
        binary[0] = gray[0]
        for i in range(1,self.GRAY_CODE_SIZE):
            if gray[i] == binary[i-1]:
                binary[i] = 0
            else:
                binary[i] = 1     
        return binary

    def binaryToDecimal(self):
        binary = self.grayToBinary()
        dec = 0
        for i in range(0,self.GRAY_CODE_SIZE):
            if binary[i] == 1:
                dec = dec + 2**(self.GRAY_CODE_SIZE-1-i)
        return dec

    def imageDisplay(self):
        self.array[(self.LINE-self.SIZE):(self.LINE+self.SIZE),(self.G1Pos-self.SIZE):(self.G1Pos+self.SIZE)].fill(255)
        self.array[(self.LINE-self.SIZE):(self.LINE+self.SIZE),(self.G2Pos-self.SIZE):(self.G2Pos+self.SIZE)].fill(255)
        self.array[(self.LINE-self.SIZE):(self.LINE+self.SIZE),(self.G3Pos-self.SIZE):(self.G3Pos+self.SIZE)].fill(255)
        self.array[(self.LINE-self.SIZE):(self.LINE+self.SIZE),(self.G4Pos-self.SIZE):(self.G4Pos+self.SIZE)].fill(255)
        self.array[(self.LINE-self.SIZE):(self.LINE+self.SIZE),(self.G5Pos-self.SIZE):(self.G5Pos+self.SIZE)].fill(255)
        self.array[(self.LINE-self.SIZE):(self.LINE+self.SIZE),(self.G6Pos-self.SIZE):(self.G6Pos+self.SIZE)].fill(255)
        self.array[(self.LINE-self.SIZE):(self.LINE+self.SIZE),(self.G7Pos-self.SIZE):(self.G7Pos+self.SIZE)].fill(255)
        self.array[(self.LINE-self.SIZE):(self.LINE+self.SIZE),(self.B1Pos-self.SIZE):(self.B1Pos+self.SIZE)].fill(255)
        self.array[(self.LINE-self.SIZE):(self.LINE+self.SIZE),(self.B2Pos-self.SIZE):(self.B2Pos+self.SIZE)].fill(255)
        self.array[(self.LINE-self.SIZE):(self.LINE+self.SIZE),(self.B3Pos-self.SIZE):(self.B3Pos+self.SIZE)].fill(255)
        return self.array

    def printInfo(self):
        print('Gray: {}:{}   Braille: {}'.format(str(self.GrayCode),str(self.binaryToDecimal()),str(self.BrailleCode)))
        return        
