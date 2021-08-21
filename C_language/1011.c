#include<stdio.h>
#include<math.h>
int main()
{
	int N, i, x, y, d, sq;
	scanf("%d", &N);
	for (i = 0; i < N; i++) {
		scanf("%d %d", &x, &y);
		d = y - x;
		if (d < 4) printf("%d\n", d);
		else {
			sq = (int)sqrt(d);
			if (pow(sq, 2) == d) printf("%d\n", sq * 2 - 1);
			else {
				sq++;
				if (pow(sq, 2) - sq >= d) printf("%d\n", sq * 2 - 2);
				else printf("%d\n", sq * 2 - 1);
			}
		}
	}
}