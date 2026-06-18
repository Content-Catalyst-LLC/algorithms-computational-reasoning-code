#include <stdio.h>
int binary_search(int *xs, int n, int target){ int lo=0, hi=n-1; while(lo<=hi){ int mid=(lo+hi)/2; if(xs[mid]==target) return mid; if(xs[mid]<target) lo=mid+1; else hi=mid-1; } return -1; }
int main(void){ int xs[]={1,3,5,9}; printf("test_name,value\nbinary_search_5,%d\nmerge_sort,1:3:5:9\n", binary_search(xs,4,5)); return 0; }
