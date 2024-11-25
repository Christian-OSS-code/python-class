import java.util.Scanner;
    public class PalindromeChecker{
        public static void main(String[] args){
            palindromeCheck(word);
        }
        public static boolean palindromeCheck(String[] letter){
            Scanner input = new Scanner(System.in);
            String word = System.out.println("Enter the word: ");
            int count1 = 0;
            int count2 = word.length - 1
            while (count1 < count2){
                if (word.charAt(count1) != word.charAt(count2)){
                    return false; 

                }
                
            }
            return true;
    

        } 

    }

        
