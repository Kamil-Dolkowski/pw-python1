#include <iostream>
#include <cstdlib>
#include <time.h>
using namespace std;

void foo(int &a){
// Zmień wartość przekazanej zmiennej o losową liczbę
// z przedziału [1,10]
  int x;
  x = rand()%10 + 1;
  a = a + x;
}

int main(){
  srand(time(NULL));
  int a = 3;

  foo(a);
  // W tym momencie `a` powinno mieć wartość zmienioną o losową
  // liczbę z przedziału [1,10], a więc powinno być
  // w zakresie [4, 13]
  cout << a << endl;

  return EXIT_SUCCESS;
}
