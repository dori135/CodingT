#include <stdio.h>

int main() {

	int n, m;

	int card[100] = { 0, };

	scanf("%d %d", &n, &m);

	for (int i = 0; i < n; i++)
		scanf("%d", &card[i]);

	int sum = -1;

	for (int i = 0; i < n - 2; i++) {
		for (int j = i + 1; j < n - 1; j++) {
			for (int k = j+1; k < n; k++) {
				if ((sum < card[i] + card[j] + card[k]) && (card[i] + card[j] + card[k] <= m))
					sum = card[i] + card[j] + card[k];
			}
		}
	}
	printf("%d", sum);

}