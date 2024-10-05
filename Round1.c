#include<stdio.h>
#include<conio.h>
void main() {
  int num,arr[100],i,j,count=0,val=0,h_count=0;
  clrscr();
  printf("Enter the number of elements in a array:");
  scanf("%d",&num);
  printf("Enter %d Values:",num);
  for(i=0;i<num;i++){
    scanf("%d",&arr[i]);
  }
  for(i=0;i<num;i++){
    count=0;
    for(j=0;j<num;j++){
      if(arr[i]==arr[j]){
        count++;
      }
    }
    if(count>h_count){
    h_count=count;
    val=arr[i];
    }
  }
  printf("The Repeated value is %d",val);
}
