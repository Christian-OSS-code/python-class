
public class ReversedList{
    public static void main(String[] args){

        System.out.println("The element in the number list is:");
        int[] numberList = {2, 3, 5, 7, 10, 12}; 
        printNumber(numberList);
        System.out.println("\nThe reverse of the element in number list array is:");
        printNumber(reverseElement(numberList));  


    }
    public static void printNumber(int[] numbers){
        for (int count = 0; count < numbers.length; count ++){
            System.out.print(numbers[count] + " ");
    
        }            

    }
    public static int[] reverseElement(int[] numbers){
        int[] reverse = new int[numbers.length];
  
        for (int count1 = 0, count2 = numbers.length - 1; count1 < numbers.length; count1 ++, count2 --){
            reverse[count2] = numbers[count1];            
        }
        return reverse;

    }
  }
