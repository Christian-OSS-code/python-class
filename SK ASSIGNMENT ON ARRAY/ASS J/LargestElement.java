 public class LargestElement{
   
    public static int largestElement(int[] numberList){
        int largestElement = numberList[0];
        for (int count = 0; count < numberList.length; count ++){

            if (numberList[count] > largestElement){
                largestElement = numberList[count];


            }

        }
        return largestElement;
    }
    public static void main(String[] args){
        int[] numberList = {1, 4, 5, 2, 9};
        System.out.println(largestElement(numberList));




    }   

}
