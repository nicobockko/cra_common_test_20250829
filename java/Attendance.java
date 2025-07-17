import java.io.*;
import java.util.*;

public class Attendance {

    static class Node {
        String w;
        String wk;
    }

    static Map<String, Integer> id1 = new HashMap<>();
    static int idCnt = 0;

    static int[][] dat = new int[100][100];
    static int[] points = new int[100];
    static int[] grade = new int[100];
    static String[] names = new String[100];

    static int[] wed = new int[100];
    static int[] weeken = new int[100];

    public static void input2(String w, String wk) {
        if (!id1.containsKey(w)) {
            id1.put(w, ++idCnt);
            names[idCnt] = w;
        }
        int id2 = id1.get(w);

        int addPoint = 0;
        int index = 0;

        switch (wk) {
            case "monday":
                index = 0;
                addPoint++;
                break;
            case "tuesday":
                index = 1;
                addPoint++;
                break;
            case "wednesday":
                index = 2;
                addPoint += 3;
                wed[id2]++;
                break;
            case "thursday":
                index = 3;
                addPoint++;
                break;
            case "friday":
                index = 4;
                addPoint++;
                break;
            case "saturday":
                index = 5;
                addPoint += 2;
                weeken[id2]++;
                break;
            case "sunday":
                index = 6;
                addPoint += 2;
                weeken[id2]++;
                break;
        }

        dat[id2][index]++;
        points[id2] += addPoint;
    }

    public static void input() {
        try (BufferedReader br = new BufferedReader(new FileReader("src/main/resources/attendance_weekday_500.txt"))) {
            for (int i = 0; i < 500; i++) {
                String line = br.readLine();
                if (line == null) break;
                String[] parts = line.split("\\s+");
                if (parts.length == 2) {
                    input2(parts[0], parts[1]);
                }
            }

            for (int i = 1; i <= idCnt; i++) {
                if (dat[i][3] > 9) {
                    points[i] += 10;
                }

                if (dat[i][5] + dat[i][6] > 9) {
                    points[i] += 10;
                }

                if (points[i] >= 50) {
                    grade[i] = 1;
                } else if (points[i] >= 30) {
                    grade[i] = 2;
                } else {
                    grade[i] = 0;
                }

                System.out.print("NAME : " + names[i] + ", ");
                System.out.print("POINT : " + points[i] + ", ");
                System.out.print("GRADE : ");

                if (grade[i] == 1) {
                    System.out.println("GOLD");
                } else if (grade[i] == 2) {
                    System.out.println("SILVER");
                } else {
                    System.out.println("NORMAL");
                }
            }

            System.out.println();
            System.out.println("Removed player");
            System.out.println("==============");
            for (int i = 1; i <= idCnt; i++) {
                if (grade[i] != 1 && grade[i] != 2 && wed[i] == 0 && weeken[i] == 0) {
                    System.out.println(names[i]);
                }
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        input();
    }
}
