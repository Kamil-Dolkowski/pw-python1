#include <iostream>
#include <map>
#include <list>
#include <cmath>
#include <algorithm>

class BuddyAllocator {
public:
    BuddyAllocator(size_t _memory_size, size_t _division_limit) {
        if (_memory_size % 2 != 0) throw std::logic_error("Memory size must be the power of 2.");

        memory_size = _memory_size;
        division_limit = _division_limit;

        std::list<size_t> zero_list;
        zero_list.push_back(0);

        free_blocks[memory_size] = zero_list;
    }
    ~BuddyAllocator() {}

    std::pair<size_t, size_t> alloc(size_t size) {
        size_t allocation_address; 

        size_t block_size = pow(2, (ceil(log2(size))));

        // jeśli block_size jest mniejszy niż limit
        if (block_size < memory_size / pow(2, division_limit)) block_size = pow(2, division_limit);

        // std::cout << "\nBlock size: " << block_size << std::endl;

        if (free_blocks.find(block_size) != free_blocks.end()) {
            // std::cout << "Znaleziono blok" << std::endl;

            if (free_blocks[block_size].empty()) {
                // znaleziono blok, ale brak adresów
                // std::cout << "Brak adresow" << std::endl;

                // sprawdź bloki wyżej
                std::pair<size_t, size_t> res = alloc(2*block_size);

                // std::cout << "--address: " << res.first << "\n--block size: " << res.second << std::endl;

                // podział
                free_blocks[res.second/2].push_back(res.first);
                free_blocks[res.second/2].push_back(res.first + res.second/2);
                
                return alloc(block_size);

            } else {
                // znaleziono blok z adresami
                // std::cout << "Usuniecie adresu z free_blocks" << std::endl;

                allocation_address = free_blocks[block_size].front();
                free_blocks[block_size].pop_front();

                return {allocation_address, block_size};
            }

        } else {
            // std::cout << "Brak takiego bloku" << std::endl;

            // jeśli chce wyjść poza zakres
            if (2*block_size > memory_size) throw std::out_of_range("Can't alloc (not enough memory space).");

            std::pair<size_t, size_t> res = alloc(2*block_size);

            // std::cout << "--address: " << res.first << "\n--block size: " << res.second << std::endl;

            // podział
            free_blocks[res.second/2].push_back(res.first);
            free_blocks[res.second/2].push_back(res.first + res.second/2);
            
            return alloc(block_size);
        }

    }

    void free(size_t address, size_t block_size) {
        // === Warunki, wychwytywanie błędnych argumentów ===

        int interval = pow(2, (division_limit));

        // walidacja address
        if (address % interval != 0 || address > memory_size) {
             throw std::invalid_argument("In method free() argument 'address' must be the existing address.");
        }

        // walidacja block_size
        if (block_size != pow(2, (ceil(log2(block_size)))) || block_size > memory_size || block_size < memory_size/pow(2,division_limit)) {
             throw std::invalid_argument("In method free() argument 'block_size' must be the existing block size.");
        }

        bool is_block_size = false;
        for (const auto &element : free_blocks) {
            if (element.first == block_size) {
                is_block_size = true;
                break;
            }
        }

        if (!is_block_size) throw std::logic_error("Block with this memory size does not exists.");

        if (std::find(free_blocks[block_size].begin(), free_blocks[block_size].end(), address) != free_blocks[block_size].end()) {
            throw std::out_of_range("Can't free (this address was already free).");
        }

        // === Algorytm free ===

        // w przypadku zwolnienia całej pamięci
        if (block_size == memory_size) {
            for (int i=block_size; i >= memory_size/pow(2,division_limit); i-=pow(2,division_limit)) {
                free_blocks.erase(i);
            }
        }


        size_t friend_address;

        friend_address = address ^ block_size;
        // std::cout << "\nFriend address: " << friend_address << std::endl;

        if (std::find(free_blocks[block_size].begin(), free_blocks[block_size].end(), friend_address) != free_blocks[block_size].end()) {
            // std::cout << "znaleziono znajomego (" << block_size << ")" << std::endl;
            
            free_blocks[block_size].pop_front();

            if (free_blocks[block_size].empty()) {
                for (int i=block_size; i >= memory_size/pow(2,division_limit); i-=pow(2,division_limit)) {
                    free_blocks.erase(i);
                }

                free_blocks.erase(block_size);

                // std::cout << "pop " << block_size << std::endl;
                // printFreeBlocks();
            }

            free(address, block_size * 2);

        } else {
            free_blocks[block_size].push_front(address);
        }
    }

    void printFreeBlocks() {
        std::cout << "==FREE_BLOCKS==" << std::endl;
        for (const auto &element : free_blocks) {
            std::cout << element.first << ": [" ;

            size_t i=1;

            for (const auto &address : element.second) {
                std::cout << address ;
                if (i != element.second.size()) std::cout << ", " ;
                i++;
            }

            std::cout << "]" << std::endl;
        }
    }

private:
    size_t memory_size;
    size_t division_limit;
    std::map<size_t, std::list<size_t>> free_blocks;
};


void printAllocationResult(std::pair<size_t, size_t> p) {
    std::cout << "\n=====ALLOCATION RESULT=====" << std::endl;
    std::cout << "Allocation address: " << p.first << std::endl;
    std::cout << "Allocated memory size: " << p.second << std::endl;
}




int main() {
    try {
        BuddyAllocator ba(1024, 5);
        std::pair<size_t, size_t> p;

        ba.printFreeBlocks();



        // std::cout << "\n-----Allocation: 40" << std::endl;

        // p = ba.alloc(40);
        // printAllocationResult(p);

        // std::cout << std::endl;
        // ba.printFreeBlocks();




        // std::cout << "\n-----Allocation: 40" << std::endl;

        // p = ba.alloc(40);
        // printAllocationResult(p);

        // std::cout << std::endl;
        // ba.printFreeBlocks();



        std::cout << "\n-----Allocation: 40" << std::endl;

        p = ba.alloc(40);
        printAllocationResult(p);

        std::cout << std::endl;
        ba.printFreeBlocks();



        // std::cout << "\n-----Free (256, 128)" << std::endl;

        // ba.free(256, 128);

        // std::cout << std::endl;
        // ba.printFreeBlocks();



        std::cout << "\n-----Free (0, 64)" << std::endl;

        ba.free(0, 64);

        std::cout << std::endl;
        ba.printFreeBlocks();


        // std::cout << "\n-----Free (0, 64)" << std::endl;

        // ba.free(0, 64);

        // std::cout << std::endl;
        // ba.printFreeBlocks();


    } catch (const std::exception &e) {
        std::cout << "\nError: " << e.what() << std::endl;
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