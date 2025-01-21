#include <iostream>
#include <map>
#include <list>

class BuddyAllocator {
public:
    BuddyAllocator(size_t _memory_size, size_t _division_limit) {
        if (_memory_size % 2 != 0) throw std::logic_error("Memory size must be the power of 2.");

        memory_size = _memory_size;
        division_limit = _division_limit;

        std::list<int> zero_list;
        zero_list.push_back(0);

        free_blocks[memory_size] = zero_list;
        
    }
    ~BuddyAllocator() {}

    // std::pair<size_t, size_t> alloc(size_t size) {}
    void free(size_t address, size_t size) {}

private:
    size_t memory_size;
    size_t division_limit;
    std::map<int, std::list<int>> free_blocks;
};




int main() {
    try {
        BuddyAllocator ba(1024, 5);
    } catch (const std::exception &e) {
        std::cout << e.what() << std::endl;
    }
    
    return 0;
}




// ==============================================

// free_blocks = { ... }
// free_blocks[1024] = [ ... ]

// ---------------------

// size = 1024
// free_blocks = {
//     1024 : [ 0 ]

// };

// ---------------------

// alokacja 500B -> addr : 512

// free_blocks = {
//     1024 : [],
//     512 : [0]
// }

// ---------------------

// alokacja 100B -> addr : 0

// free_blocks = {
//     1024 : [],
//     512 : [],
//     256 : [256],
//     128 : [128]
// }

// free_blocks {
//     1024 : []
//     512 : [512]
// }