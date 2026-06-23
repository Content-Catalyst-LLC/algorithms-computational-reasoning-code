public class WorkloadBurden {
    public static void main(String[] args) {
        double pace = 0.84;
        double hours = 0.72;
        double fatigue = 0.70;
        double scheduleVolatility = 0.78;
        double burden = (pace + hours + fatigue + scheduleVolatility) / 4.0;
        System.out.printf("workload_burden_score=%.4f%n", burden);
    }
}
