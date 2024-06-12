import java.util.Random;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        System.out.print("Введите размерность матрицы: ");
        int n = new Scanner(System.in).nextInt();

        int[][] matrix = new int[n][n];
        Random random = new Random();

        System.out.println("Сгенерированная матрица:");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                matrix[i][j] = random.nextInt(100); // Генерируем случайное число от 0 до 99
                System.out.print(matrix[i][j] + "\t");
            }
            System.out.println();
        }

        int sum = sumUnderDiag(matrix);
        int count = countUnderDiag(matrix);

        System.out.println("Сумма элементов под главной диагональю: " + sum);
        System.out.println("Количество элементов под главной диагональю: " + count);
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

