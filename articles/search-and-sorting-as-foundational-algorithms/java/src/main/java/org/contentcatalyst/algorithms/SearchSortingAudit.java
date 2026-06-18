package org.contentcatalyst.algorithms;
import java.util.Arrays;
public class SearchSortingAudit {
  static int linearSearch(int[] xs, int target){ for(int i=0;i<xs.length;i++){ if(xs[i]==target) return i; } return -1; }
  public static void main(String[] args){
    int[] xs = {7,2,9,1}; Arrays.sort(xs);
    System.out.println("test_name,value");
    System.out.println("linear_search_9," + linearSearch(new int[]{7,2,9,1},9));
    System.out.println("sort_demo," + Arrays.toString(xs));
  }
}
