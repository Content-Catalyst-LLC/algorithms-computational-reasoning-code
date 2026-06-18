package org.contentcatalyst.algorithms;
import java.util.Arrays;
public class DivideConquerAudit {
  public static void main(String[] args){
    int[] xs = {9,3,5,1}; Arrays.sort(xs);
    System.out.println("test_name,value");
    System.out.println("merge_sort," + Arrays.toString(xs));
    System.out.println("binary_search_5," + Arrays.binarySearch(xs, 5));
  }
}
