import java.util.Arrays;

public class Main {
    public static String[] SortByJumper (String [] array){
        int N = array.length;
        String tempStr;
        for (int k = 0; k < array.length - 1; k++) {
            for (int i= 0; i < array.length - k -1; i++) {
                if(array[i+1].length() > array[i].length()) {
                    tempStr = array[i];
                    array[i] = array[i + 1];
                    array[i + 1] = tempStr;
                }
            }
        }
        return array;
    }

    public static void main(String[] args) {
     String [] array = {"Aaaaa","AAAA","aaa","aaaaaaa"};
     String [] wr_array = SortByJumper(array);
     String [] test_array = {"aaaaaaa","Aaaaa","AAAA","aaa"};
     for (int i = 0; i < wr_array.length; i++){
         System.out.println(wr_array[i]);
     }
     if (Arrays.equals(test_array, wr_array))
         System.out.println("Тест пройден");
     else
         System.out.println("Тест не пройден");
    }
}