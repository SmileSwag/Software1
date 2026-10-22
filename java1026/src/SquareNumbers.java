import java.util.ArrayList;

public class SquareNumbers {
    public static void main(String[] args) {
        ArrayList<Integer> squares = new ArrayList<>();

        for (int number = 1; number <= 20; number++) {
            squares.add(number * number);
        }
        // Remove all odd numbers from the list
        for (int index = 0; index < squares.size(); index++) {
            int element = squares.get(index);
            if (element % 2 != 0) {
                squares.remove(index);
            }

            for (int square : squares) {
                System.out.println(square);
            }
        }
    }
}