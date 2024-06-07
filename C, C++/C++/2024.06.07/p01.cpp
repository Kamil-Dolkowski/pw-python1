/*
1 0 
1 1 
before add
1 0 1 
delete id=3, elements=3
delete id=1, elements=2
delete id=2, elements=2
result of add
5350-124
end
delete id=2, elements=2
free(): double free detected in tcache 2
*/

#include <iostream>
#include <iomanip>

template <typename Element>
class DynamicTable{
private:
	unsigned int size;
	unsigned int idx; 
	Element *elements;
public:
  static int counter;
	int id;
	DynamicTable(){
		size = 0;
		idx = 0;
		//https://stackoverflow.com/a/20509811
		elements = nullptr;
		id = counter;
		counter++;
	}
	
	void addElement(Element element){
		Element * newTable;
		if (size == 0) {
			//https://stackoverflow.com/a/6833214
			try {
				elements = new Element[1];
				size = 1;
				idx = 0;
				elements[idx] = element;
			}catch (std::bad_alloc&) {
				std::cout<<"ERROR"<<std::endl;
				return;
			}
		} else {
			if (idx< size-1) {
				idx += 1;
				elements[idx] = element;
			} else {
				try {
					newTable = new Element[size*2];
					for(int i = 0; i<size; i++) {
						newTable[i] = elements[i];
					}
					size *= 2;
					idx += 1;
					delete [] elements;
					elements = newTable;
					elements[idx] = element;
				} catch (std::bad_alloc&) {
					std::cout<<"ERROR"<<std::endl;
					return;
				}
			}
		}
	}
	
	~DynamicTable(){
	    std::cout<<"delete id="<<id<<", elements="<<(idx+1)<<std::endl;
		delete [] elements;
	}
	
	Element getElement(unsigned int idx){
		if(idx>this->idx){
			throw std::out_of_range("Index out of range");
		}
		
		return elements[idx];
		
	}
	
	void updateElement(Element element, unsigned int idx){
		if(idx>this->idx){
			throw std::out_of_range("Index out of range");
		}
		elements[idx]=element;
	}
	
	void print(){
		int i;
		std::cout<<"size: "<< size <<", last element index: "<< idx <<std::endl;
		for(i=0; i<=idx; i++) {
			std::cout<<"index: " << i << ", element: " << elements[i] << std::endl;
		}	
	}
	
	Element& operator[](unsigned int idx){
		return elements[idx];
	}
	
	unsigned int count(){
		return idx+1;
	}
	
	DynamicTable (const DynamicTable & t) {
	  std::cout << "Copy constructor" << t.id << std::endl;
	  
	  size = t.size;
	  idx = t.idx;
	  elements = new Element[t.size];
	  for (int i=0; i<=t.idx; i++) {
	    elements[i] = t.elements[i];
	  }
	}
	
	DynamicTable& operator= (const DynamicTable& t) {
	  std::cout << "Copy assignment" << t.id << std::endl;
	  
	  if (elements != nullptr) {
	    delete [] elements;
	  }
	  
	  size = t.size;
	  idx = t.idx;
	  elements = new Element[t.size];
	  for (int i=0; i<=t.idx; i++) {
	    elements[i] = t.elements[i];
	  }
	  
	  return *this;
	}
};

template <typename Element>
int DynamicTable<Element>::counter = 0;
	
class Binary{
	private:
		DynamicTable<char> digits;
	public:
		Binary(){}
		Binary(unsigned int n){
			unsigned int r,c;
			while (n > 0){
				r = n % 2;
				c = n / 2;
				n = c;
				digits.addElement(r);
			}
		}
		
		void print()
		{	
			for (int i=digits.count()-1 ; i>=0 ; i--){
				std::cout<<std::left<<std::setw(2) << static_cast<int>(digits[i]);
				
			}
			std::cout<<std::endl;
		}
		
		unsigned int count(){
			return digits.count();
		}
		
		char getBit(unsigned int idx){
		    if(idx >= digits.count()){
			    throw std::out_of_range("Index out of range");
		    }
		
		    return digits.getElement(idx);
	    }
	
	    void updateBit(char value, unsigned int idx){
		    if(idx >= digits.count()){
			    throw std::out_of_range("Index out of range");
		    }
		    digits.updateElement(value, idx);
	    }
	    
	    void addNextBit(char value){
		    digits.addElement(value);
	    }
};

Binary add(Binary b1, Binary b2)
{
	Binary result;
	int i=0;
	char c_in=0,c_out=0,d=0,d1=0,d2=0;
	while (true){
		c_in=c_out;
		if(i<b1.count() && i<b2.count()){
			d1=b1.getBit(i);
			d2=b2.getBit(i);
			if(d1+d2+c_in==0){
				d=0;
				c_out=0;
			}else if(d1+d2+c_in==1){
				d=1;
				c_out=0;
			}else if(d1+d2+c_in==2){
				d=0;
				c_out=1;
			}else if(d1+d2+c_in==3){
				d=1;
				c_out=1;
			}
			result.addNextBit(d);
		}else if(i==b1.count() && i==b2.count() && c_out==1){
		    result.addNextBit(c_out);
			break;
		}
		i += 1;
	}
	result.print();
	return result;
}

int main(){
	Binary b;
	Binary b1(2);
	Binary b2(3);
	b1.print();
	b2.print();
	std::cout<<"before add"<<std::endl;
	b = add(b1,b2);
	std::cout<<"result of add"<<std::endl;
	b.print();
	std::cout<<"end"<<std::endl;
}