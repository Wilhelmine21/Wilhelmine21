#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <time.h>

#define MAX_LINE_LENGTH 256

int main(int argc, char *argv[]) {
    if (argc != 3) {
        printf("Usage: %s finst freport\n", argv[0]);
        return 1;
    }

    char *finst = argv[1];
    char *freport = argv[2];

    clock_t t1 = clock();
    FILE *f1 = fopen(finst, "r");
    FILE *f2 = fopen(freport, "r");
    FILE *out = fopen("output.log", "w");

    if (!f1 || !f2 || !out) {
        printf("Error opening files\n");
        return 1;
    }

    bool inst[MAX_LINE_LENGTH];
    memset(inst, false, sizeof(inst));

    char line[MAX_LINE_LENGTH];
    int count = 0;
    while (fgets(line, MAX_LINE_LENGTH, f1)) {
        int len = strlen(line);
        if (line[len - 1] == '\n') {
            line[len - 1] = '\0';
        }
        inst[count++] = true;
    }

    count = 0;
    while (fgets(line, MAX_LINE_LENGTH, f2)) {
        int len = strlen(line);
        if (line[len - 1] == '\n') {
            line[len - 1] = '\0';
        }
        for (int i = 0; i < count; i++) {
            if (inst[i] && strstr(line, line + i * MAX_LINE_LENGTH)) {
                fprintf(out, "%s\n", line + i * MAX_LINE_LENGTH);
                inst[i] = false;
                break;
            }
        }
    }

    fclose(f1);
    fclose(f2);
    fclose(out);

    clock_t ta = clock() - t1;
    double elapsed_time = (double) ta / CLOCKS_PER_SEC;
    int minutes = (int) elapsed_time / 60;
    double seconds = elapsed_time - minutes * 60;
    printf("It cost %d min %.2f sec.\n", minutes, seconds);

    return 0;
}
