package practice;
import java.util.Arrays;
public class zadanie2 {
    public static String[] splitString(String input) {
        return input.split("[\\s.,!?:;]+");
    }

    public static void main(String[] args) {
        String input = "Привет, всем! Это юнит тест.";
        String[] expectedWords = {"Привет", "всем", "Это", "юнит", "тест"};
        String[] actualWords = splitString(input);
        
        if (Arrays.equals(expectedWords, actualWords)) {
            System.out.println("Тест пройден.");
        } else {
            System.out.println("Тест не пройден.");
        }
    }
}
