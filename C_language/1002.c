#include<stdio.h>
#include<math.h>
int main()
{
    int i, N, diff, x1, y1, x2, y2, r1, r2;
    scanf("%d", &N);
    for (i = 0; i < N; i++) {
        scanf("%d %d %d %d %d %d", &x1, &y1, &r1, &x2, &y2, &r2);
        diff = (x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1);
        if (diff == 0 && r1 == r2) {
            printf("-1\n");
        }
        else if (diff > (r1 + r2) * (r1 + r2)) {
            printf("0\n");
        }
        else if (diff == (r1 + r2) * (r1 + r2)) {
            printf("1\n");
        }
        else if (diff < (r1 + r2) * (r1 + r2)) {
            if (diff == (r2 - r1) * (r2 - r1) || diff == (r1 - r2) * (r1 - r2)) {
                printf("1\n");
            }
            else if (diff < (r2 - r1) * (r2 - r1) || diff < (r1 - r2) * (r1 - r2)) {
                printf("0\n");
            }
            else {
                printf("2\n");
            }
        }
    }
}