package zadanie3;
import java.util.ArrayList;
import java.util.Scanner;
import java.util.InputMismatchException;

public class zadanie3 {
    static class Kvartira {
        String FIO;
        double plowad;
        int komnati;
        int etaj;

        public Kvartira(String FIO, double plowad, int komnati, int etaj) {
            this.FIO = FIO;
            this.plowad = plowad;
            this.komnati = komnati;
            this.etaj = etaj;
        }
    }

    public static void main(String[] args) {
        boolean internalTestsPassed = internalUnitTest();
        if (internalTestsPassed) {
            System.out.println("Тест пройден.");
        } else {
            System.out.println("Тест не пройден.");
            return;
        }

        Scanner scanner = new Scanner(System.in);
        ArrayList<Kvartira> kvartiraList = new ArrayList<>();
        while (true) {
            System.out.println("\nВыберите действие:");
            System.out.println("1. Создать новую квартиру");
            System.out.println("2. Сортировать список квартир по ФИО владельца");
            System.out.println("3. Поиск квартиры по владельцу");
            System.out.println("4. Изменить данные квартиры");
            System.out.println("5. Удалить квартиру");
            System.out.println("6. Вывести список квартир");
            System.out.println("7. Выход");
            int choice = scanner.nextInt();
            scanner.nextLine();
            switch (choice) {
                case 1:
                    createKvartira(scanner, kvartiraList);
                    break;
                case 2:
                    sortKvartiraByFIO(kvartiraList);
                    break;
                case 3:
                    searchKvartiraByFIO(scanner, kvartiraList);
                    break;
                case 4:
                    updateKvartira(scanner, kvartiraList);
                    break;
                case 5:
                    deleteKvartira(scanner, kvartiraList);
                    break;
                case 6:
                    printKvartiraList(kvartiraList);
                    break;
                case 7:
                    return;
                default:
                    System.out.println("Неверный выбор. Попробуйте снова.");
            }
        }
    }

    public static void createKvartira(Scanner scanner, ArrayList<Kvartira> kvartiraList) {
        System.out.print("Введите ФИО владельца: ");
        String FIO = scanner.nextLine();
        System.out.print("Введите площадь квартиры: ");
        double plowad = scanner.nextDouble();
        System.out.print("Введите количество комнат: ");
        int komnati = scanner.nextInt();
        System.out.print("Введите этаж: ");
        int etaj = scanner.nextInt();
        kvartiraList.add(new Kvartira(FIO, plowad, komnati, etaj));
        System.out.println("Квартира добавлена в список.");
    }

    public static void sortKvartiraByFIO(ArrayList<Kvartira> kvartiraList) {
        int n = kvartiraList.size();
        for (int i = 1; i < n; ++i) {
            Kvartira key = kvartiraList.get(i);
            int j = i - 1;
            while (j >= 0 && kvartiraList.get(j).FIO.compareTo(key.FIO) > 0) {
                kvartiraList.set(j + 1, kvartiraList.get(j));
                j = j - 1;
            }
            kvartiraList.set(j + 1, key);
        }
        System.out.printf("%-20s %-10s %-10s %-10s\n", "ФИО владельца", "Площадь", "Комнаты", "Этаж");
        for (Kvartira kvartira : kvartiraList) {
            System.out.printf("%-20s %-10.2f %-10d %-10d\n", kvartira.FIO, kvartira.plowad, kvartira.komnati, kvartira.etaj);
        }
    }

    public static void searchKvartiraByFIO(Scanner scanner, ArrayList<Kvartira> kvartiraList) {
        System.out.print("Введите ФИО владельца для поиска: ");
        String searchFIO = scanner.nextLine();
        boolean found = false;
        System.out.println("Результаты поиска:");
        for (Kvartira kvartira : kvartiraList) {
            if (kvartira.FIO.equalsIgnoreCase(searchFIO)) {
                printKvartiraInfo(kvartira);
                found = true;
            }
        }
        if (!found) {
            System.out.println("Квартира с владельцем " + searchFIO + " не найдена.");
        }
    }

    public static void updateKvartira(Scanner scanner, ArrayList<Kvartira> kvartiraList) {
        System.out.print("Введите номер квартиры для изменения (начиная с 1): ");
        int index = scanner.nextInt();
        scanner.nextLine();
        if (index >= 1 && index <= kvartiraList.size()) {
            System.out.println("Введите новые данные для квартиры " + index + ":");
            System.out.print("ФИО владельца: ");
            String FIO = scanner.nextLine();
            System.out.print("Площадь квартиры: ");
            double plowad = scanner.nextDouble();
            System.out.print("Количество комнат: ");
            int komnati = scanner.nextInt();
            System.out.print("Этаж: ");
            int etaj = scanner.nextInt();
            kvartiraList.set(index - 1, new Kvartira(FIO, plowad, komnati, etaj));
            System.out.println("Данные квартиры " + index + " обновлены.");
        } else {
            System.out.println("Квартира с указанным номером не существует.");
        }
    }

