import java.util.Scanner;
 public class Integers{
  public static void main(String[] args){
   Scanner reader = new Scanner(System.in);
   System.out.print("Enter three digits: ");
   int number = reader.nextInt();
   
   int digit1 = (number)/100;
   int digit2 = ((number)/10)%10;
   int digit3 = (number)%10;
   if(digit1 == digit3){
    System.out.printf("%d is a palindrome", number);
   }
   else if(digit1 != digit3){
   System.out.printf("%d is not a palindrome", number);
   }
  }
 }

   
   