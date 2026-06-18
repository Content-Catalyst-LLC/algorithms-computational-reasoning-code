package org.contentcatalyst.algorithms;
public class EvolutionarySearchAudit {
  static int fitness(int[] xs){ int s=0; for(int x:xs){ s += x; } return s; }
  public static void main(String[] args){
    System.out.println("test_name,value");
    System.out.println("binary_fitness," + fitness(new int[]{1,0,1,1}));
    System.out.println("mutation_rate,0.03");
  }
}
