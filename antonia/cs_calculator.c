//cs calculator
#include <stdio.h>


int main (void){
    int loop = 1;
    char command = 0;
    int number = 0;
    int calculatingnumber = 0;
    int output = 1;
    int counter = 0;

while (loop ==1) {
printf("Enter instruction: ");
        scanf(" %c", &command);
        scanf("%d", &number);
            if (command == 's') {   
                output = number * number;
                printf("%d\n", output);
            }
            else if (command == 'p') {
                scanf("%d", &calculatingnumber);
                counter = 0;
                for (counter = 0; counter < calculatingnumber; counter++) {
                output = output * number;
                }
                printf("%d\n", output);
            }
            else {
                return 1;
            }
}
        
    return 0;
}
