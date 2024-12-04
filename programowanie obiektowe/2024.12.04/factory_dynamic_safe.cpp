// Bezpieczne -> zapełnia pamięć i ją usuwa
// Kod niepełny

#include <exception>
#include <memory>

int main() {
    while (true) {
        try {
            std::unique_ptr ...
            throw std::exception();
        } catch (const std::exception &e) {
            /* nic */
        }
    }

    return 0;
}