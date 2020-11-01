import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

class BinaryGapFinder {
    // class Solution {
    //     // public int solution(int N);
    // } 

    public static String numToBinary() {
        Scanner myScanner = new Scanner(System.in);
        System.out.println("Please enter a number: ");
        int N = myScanner.nextInt();
        myScanner.close();
        return Integer.toBinaryString(N);
    }

    public static void main(String[] args) {
        
        ArrayList<Integer> binGapsList = new ArrayList<Integer>();
        boolean firstOne = false, lastOne = false;
        int gapLength = 0;

        String binRepString = numToBinary();
        System.out.println("The binary representation of N: " + binRepString.toString());
        
        // eliminate the first "1" 
        binRepString = binRepString.substring(1);
        char[] binRepCharSet = binRepString.toCharArray();
        

        for (char numChar : binRepCharSet) {
            switch (numChar) {
                case '0':
                   gapLength += 1;
                   firstOne = true;
                   break;
                case '1':
                    if (firstOne && !lastOne) {
                        firstOne = false;
                        lastOne = true;
                        binGapsList.add(gapLength);
                    } 
                    else if (!firstOne && lastOne){
                        firstOne = true;
                        lastOne = false;
                    }
                    gapLength = 0;
                    break;
            }
        }

        if (binGapsList.isEmpty()) {
            System.out.println("The binary gap is: 0");
        }
        else {
            System.out.println("The binary gap is: " + Collections.max(binGapsList));
        }

    }
}