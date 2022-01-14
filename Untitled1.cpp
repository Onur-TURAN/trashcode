#include <stdio.h>
#include <stdlib.h>
int F(int sayi)
{
	int max=0,n;
	while(sayi>0)
	{
		n=sayi%10;
		if(n>max) max=n;
		sayi/=10;
	}
	return max;
}
int main ()
{
	int sayi=4893,max;
	max=F(sayi);
	printf("max: %d",max);
	return 0;
}
