//Написать функцию, которая принимает строку. В качестве результата возвращает число символов в строке, которые не являются знаками препинания (.,!?-) и пробелом.

public class Main {
    public static void main(String[] args) {
        equals(0, countNonPunctuationChars(""));
        equals(0, countNonPunctuationChars(" "));
        equals(0, countNonPunctuationChars(".,!?-"));
        equals(6, countNonPunctuationChars("Привет"));
        equals(9, countNonPunctuationChars("Привет, мир!"));
        equals(20, countNonPunctuationChars("Как дела, друг? Все хорошо?"));
        equals(22, countNonPunctuationChars("Я люблю программирование"));
        equals(24, countNonPunctuationChars("Этот тест проверяет функцию"));
    }
    public static void equals(int expecterdCount, int count){
        if(count == expecterdCount){
            System.out.println("Тест пройден");
        }
        else{
            System.out.println("Тест не пройден\tЧисло символов: " + count);
        }
    }
    public static int countNonPunctuationChars(String str) {
        char[] punctuation = {'.', ',', '!', '?', '-', ' '};
        int count = 0;
        for (int i = 0; i < str.length(); i++) {
            char ch = str.charAt(i);
            boolean isPunctuation = false;
            for (char c : punctuation) {
                if (ch == c) {
                    isPunctuation = true;
                    break;
                }
            }
            if (!isPunctuation) {
                count++;
            }
        }
        return count;
    }
}