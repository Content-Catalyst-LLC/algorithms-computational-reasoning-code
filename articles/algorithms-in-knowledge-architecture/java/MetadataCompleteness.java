public class MetadataCompleteness {
    public static void main(String[] args) {
        double presentFields = 11.0;
        double requiredFields = 12.0;
        double score = presentFields / requiredFields;
        System.out.printf("metadata_completeness_score=%.4f%n", score);
    }
}
