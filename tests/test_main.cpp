#include <cassert>
#include "../src/lib.h"

int main() {
    assert(add(2, 2) == 4 && "add(2,2) should equal 4");
    assert(add(-1, 1) == 0 && "add(-1,1) should equal 0");
    assert(square(2) == 4 && "square(2) should equal 4");
    assert(square(-3) == 9 && "square(2) should equal 9");
    return 0;
}
