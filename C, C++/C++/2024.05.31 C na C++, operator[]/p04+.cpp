#include <iostream>
#include <cstdlib>
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
        cout << "Resize" << endl;
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
  
  
};



//==============================MAIN==================================

int main(void) {
  DynamicTable<int> tab;

  tab.print();
  
  tab.addElement(1);
  tab.addElement(2);
  tab.addElement(3);
  tab.addElement(4);
  tab.addElement(5);
  //tab.addElement(6);
  
  tab.print();
  //------------------getElement----------------------
  try {
    cout << "\n==================" << endl;
    cout << tab.getElement(4) << endl;
    cout << tab.getElement(7) << endl;
  } catch (const std::out_of_range& e){
    cout << e.what() << endl;
  }
  //-----------------updateElement--------------------
  try {
    cout << "\n==================" << endl;
    tab.updateElement(22,1);
    tab.print();
    tab.updateElement(22,10);
    tab.print();
  } catch (const std::out_of_range& e) {
    cout << e.what() << endl;
  }
  //--------------DynamicTable<double>----------------
  cout << "\n==================" << endl;
  
  DynamicTable<double> tabD;
  
  tabD.addElement(1.1);
  tabD.addElement(2.2);
  tabD.addElement(3.3);
  tabD.addElement(4.4);
  tabD.addElement(5.5);
  
  tabD.print();
  //------------------operator []---------------------  !!!
  cout << "\n==================" << endl;
  
  tabD[1] = 10.7;
  tabD.print();
  
  cout << tabD[1] << endl;
  
  return 0;
}
