import java.security.MessageDigest;
import java.nio.charset.StandardCharsets;

public class HashVerificationDemo {
    static String sha256Prefix(String input) throws Exception {
        MessageDigest digest = MessageDigest.getInstance("SHA-256");
        byte[] bytes = digest.digest(input.getBytes(StandardCharsets.UTF_8));
        StringBuilder sb = new StringBuilder();
        for (byte b : bytes) sb.append(String.format("%02x", b));
        return sb.substring(0, 16);
    }

    public static void main(String[] args) throws Exception {
        String original = "verified artifact manifest";
        String altered = "verified artifact manifest!";
        System.out.println("original sha256=" + sha256Prefix(original));
        System.out.println("altered sha256=" + sha256Prefix(altered));
        System.out.println("match=" + sha256Prefix(original).equals(sha256Prefix(altered)));
    }
}
