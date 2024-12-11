#include <iostream>
#include <unordered_map>
#include <fstream>
#include <string>

class Configuration {
public:
    ~Configuration() {
        std::cout << "Dekonstruktor" << std::endl;
        for (auto const& x : string_string_map) {
            std::cout << x.first << std::endl;
        }
    }

    static Configuration& getInstance() {
        static Configuration instance;
        return instance;
    }

    void set(const std::string &key, const std::string &value) {
        string_string_map[key] = value;
    }

    void set(const std::string &key, const int value) {
        string_int_map[key] = value;
    }

    std::string getString(const std::string &key) {
        return string_string_map[key];
    }

    int getInt(const std::string &key) {
        return string_int_map[key];
    }

private:
    Configuration() {
        std::ifstream string_file ("config_string.txt");
        std::ifstream int_file ("config_int.txt");
        std::string line;
        std::string key, value_string;
        int value_int;
        
        // file_read<std::string>(string_file, string_string_map);
        // file_read<int>(int_file, string_int_map);

        if (string_file.is_open()) {
            while (!string_file.eof()) {
                getline(string_file, key, '=');
                if (key == "") break;
                getline(string_file, value_string, '\n');
                
                string_string_map[key] = value_string;
                
                //std::cout << key << ": " << value_string <<std::endl;
            }

            string_file.close();
        } else {
            std::cout << "Error: File does not exist." << std::endl;
        }

        if (int_file.is_open()) {
            while (!int_file.eof()) {
                getline(int_file, key, '=');
                if (key == "") break;
                getline(int_file, value_string, '\n');
                
                value_int = stoi(value_string);
                string_int_map[key] = value_int;
                
                //std::cout << key << ": " << value_int <<std::endl;
            }

            string_file.close();
        } else {
            std::cout << "Error: File does not exist." << std::endl;
        }
        
        
    }


    // //NIEZROBIONY POMYSL:

    // template<typename T>
    // static void file_read(std::ifstream &file, std::unordered_map<std::string, T> &map) {
    //     std::string key;
    //     std::string value_str;

    //     if (file.is_open()) {
    //         while (!file.eof()) {
    //             getline(file, key, '=');
    //             if (key == "") break;
    //             getline(file, value_str, '\n');
                
                

    //             // constexpr bool isInt = typeid(T) == typeid(int);

    //             if (typeid(T) == typeid(int)) {
    //                 value_str=stoi(value_str);
    //                 map[key] = value_str;
    //             } else {
    //                 // map[key] = value_str;
    //             }
                
                
    //             std::cout << key << ": " << value_str <<std::endl;
    //         }

    //         file.close();
    //     } else {
    //         std::cout << "Error: File does not exist." << std::endl;
    //     }

    // }

    std::unordered_map<std::string, std::string> string_string_map;
    std::unordered_map<std::string, int> string_int_map;
};





int main() {
    Configuration& config = Configuration::getInstance();

    std::cout << config.getString("config1") << std::endl;
    std::cout << config.getInt("config_int1") << std::endl;
    std::cout << config.getString("config2") << std::endl;
    return 0;
}