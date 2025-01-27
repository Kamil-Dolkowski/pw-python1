#include <iostream>
#include <map>
#include <list>
#include <cmath>
#include <algorithm>

class BuddyAllocator {
public:
    BuddyAllocator(size_t _memory_size, size_t _division_limit) {
        if ((_memory_size == 0) || (_memory_size & (_memory_size - 1))) {
            throw std::logic_error("Memory size must be the power of 2.");
        }
        
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
        if (block_size < memory_size / pow(2, division_limit)) block_size = memory_size/pow(2, division_limit);

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

        // walidacja address
        int interval = memory_size/pow(2, division_limit);
        if (address % interval != 0 || address >= memory_size) {
             throw std::invalid_argument("In method free() argument 'address' must be the existing address.");
        }

        // walidacja block_size
        if (block_size != pow(2, (ceil(log2(block_size)))) || block_size > memory_size || block_size < memory_size/pow(2,division_limit)) {
             throw std::invalid_argument("In method free() argument 'block_size' must be the existing block size.");
        }

        // sprawdzenie, czy dany blok istnieje w free_blocks 
        if (free_blocks.find(block_size) == free_blocks.end()) {
            throw std::logic_error("Block with this memory size does not exists.");
        }

        // sprawdzenie, czy dany adres jest już wolny (czy dany adres znajduje się w danym bloku w free_blocks)
        if (std::find(free_blocks[block_size].begin(), free_blocks[block_size].end(), address) != free_blocks[block_size].end()) {
            throw std::out_of_range("Can't free (this address is already free).");
        }

        // sprawdzenie, czy większy blok ma zwolnioną pamięć o danym adresie
        for (const auto &element : free_blocks) {
            if (element.first > block_size) {
                for (const auto &_address : element.second) {
                    // blok wolny (przedział): [_address, _address + element.first)
                    if (address >= _address  && address < _address + element.first) {
                        throw std::out_of_range("Can't free (this address is already free).");
                    }
                }
            } else {
                continue;
            }
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
            
            auto it = std::find(free_blocks[block_size].begin(), free_blocks[block_size].end(), friend_address);
            free_blocks[block_size].erase(it);

            if (free_blocks[block_size].empty()) {
                for (int i=block_size; i >= memory_size/pow(2,division_limit); i-=pow(2,division_limit)) {
                    free_blocks.erase(i);
                }

                free_blocks.erase(block_size);

                // std::cout << "pop " << block_size << std::endl;
                // printFreeBlocks();
            }

            if (address < friend_address) { 
                free(address, block_size * 2);
            } else {
                free(friend_address, block_size * 2);
            }

        } else {
            free_blocks[block_size].push_front(address);
            free_blocks[block_size].sort();

            // czyszczenie, zwalnianie pamięci "wewnątrz" bloku, np. dla bloku 512 -> zwolnienie 2x 256, 4x 128, itd.
            // np. zwolnienie bloku zaczynającego się od adresu 0 o pojemności 512 zwolni całą pamięć od adresu 0 do 511 
            
            clear_below(address, block_size);

        }

    }

    // czyszczenie, zwalnianie pamięci "wewnątrz" bloku (zwalnianie całego bloku pamięci)
    void clear_below(size_t address, size_t block_size) {

        // sprawdź, czy istnieje blok poniżej
        if (free_blocks.find(block_size/2) != free_blocks.end()) {
            auto it = std::find(free_blocks[block_size/2].begin(), free_blocks[block_size/2].end(), address);
            if (it != free_blocks[block_size/2].end()) {
                free_blocks[block_size/2].erase(it);
            }

            it = std::find(free_blocks[block_size/2].begin(), free_blocks[block_size/2].end(), address + block_size/2);
            if (it != free_blocks[block_size/2].end()) {
                free_blocks[block_size/2].erase(it);
            }
            
            clear_below(address, block_size/2);
            clear_below(address + block_size/2, block_size/2);

        } else {
            if(free_blocks[block_size].empty()) free_blocks.erase(block_size);
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


//====================================== MAIN() =======================================


int main() {
    try {
        BuddyAllocator ba(1024, 5);
        std::pair<size_t, size_t> p;

        ba.printFreeBlocks();

        //--------------------------ALLOCATION---------------------------
        
        for (int i=0; i<4; i++) {
            std::cout << "\n-----Allocation: 40" << std::endl;

            p = ba.alloc(40);
            printAllocationResult(p);

            std::cout << std::endl;
            ba.printFreeBlocks();
        }

        //-----------------------------FREE------------------------------

        std::cout << "\n-----Free (64, 64)" << std::endl;

        ba.free(64, 64);

        std::cout << std::endl;
        ba.printFreeBlocks();

        
        std::cout << "\n-----Free (128, 64)" << std::endl;

        ba.free(128, 64);

        std::cout << std::endl;
        ba.printFreeBlocks();


        std::cout << "\n-----Free (0, 64)" << std::endl;

        ba.free(0, 64);

        std::cout << std::endl;
        ba.printFreeBlocks();

        //------------------------INNE PRZYKŁADY-------------------------

        // można też zwolnić cały blok pamięci (np. blok zaczynający się od adresu 0 o pojemności 512)
        std::cout << "\n-------------------------------------" << std::endl;
        std::cout << "Zwolnienie całego bloku pamięci:" << std::endl;
        std::cout << "\n-----Free (0, 512)" << std::endl;

        ba.free(0, 512);

        std::cout << std::endl;
        ba.printFreeBlocks();


        std::cout << "\n-----Allocation: 128" << std::endl;

        p = ba.alloc(128);
        printAllocationResult(p);

        std::cout << std::endl;
        ba.printFreeBlocks();


        // można też zwolnić całą dostępną pamięć
        std::cout << "\n-------------------------------------" << std::endl;
        std::cout << "Zwolnienie całej dostępnej pamięci:" << std::endl;
        std::cout << "\n-----Free (0, 1024)" << std::endl;

        ba.free(0, 1024);

        std::cout << std::endl;
        ba.printFreeBlocks();


        std::cout << "\n-----Allocation: 128" << std::endl;

        p = ba.alloc(128);
        printAllocationResult(p);

        std::cout << std::endl;
        ba.printFreeBlocks();


        // w przypadku próby zwolnienia niezalokowanej pamięci wystąpi błąd 
        std::cout << "\n-------------------------------------" << std::endl;
        std::cout << "Zwolnienie niezalokowanej pamięci:" << std::endl;
        std::cout << "\n-----Free (128, 128)" << std::endl;

        ba.free(128, 128);

        std::cout << std::endl;
        ba.printFreeBlocks();

    } catch (const std::exception &e) {
        std::cout << "\nError: " << e.what() << std::endl;
    }
    
    return 0;
}
