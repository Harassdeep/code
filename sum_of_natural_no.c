#include <stdio.h>

int main() {

    int n;
    int i=1;
    int l=1;
    printf("Enter the limit of your sum: ");
    scanf("%d", &n);

    do {
        printf("The sum of first %d numbers is %d\n", i,l);
        i = i+1;
        l = l+i;

    }while(i<n+1);

    return 0;
}
