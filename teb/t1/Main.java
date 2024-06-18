package org.example;

public class Main {
    public static void main(String[] args) {
        int[][] Matrix = {
                {3, 1, 4, 2},
                {5, 9, 7, 1},
                {2, 6, 8, 3},
                {1, 3, 5, 7}
        };

        int[][] expectedMatrix = {
                {4, 2, 3, 1},
                {9, 5, 7, 1},
                {8, 6, 2, 3},
                {7, 3, 5, 1}
        };

        for (int i = 0; i < Matrix.length; i++) {
            int max = i;
            int min = i;
            for (int j = i; j < Matrix[i].length; j++) {
                if (Matrix[i][j] > Matrix[i][max]) {
                    max = j;
                }
                if (Matrix[i][j] < Matrix[i][min]) {
                    min = j;
                }
            }
            int temp = Matrix[i][0];
            Matrix[i][0] = Matrix[i][max];
            Matrix[i][max] = temp;

            temp = Matrix[i][Matrix[i].length - 1];
            Matrix[i][Matrix[i].length - 1] = Matrix[i][min];
            Matrix[i][min] = temp;
        }
        for (int i = 0; i < Matrix.length; i++) {
            for (int j = 0; j < Matrix[i].length; j++) {
                System.out.print(Matrix[i][j] + " ");
            }
            System.out.println();
        }
        boolean Flag = true;
        for (int i = 0; i < Matrix.length; i++) {
            for (int j = 0; j < Matrix[i].length; j++) {
                if (Matrix[i][j]!= expectedMatrix[i][j]) {
                    Flag = false;
                    break;
                }
            }
            if (!Flag) {
                break;
            }
        }

        if (Flag) {
            System.out.println("Тест пройден");
        } else {
            System.out.println("Тест не пройден");
        }
    }
}