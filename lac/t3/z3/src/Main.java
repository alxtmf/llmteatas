//Дана строка. Отсортируйте все символы в строке, удалив пробелы.

import java.util.Objects;

public class Main {
    public static void main(String[] args) {
        equals("0123456789", sortString("9876543210"));
        equals("Hdellloorw", sortString("Hello world"));
        equals("()+-01233457779", sortString("+7 (914) 052 73-73"));
    }

    public static void equals(String expectedStr, String str){
        if(Objects.equals(expectedStr, str)){
            System.out.println("Тест пройден");
        }
        else{
            System.out.println("Тест не пройден\tОжидаемая строка: " + str);
        }
    }

    public static String sortString(String inputString) {
        char[] array = inputString.replaceAll("\\s", "").toCharArray();
        java.util.Arrays.sort(array);
        return new String(array);
    }
}
