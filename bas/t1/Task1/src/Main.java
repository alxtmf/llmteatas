import java.util.Scanner;

public class Main {

    public static String SplitUpAndMerge (String str1, String str2){
        int min = Math.min(str1.length(),str2.length());
        String s3 = "";
        for (int i = 0; i < min; i++){
            if (i % 2 == 0){
                char tmp = str1.charAt(i);
                s3 = s3 + tmp;
            }
            else {
                char tmp = str2.charAt(i);
                s3 = s3 + tmp;
            }

        }
        return s3;
    }



    public static void main(String[] args) {
        String str1_test = "Тестовая";
        String str2_test = "Строка";
        String exp_str = "Ттсооа";
        if(SplitUpAndMerge(str1_test,str2_test).equals(exp_str))
            System.out.println("Тест пройден");
        else
            System.out.println("Тест провален. Получено:" + SplitUpAndMerge(str1_test,str2_test) + ",Вместо:" + exp_str);
    }
}