import java.util.List;

public class Main {

    private static Integer min (List<Integer> list){
        Integer min = null;
        if (list != null &&!list.isEmpty()){
            min = Integer.MAX_VALUE;

            for(Integer num : list){
                if(num < min) {
                    min = num;
                }
            }
        }
        return min;
    }

    public static void main(String[] args) {

        List<Integer> list = List.of(1, 2, 3, -1, 5);
        Integer rightAnswer = -1;

        Integer answer = min(list);

        if (answer.equals(rightAnswer)) {
            System.out.println("Тест пройден");
        }else {
            System.out.println("Тест не пройден");
        }
    }
}