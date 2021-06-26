#include <string>
#include <iostream>
#include <set>

using namespace std;

string twoStrings(string s1, string s2) {
	set<char> s1_set;
	set<char> s2_set;

	for(char c: s1) {
		s1_set.insert(c);
	}
	
	for(char c: s2) {
		s2_set.insert(c);
	}

	for (char c = 'a'; c <= 'z'; c++) {
		if (s1_set.count(c) and s2_set.count(c)) {
			return "YES";
		}
	}

	return "NO";
}

int main() {

	cout << twoStrings("yoyo", "bilim") << endl;

	return 0;
}

