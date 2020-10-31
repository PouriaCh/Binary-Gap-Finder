class BinGapFinder:
    def __init__(self, N) -> None:
        self.N = N

    #  numToBinary

    # def solution (N):
    #     return False

    if __name__ == "__main__":
        binGapsList = []
        firstOne = False
        lastOne = False
        gapLength = 0

        N = input("Please enter a number: ")
        # N= 85
        # obj = BinGapFinder(N)
        binaryN = bin(int(N)).replace("0b","")
        print("The binary representation of", N , ":", binaryN)
        print(len(binaryN))

        if (len(binaryN) < 3): 
            binGapsList.append(gapLength)
        else:
            binaryN = binaryN[1:] # skip the first one
            
            # loop over the rest of bits
            for index in range(1,len(binaryN)):
                if (binaryN[index] == "0"):
                    gapLength += 1
                    firstOne = True
                elif (binaryN[index] == "1" and firstOne and ~lastOne):
                    firstOne = False
                    lastOne = True
                    binGapsList.append(gapLength)
                    gapLength = 0
                elif (binaryN[index] == "1" and ~firstOne and lastOne):
                    firstOne = True
                    lastOne = False
                    gapLength = 0

        if (binGapsList == []):
            print("The binary gap is: 0")
        else:
            print("The binary gap is:",max(binGapsList))
