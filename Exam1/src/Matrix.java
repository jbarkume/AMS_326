public class Matrix {

    private int rows = 2;
    private int columns = 2;
    private int[][] data;

    public Matrix() {
        this.data = new int[rows][columns];
    }

    public Matrix(int rows, int columns) {
        this.rows = rows;
        this.columns = columns;
        this.data = new int[rows][columns];
    }

    public int getRows() {
        return this.rows;
    }

    public int getColumns() {
        return this.columns;
    }

    public int[][] getData() {
        return this.data;
    }

    public void printData() {
        for (int[] datum : data) {
            for (int i : datum) {
                System.out.print(i + " ");
            }
            System.out.println();
        }
    }

    public int insertValue(int i, int j, int value) {
        try {
            this.data[i][j] = value;
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Index Out Of Bounds!");
            return -1;
        }
        return 1;
    }

    public int getValue(int i, int j) {
        return this.data[i][j];
    }

    public static void main(String[] args) {
        Matrix intMatrix = new Matrix(3, 3);
        intMatrix.printData();
    }
}
