//Дана целочисленная матрица A(N, N). Вычислите сумму и число элементов матрицы, находящихся под главой диагональю.

public class Main {
    public static void main(String[] args) {
        int[][] matrix = {
                {10, 20, 30, 40},
                {50, 60, 70, 80},
                {90, 100, 110, 120},
                {130, 140, 150, 160}
        };
        int expectedSum = 660;
        int expectedCount = 6;

        System.out.println("Сгенерированная матрица:");
        for (int[] ints : matrix) {
            for (int j = 0; j < matrix.length; j++) {
                System.out.print(ints[j] + "\t");
            }
            System.out.println();
        }

        int sum = sumUnderDiag(matrix);
        System.out.println("Сумма элементов под главной диагональю: " + sum + "\tОжидаемая сумма: " + expectedSum);

        int count = countUnderDiag(matrix);
        System.out.println("Количество элементов под главной диагональю: " + count + "\tОжидаемое кол-во: " + expectedCount);

        if(expectedCount == count && expectedSum == sum){
            System.out.println("Тест пройден");
        }
        else{
            System.out.println("Тест не пройден");
        }
    }
    public static int sumUnderDiag(int[][] matrix) {
        int sum = 0;
        for (int i = 1; i < matrix.length; i++) {
            for (int j = 0; j < i; j++) {
                sum += matrix[i][j];
            }
        }
        return sum;
    }

    public static int countUnderDiag(int[][] matrix) {
        int count = 0;
        for (int i = 1; i < matrix.length; i++) {
            count += i;
        }
        return count;
    }
}

