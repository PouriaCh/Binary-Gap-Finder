import java.util.Scanner;

class BinaryGapFinder {
    class Solution {
        // public int solution(int N);
    } 

    public static String numToBinary() {
        Scanner myScanner = new Scanner(System.in);
        System.out.println("Please enter a number: ");
        int N = myScanner.nextInt();
        myScanner.close();
        return Integer.toBinaryString(N);
    }

    public static void main(String[] args) {
        
        String binRepString = numToBinary();
        System.out.println("The binary representation of N: " + binRepString.toString());
        char[] binRepCharSet = binRepString.toCharArray();
        
    }
}