public class StockFlowUpdate {
    public static void main(String[] args) {
        double currentStock = 100.0;
        double inflow = 12.0;
        double outflow = 7.0;
        double nextStock = currentStock + inflow - outflow;
        System.out.printf("next_stock=%.4f%n", nextStock);
    }
}
