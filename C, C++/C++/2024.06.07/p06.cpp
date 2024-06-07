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
#include <cmath>

template <typename Element>
class DynamicTable{
private:
	unsigned int size;
	unsigned int idx; 
	Element *elements;
public:
	int id;
	DynamicTable(){
		size = 0;
		idx = 0;
		//https://stackoverflow.com/a/20509811
		elements = nullptr;
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

	  size = t.size;
	  idx = t.idx;
	  elements = new Element[t.size];
	  for (int i=0; i<=t.idx; i++) {
	    elements[i] = t.elements[i];
	  }
	}
	
	DynamicTable& operator= (const DynamicTable& t) {

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


class Number {
  public:
    // Nie tak
    //void print() {};
    //unsigned long int toDecimal() {};
  
    virtual void print() = 0;
    virtual unsigned long int toDecimal() = 0;
};
	
class Binary : public Number {
	private:
		DynamicTable<char> digits;
	public:
		Binary(){}
		Binary(unsigned int n){
			unsigned int r,c;
			
			if (n == 0) {
			  digits.addElement(0);
			} else {
  			while (n > 0){
  				r = n % 2;
  				c = n / 2;
  				n = c;
  				digits.addElement(r);
  			}
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
	    
	    unsigned long int toDecimal() {
	      char c;
	      unsigned int sum = 0;
	      
	      for (int i=0; i<digits.count(); i++) {
	        c = digits[i];
	        sum += pow(2,i) * c;
	      }
        return sum;
	    }
	    
	    /*
	    //toDecimal inna wersja                                     !!!
	    unsigned long int toDecimal() {
	      unsigned long int s = digits.getElement(digits.count()-1);
	      
	      for (int i=digits.count()-2; i>=0; i--) {
	        s = s*2 + digits.getElement(i);
	      }
	      
        return s;
	    }
	    
	    //1011
	    //2^3*1 + 2^2*0 + 2^1*1 + 2^0*1 = (((((1*2)+0)*2)+1)*2)*1
	    */
};


class Decimal : public Number {
  private:
    Binary b;
  public:
    Decimal(){}
    Decimal(unsigned long int n) {
      b = Binary(n);
    }
    
    unsigned long int toDecimal() {
      return b.toDecimal();
    }
    
    friend Decimal add(Decimal d1, Decimal d2);
    
    void print() {
      std::cout << b.toDecimal() << std::endl;
    }
};


Binary add(Binary b1, Binary b2) {
	Binary result;
	int i=0;
	char c_in=0,c_out=0,d=0,d1=0,d2=0;
	
	int c1 = b1.count();
	int c2 = b2.count();
	
	if (c1 > c2) {
	  for (int i=0; i<c1-c2; i++) {
	    b2.addNextBit(0);
	  }
	} else if (c1 < c2) {
	  for (int i=0; i<c2-c1; i++) {
	    b1.addNextBit(0);
	  }
	}
	
	i=0;
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
		}else if(i==b1.count() && i==b2.count() && c_out==0){
			break;
		}
		i += 1;
	}
	return result;
	
}

Binary shift(Binary b, unsigned int by) {
  Binary bShifted;
  
  for (int i=0; i<by; i++) {
    bShifted.addNextBit(0);
  }
  
  for (int i=0; i<b.count(); i++) {
    bShifted.addNextBit(b.getBit(i));
  }
  
  return bShifted;
}

Binary mul(Binary b1, Binary b2) {
  Binary b1Zero;
  Binary s;
  Binary result(0);
  char b;
  
  
  for (int i=0; i<b1.count(); i++) {
    b1Zero.addNextBit(0);
  }
  
  for (int i=0; i<b2.count(); i++) {
    b = b2.getBit(i);
    //std::cout << "b=" << static_cast<int> (b2.getBit(i)) << std::endl;
    if (b == 0) {
      s = shift(b1Zero, i);
    } else { //b == 1
      s = shift(b1, i);
    }
    //std::cout << "i=" << i << std::endl;
    //result.print();
    //s.print();
    result = add(result, s);
    //result.print();
  }
  
  return result;
}


Decimal add(Decimal d1, Decimal d2) {
  Decimal d;
  
  d.b = add(d1.b, d2.b);
  return d;
}

class Fractional : public Number {
  private:
    Decimal numerator; // Licznik
    Decimal denominator; // Mianownik
  public:
    Fractional(unsigned long int n, unsigned long int d) {
      numerator = Decimal(n);
      denominator = Decimal(d);
    }
    
    void print() {
      numerator.print(); 
      std:: cout << "/" << std::endl;
      denominator.print();
    }
    
    unsigned long int toDecimal() {
      unsigned long int n = numerator.toDecimal();
      unsigned long int d = denominator.toDecimal();
      
      return n/d;
    }
    
    double toDecimalReal() {
      double n = numerator.toDecimal();
      double d = denominator.toDecimal();
      
      return n/d;
    }
};


int main(){
  // Nie tak
  /*
  Number numbers[2];
  
	Binary b1(19);
	Decimal d1(17);
	
	
	b1.print();
	std::cout << b1.toDecimal() << std::endl;
	
	d1.print();
	std::cout << d1.toDecimal() << std::endl;
	
	numbers[0] = b1;
	numbers[1] = d1;
	*/
	
  
  Number ** numbers = new Number * [3];
  Binary *b1 = new Binary(19);
  Decimal *d1 = new Decimal(17);
  Fractional *f1 = new Fractional(5,7);
  
  //Number n;   // To się nie uda
  
  numbers[0] = b1;
  numbers[1] = d1;
  numbers[2] = f1;
  
  for (int i=0; i<3; i++) {
    numbers[i] -> print();
    std::cout << numbers[i] -> toDecimal() << std::endl;
  }
  
  std::cout << f1 -> toDecimalReal() << std::endl;
  
  return 0;
}