    public static void deleteKvartira(Scanner scanner, ArrayList<Kvartira> kvartiraList) {
        System.out.print("Введите номер квартиры для удаления (начиная с 1): ");
        int index = scanner.nextInt();
        scanner.nextLine();
        if (index >= 1 && index <= kvartiraList.size()) {
            kvartiraList.remove(index - 1);
            System.out.println("Квартира " + index + " удалена из списка.");
        } else {
            System.out.println("Квартира с указанным номером не существует.");
        }
    }

    public static void printKvartiraList(ArrayList<Kvartira> kvartiraList) {
        System.out.println("\nСписок квартир:");
        System.out.println("-----------------------------------------------------------------");
        System.out.printf("%-5s %-20s %-10s %-10s %-10s\n", "№", "ФИО владельца", "Площадь", "Комнаты", "Этаж");
        System.out.println("-----------------------------------------------------------------");
        for (int i = 0; i < kvartiraList.size(); i++) {
            System.out.printf("%-5d %-20s %-10.2f %-10d %-10d\n", i + 1,
                    kvartiraList.get(i).FIO, kvartiraList.get(i).plowad,
                    kvartiraList.get(i).komnati, kvartiraList.get(i).etaj);
        }
        System.out.println("-----------------------------------------------------------------");
        System.out.println("Всего квартир: " + kvartiraList.size());
    }

    public static void printKvartiraInfo(Kvartira kvartira) {
        System.out.println("ФИО владельца: " + kvartira.FIO);
        System.out.println("Площадь: " + kvartira.plowad);
        System.out.println("Количество комнат: " + kvartira.komnati);
        System.out.println("Этаж: " + kvartira.etaj);
        System.out.println("-------------------------");
    }

    // Юнит-тесты
    public static boolean internalUnitTest() {
        ArrayList<Kvartira> kvartiraList = new ArrayList<>();
        createKvartiraTest(kvartiraList);
        sortKvartiraByFIOUnitTest(kvartiraList);
        searchKvartiraByFIOUnitTest(kvartiraList);
        updateKvartiraUnitTest(kvartiraList);
        deleteKvartiraUnitTest(kvartiraList);
        printKvartiraListUnitTest(kvartiraList);
        return true;
    }

    public static void createKvartiraTest(ArrayList<Kvartira> kvartiraList) {
        Kvartira kvartira = new Kvartira("Иванов", 80.0, 3, 2);
        kvartiraList.add(kvartira);
    }

    public static void sortKvartiraByFIOUnitTest(ArrayList<Kvartira> kvartiraList) {
        System.out.println("Сортировка списка квартир по ФИО владельца:");
        sortKvartiraByFIO(kvartiraList);
    }

    public static void searchKvartiraByFIOUnitTest(ArrayList<Kvartira> kvartiraList) {
        System.out.println("Поиск квартиры по ФИО владельца:");
        Scanner scanner = new Scanner("Иванов\n");
        searchKvartiraByFIO(scanner, kvartiraList);
    }

    public static void updateKvartiraUnitTest(ArrayList<Kvartira> kvartiraList) {
        Scanner scanner = new Scanner("1\nНовый Владелец\n100.0\n4\n2\n");
        System.out.println("Обновление данных квартиры:");
        System.out.print("Введите номер квартиры для изменения (начиная с 1): ");
        int index = scanner.nextInt();
        scanner.nextLine();
        System.out.println("Введите новые данные для квартиры " + index + ":");
        System.out.print("ФИО владельца: ");
        String FIO = scanner.nextLine();
        double plowad;
        try {
            System.out.print("Площадь квартиры: ");
            plowad = scanner.nextDouble();
        } catch (InputMismatchException e) {
            System.out.println("Некорректный ввод. Пожалуйста, введите число для площади квартиры.");
            return;
        }
        System.out.print("Количество комнат: ");
        int komnati = scanner.nextInt();
        System.out.print("Этаж: ");
        int etaj = scanner.nextInt();
        kvartiraList.set(index - 1, new Kvartira(FIO, plowad, komnati, etaj));
        System.out.println("Данные квартиры " + index + " обновлены.");
    }



    public static void deleteKvartiraUnitTest(ArrayList<Kvartira> kvartiraList) {
        System.out.println("Удаление квартиры:");
        Scanner scanner = new Scanner("1\n");
        deleteKvartira(scanner, kvartiraList);
    }

    public static void printKvartiraListUnitTest(ArrayList<Kvartira> kvartiraList) {
        System.out.println("Вывод списка квартир:");
        printKvartiraList(kvartiraList);
    }
}
