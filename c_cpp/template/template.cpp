#include <iostream>

template <class T>
class Container
{
    public:
        Container(T n) : member(n) {}
        
        T get() { return member; }

    private:
        T member;
};

template <class T>
void swap(T& a, T& b) {
    T tmp = a;

    a = b;
    b = tmp;
}

int main(void) {

    int a = 10;
    int b = 20;

    std::cout << "a = " << a << std::endl;

    swap(a, b);

    std::cout << "a = " << a << std::endl;

    Container<int> c(a);

    std::cout << c.get() << std::endl;

    return 0;
}
