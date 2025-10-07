#include <iostream>
#include <string_view>
#include "../src/lib.h"

// Testing Template
template <typename T, typename U>
bool check_eq(std::string_view label, const T& got, const U& expected, int& fails) {
    if (got == expected) {
        std::cout << "✅ " << label << "  got=" << got << "  expected=" << expected << "\n";
        return true;
    } else {
        std::cerr << "❌ " << label << "  got=" << got << "  expected=" << expected << "\n";
        ++fails;
        return false;
    }
}

int main() {
    int fails = 0;
    std::cout << "Running SimpleCalculator tests...\n";

    check_eq("add(2, 2)",   add(2, 2),   4, fails);
    check_eq("add(-1, 1)",  add(-1, 1),  0, fails);
    check_eq("square(2)",   square(2),   4, fails);
    check_eq("square(-3)",  square(-3),  9, fails);
    check_eq("Subtract(1, 1)", subtract(1, 1),   0, fails);
    check_eq("Subtract(-1, 1)", subtract(-1, 1),   -2, fails);

    if (fails == 0) {
        std::cout << "✅  All tests passed\n";
        return 0;
    } else {
        std::cerr << "❌ " << fails << " test(s) failed\n";
        return 1;
    }
}
