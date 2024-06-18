package org.example;

import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        String str = "привет, мир!";
        String expectedStr = "веиимп, ррт!";
        String sortedStr = sortString(str);
        if (expectedStr.equals(sortedStr)) {
            System.out.println(sortedStr);
            System.out.println("Тест пройден");
        }
        else {
            System.out.println("Тест не пройден");
        }
    }

    public static String sortString(String str) {
        char[] chars = str.toCharArray();
        char[] sortedChars = new char[chars.length];

        int j = 0;
        for (int i = 0; i < chars.length; i++) {
            if (Character.isLetter(chars[i])) {
                sortedChars[j++] = chars[i];
            }
        }

        Arrays.sort(sortedChars, 0, j);

        StringBuilder sb = new StringBuilder();
        j = 0;
        for (int i = 0; i < chars.length; i++) {
            if (Character.isLetter(chars[i])) {
                sb.append(sortedChars[j++]);
            } else {
                sb.append(chars[i]);
            }
        }

        return sb.toString();
    }
}