//Zad.
//Zamiana liczby dziesietnej na dwojkowa.
//dziesietna calkowita (dodatnia) na dwojkowa (ciag 0 i 10 w tablicy)

//----------------------------------------------------------------------

#include <iostream>
#include <iomanip>
using namespace std;

template <typename Element>

class DynamicTable {
private:
  unsigned int size;
  unsigned int idx; 
  Element *elements;
public:
  DynamicTable() {
    size = 0;
    idx = 0; 
    elements = nullptr;
  }
  ~DynamicTable() {
    delete [] elements;
  }
  void addElement(Element element) {
    Element * newTable;
    int i;
  
    if (size == 0) {
      try {
        elements = new Element [1];
        size = 1;
        idx = 0;
        elements[idx] = element;
      } catch (bad_alloc&) {
        cout << "ERROR" << endl;
        return;
      }
    } else {
      if (idx<size-1) {
        idx += 1;
        elements[idx] = element;
      } else {
        //cout << "Resize" << endl;
        try {
          newTable = new Element [size*2]; // malloc(sizeof(int) * (size) * 2);
          for(i = 0; i<size; i++) {
            newTable[i] = elements[i];
          }
          size *= 2;
          idx += 1;
          delete [] elements;
          elements = newTable;
          elements[idx] = element;
        } catch (bad_alloc&) {
          cout << "ERROR" << endl;
          return;
        }
      }
    }
    
  }
  
  Element getElement(unsigned int index) {
    if (index>idx) {
      throw std::out_of_range ("Index out of range");
    }
    
    return elements[index];
  }
  
  void updateElement(Element element, unsigned int index) {
    if (index>idx) {
      throw std::out_of_range ("Index out of range");
    }
    
    elements[index] = element;
  }
  
  void print() {
    cout << "size: " << size << ", last element index: " << idx << endl;
    if (size != 0) {
      for (int i=0; i<=idx; i++) {
        cout << "array[" << i << "]: " << elements[i] << endl;
        //printf("array[%d]: %d\n", i, elements[i]);
      }
    }
  }
  
  Element& operator[] (int index) {       // !!!
    return elements[index];
  }
  
  unsigned int count() {
    return idx + 1;
  }
};


//-----------------------------------------------

DynamicTable<char> decimalToBinary(unsigned int n) {
  unsigned int r, c;
  DynamicTable<char> result;
  
  while (n > 0) {
    r = n % 2;
    c = n / 2;
    n = c;
    //cout << r << endl;
    result.addElement(r);
  }
  
  return result;
}


class Binary {
private:
  DynamicTable<char> digits;
public:
  Binary():Binary(0) {} 
  
  Binary(unsigned int n) {
    unsigned int r, c;
    
    while (n > 0) {
      r = n % 2;
      c = n / 2;
      n = c;
      //cout << r << endl;
      digits.addElement(r);
    }
  }
  
  void print() {
    for (int i=digits.count()-1; i>=0; i--) {
      //cout << static_cast<int>(digits[i]);
      cout << std::left << std::setw(5) << static_cast<int>(digits[i]);
    }
  }
  
  unsigned int count() {
    return digits.count();
  }
  
  char& operator[] (int index) { 
    return digits[index];
  }
};


Binary add(Binary b1, Binary b2) {
  Binary result;
  unsigned int i=0, c_in=0, c_out=0, d=0;
  int d1, d2;
  
  while (true) {
    c_in = c_out;
    if(i < b1.count() && i < b2.count()) {
      d1 = b1[i];
      d2 = b2[i];
      if (d1 + d2 + c_in == 0) {
        d = 0;
        c_out = 0;
      } else if (d1 + d2 + c_in == 1) {
        d = 1;
        c_out = 0;
      } else if (d1 + d2 +c_in == 2) {
        d = 0;
        c_out = 1;
      } else if (d1 + d2 + c_in == 3) {
        d = 1;
        c_out = 1;
      }
      result[i] = d;
    } else if(i == b1.count() && i == b2.count() && c_out == 1) {
      result[i] = c_out;
      break;
    }
    i++;
    
  }
  
  return result;
}


//c_in    d1    d2  |  d    c_out
// 0      0     0   |  0     0
// 0      0     1   |  1     0
// 0      1     0   |  1     0
// 0      1     1   |  0     1

//c_in    d1    d2  |  d    c_out
// 1      0     0   |  1     0
// 1      0     1   |  0     1
// 1      1     0   |  0     1
// 1      1     1   |  1     1



//13 -> 0000 1101

//13 = 2*6+1
//6 = 2*3+0
//3 = 2*1+1
//1 = 2*0+1
//0



//==============================MAIN==================================

int main(void) {
  Binary b;
  Binary b1(9);
  Binary b2(13);
  
  b1.print();
  b2.print();
  
  b = add(b1, b2);
  
  b.print();
  
  return 0;
}






//wypisywanie szerokosci pól



