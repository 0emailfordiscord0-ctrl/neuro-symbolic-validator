#include <stdio.h>

int calculate_buffer(int x) {
    // Vulnerable addition that can wrap around 32-bit signed limits
    int total = x + 100;
    if (total > 2000) {
        return 2000;
    }
    return total;
}