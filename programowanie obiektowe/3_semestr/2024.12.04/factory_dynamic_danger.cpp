// !! Niebezpieczne -> zapełnia pamięć i jej nie usuwa

#include <exception>

int main() {
    while (true) {
        try {
            int *tab = new int[1000];
            throw std::exception();
        } catch (const std::exception &e) {
            /* nic */
        }
    }

    return 0;
}