#include <iostream>

template <typename T>
class Node {
public:
    Node(T value) : data(value), next(nullptr) {}
    T data;
    Node<T> *next;
};


template <typename T>
class Container {
public:
    virtual void push(const T &value) = 0;
    virtual T pop() = 0;
    virtual bool isEmpty() const = 0;
    virtual size_t size() const = 0;
    virtual ~Container() {}
};


template <typename T>
class Queue : public Container<T> {
public:
    Queue() {}
    ~Queue() {}
    virtual void push(const T &value) {
        Node<T> *n = new Node<T>(value);
        n->next = head;
        head = n;
        std::cout << "push " << value << std::endl;
    };
    virtual T pop() {
        if (isEmpty()) {
            throw std::out_of_range("Stack is empty");
        }
        Node<T> *n = head;
        T ret = n->data;

        Node<T> *t = tail;
        while (t->next != head) {
            t = t->next;
            std::cout << t->data << std::endl;
        }

        t->next = nullptr;

        head = t;
        delete n;

        std::cout << "pop " << ret << std::endl;
        return ret; 
    };
    virtual bool isEmpty() const {
        if (head == nullptr) {
            return true;
        }
        return false;
    };
    virtual size_t size() const {
        size_t stack_size = 0;
        Node<T> *n = head;
        while (n != nullptr) {
            stack_size++;
            n = n->next;
        }
        return stack_size;
    };
private:
    Node<T> *head = nullptr;
    Node<T> *tail = nullptr;
};


template <typename T>
class Stack : public Container<T> {
public:
    Stack() {}
    ~Stack() {
        
    }
    virtual void push(const T &value) {
        Node<T> *n = new Node<T>(value);
        n->next = head;
        head = n;
        std::cout << "push " << value << std::endl;
    };
    virtual T pop() {
        if (isEmpty()) {
            throw std::out_of_range("Stack is empty");
        }
        Node<T> *n = head;
        T ret = n->data;
        head = n->next;
        delete n;
        std::cout << "pop " << ret << std::endl;
        return ret; 
    };
    virtual bool isEmpty() const {
        if (head == nullptr) {
            return true;
        }
        return false;
    };
    virtual size_t size() const {
        size_t stack_size = 0;
        Node<T> *n = head;
        while (n != nullptr) {
            stack_size++;
            n = n->next;
        }
        return stack_size;
    };
private:
    Node<T> *head = nullptr;
};



int main() {
    Queue<int> kolejka;
    Stack<int> stos;

    // try {
    //     stos.push(1);
    //     std::cout << "size " << stos.size() << std::endl;
    //     stos.pop();
    //     std::cout << "size " << stos.size() << std::endl;
    //     stos.pop();
    //     stos.pop();
    // } catch (std::exception &e) {
    //     std::cerr << e.what() << std::endl;
    // }

    try {
        kolejka.push(1);
        kolejka.push(2);
        // std::cout << "size " << kolejka.size() << std::endl;
        kolejka.pop();
        // std::cout << "size " << kolejka.size() << std::endl;
        // kolejka.pop();
        // kolejka.pop();
    } catch (std::exception &e) {
        std::cerr << e.what() << std::endl;
    }
    
    

    return 0;
}






// ==Stack==

// head
// 1
// 2
// 3