"""BinGapFinder"""


class BinGapFinder:
    """
    A binary gap within a positive integer N is any maximal sequence of consecutive zeros 
    that is surrounded by ones at both ends in the binary representation of N.
    """
    def __init__(self, number: int) -> None:
        self.number = number
        self.binary_gaps_list = []

    def find_binary_gap(self) -> int:

        gap_length = 0
        first_digit_one = False
        last_digit_one = False

        binary_number = bin(int(self.number)).replace("0b","")
        print("The binary representation of", self.number , ":", binary_number)
        
        for index in range(1,len(binary_number)):
            if (binary_number[index] == "0"):
                gap_length += 1
                first_digit_one = True
            elif (binary_number[index] == "1" and first_digit_one and ~last_digit_one):
                first_digit_one = False
                last_digit_one = True
                self.binary_gaps_list.append(gap_length)
                gap_length = 0
            elif (binary_number[index] == "1" and ~first_digit_one and last_digit_one):
                first_digit_one = True
                last_digit_one = False
                gap_length = 0

        if (self.binary_gaps_list == []):
            return 0
        return max(self.binary_gaps_list)


if __name__ == "__main__":
    number = input("Please enter a number: ")
    binary_gap_finder = BinGapFinder(number=number)
    result = binary_gap_finder.find_binary_gap()
    print(f"The binary gap is: {result}")
