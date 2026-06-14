package net.thecontentcatalyst.acr;

public class Main {
    static long factorial(int n) {
        return n == 0 ? 1 : n * factorial(n - 1);
    }

    public static void main(String[] args) {
        for (int i = 0; i <= 6; i++) {
            System.out.println(i + " " + factorial(i));
        }
    }
}
