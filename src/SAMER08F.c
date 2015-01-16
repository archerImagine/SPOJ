/*
* SPOJ: http://www.spoj.com/problems/SAMER08F/
* http://www.quora.com/How-do-you-calculate-the-number-of-squares-in-an-n-x-n-square-grid
*/

#include<stdio.h>
int feynman(n){
	if (n == 1)
	{
		return 1;
	}else{
		return (n * (n+1)*(2*n +1))/6;
	}
}

int main(int argc, char const *argv[])
{
	int t = 0;
	scanf("%d",&t);
	while(t){
		printf("%d\n",feynman(t));
		scanf("%d",&t);
	}
	return 0;
}