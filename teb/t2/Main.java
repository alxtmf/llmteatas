package org.example;

public class Main {
    public static void main(String[] args) {
        int[] array = {5, 4, 3, 2, 1};
        int result = isDescending(array);
        System.out.println(result);

        if(result == 1){
            System.out.println("Тест пройден");
        }
        else{
            System.out.println("Тест не пройден");
        }
    }
    public static int isDescending(int[] array) {
        for (int i = 0; i < array.length - 1; i++) {
            if (array[i] < array[i + 1]) {
                return 0;
            }
        }
        return 1;
    }

}