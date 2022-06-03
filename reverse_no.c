#include <stdio.h>

int main() {

    int n,k;
    int l;
    printf("Enter your number: ");
    scanf("%d", &n);

    do{
        n=n%10;
        l=l*10+n;
    }while(n!=0);

    printf("%d", l);

//    int t = 5676555554;
//    printf("%d", t);

    return 0;
}
