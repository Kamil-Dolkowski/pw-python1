#include <iostream>
#include <unordered_map>
#include <set>
#include <algorithm>


// Zad.1
bool areAnagrams(std::string string1, std::string string2) {
    if (string1.size() != string2.size()) {
        return false;
    }

    std::transform(string1.begin(), string1.end(), string1.begin(), ::tolower);
    std::transform(string2.begin(), string2.end(), string2.begin(), ::tolower);

    std::unordered_map<char, unsigned int> numberOfChars1;
    std::unordered_map<char, unsigned int> numberOfChars2;

    for (int i=0; i < string1.size(); i++) {
        numberOfChars1[string1[i]] += 1;
        numberOfChars2[string2[i]] += 1;
    }

    for (const auto &value : numberOfChars1) {
        if (numberOfChars1[value.first] != numberOfChars2[value.first]) {
            return false;
        }
    }

    return true;
}

// Zad.2
std::set<std::string> getSubstring(std::string str) {
    std::set<std::string> result;

    for (int j=0; j < str.size(); j++) {
        for (int i=1; i <= str.size()-j; i++) {
            //std::cout << str.substr(j,i) << std::endl;
            result.insert(str.substr(j,i));
        }
    }

    return result;
}

// Zad.3

// #include <iostream>
// #include <array>
// #include <algorithm>

// int main()
// {
//     std::array<int,11> arr = {1,4,7,6,9,0,3,4,5,2,1};
//     // std::swap
    
//     return 0;
// }


int main() {
    bool x = areAnagrams("arbuz", "Burza");
    std::cout << "Are anagrams: " << x << std::endl;

    std::set<std::string> result = getSubstring("kamil");
    
    std::cout << "\nSubstrings: " << std::endl;
    for (std::string i : result) {
        std::cout << i << std::endl;
    }

    return 0;
}