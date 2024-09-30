#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>

#include "libs/matfun.h"
#include "libs/geofun.h"

int main() {
	double **k,**M,**C;
	int m=1,c=2;
	
	k = createMat(2,1);
	k[0][0]=m;
	k[1][0]=c;
	FILE *file;
	file = fopen("values.dat", "w");

	if (file == NULL) {
		printf("Error opening file!\n");
		return 1;
	}
	fprintf(file, "m\tc\t of L\n");
	fprintf(file, "%.02lf\t", k[0][0]);
	fprintf(file, "%.02lf", k[1][0]);

	fclose(file);
	printf("Results have been written to values.dat\n");

	freeMat(k,2);
	return 0;
}
