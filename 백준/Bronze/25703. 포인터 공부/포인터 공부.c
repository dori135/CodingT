#include <stdio.h>

int main(void) {
   int num;

   scanf("%d", &num);
   printf("int a;\nint *ptr = &a;\n");

   for (int i = 1; i < num; i++){
      if (i==1)
        printf("int **ptr%d = &ptr;\n", i+1);

      else{
        printf("int ");
        for (int j = 0; j < i; j++)
          printf("*");
        printf("*ptr%d = &ptr%d;\n", i+1, i);
        }
   }
}