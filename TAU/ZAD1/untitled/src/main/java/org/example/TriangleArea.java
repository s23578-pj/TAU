package org.example;

public class TriangleArea {
    public static boolean canBuildTriangle(double a, double b, double c) {
        return a + b > c && a + c > b && b + c > a;
    }

    public static double calculateTriangleArea(double a, double b, double c) {
        double p = (a + b + c) / 2;
        return Math.sqrt(p * (p - a) * (p - b) * (p - c));
    }
}
