#include <stdio.h>

int main() {
    // Define parabola parameters
    double p1 = 1.0; // Parameter for y^2 = 4px
    double p2 = 1.0; // Parameter for x^2 = 4py

    // Open the file to write the parameters
    FILE *file = fopen("data.txt", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Write the parabola parameters to the file
    fprintf(file, "%f\n", p1); // Parameter for the first parabola
    fprintf(file, "%f\n", p2); // Parameter for the second parabola

    // Close the file
    fclose(file);

    printf("Data written to data.txt\n");

    return 0;
}
 