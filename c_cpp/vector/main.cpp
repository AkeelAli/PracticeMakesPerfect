#include <vector>
#include <iostream>
#include "object.cpp"
#include <memory>

using namespace std;
	
vector<shared_ptr<object>> arr; 

shared_ptr<object>
get_object(size_t idx)
{
	return arr[idx];
}

int main(void) {
	arr.resize(2);

	arr[1] = make_shared<object>(1);

	cout << get_object(1)->m_value;

	return 0;
}
