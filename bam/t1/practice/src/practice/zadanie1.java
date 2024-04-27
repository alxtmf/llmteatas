package practice;
public class zadanie1 {
    public static double averageAfterMinAbsElement(double[] array) {
        int minIndex = 0;
        double minAbsValue = Math.abs(array[0]);
        for (int i = 1; i < array.length; i++) {
            if (Math.abs(array[i]) < minAbsValue) {
                minAbsValue = Math.abs(array[i]);
                minIndex = i;
            }
        }
        if (minIndex < array.length - 1) {
            double sum = 0;
            int count = 0;
            for (int i = minIndex + 1; i < array.length; i++) {
                sum += array[i];
                count++;
            }
            return sum / count;
        } else {
            return 0;
        }
    }
    public static void main(String[] args) {
        double[] testArray = {1.5, -2.5, 3.0, -4.0};
        double result = averageAfterMinAbsElement(testArray);
        System.out.println("Среднее арифметическое элементов после минимального по модулю элемента: " + result);
        double expectedResult = -3.5 / 3.0;
        double actualResult = averageAfterMinAbsElement(testArray);
        if (actualResult == expectedResult) {
            System.out.println("Тест пройден.");
        } else {
            System.out.println("Тест не пройден. Ожидалось: " + expectedResult + ", Получено: " + actualResult);
        }
    }
}
