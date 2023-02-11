#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <time.h>

#define MAX_LINE_LENGTH 256

int main() {
    clock_t t1 = clock();

    FILE *f1 = fopen("inst.txt", "r");
    FILE *f2 = fopen("report.txt", "r");
    FILE *out = fopen("output.log", "w");

    char inst[MAX_LINE_LENGTH][MAX_LINE_LENGTH];
    int inst_count = 0;
    char line[MAX_LINE_LENGTH];
    bool found;

    while (fgets(line, MAX_LINE_LENGTH, f1)) {
        line[strcspn(line, "\n")] = 0;
        strcpy(inst[inst_count++], line);
    }

    while (fgets(line, MAX_LINE_LENGTH, f2)) {
        line[strcspn(line, "\n")] = 0;
        found = false;
        for (int i = 0; i < inst_count; i++) {
            if (strstr(line, inst[i])) {
                fprintf(out, "%s\n", inst[i]);
                found = true;
                break;
            }
        }
        if (found) {
            for (int i = 0; i < inst_count; i++) {
                if (strcmp(line, inst[i]) == 0) {
                    for (int j = i; j < inst_count - 1; j++) {
                        strcpy(inst[j], inst[j + 1]);
                    }
                    inst_count--;
                    break;
                }
            }
        }
    }

    fclose(f1);
    fclose(f2);
    fclose(out);

    double ta = (double)(clock() - t1) / CLOCKS_PER_SEC;
    int minutes = (int)ta / 60;
    double seconds = ta - minutes * 60;
    printf("It took %d min %.2f sec.\n", minutes, seconds);

    return 0;
}
