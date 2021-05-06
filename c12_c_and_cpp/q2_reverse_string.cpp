// Implement a function void reverse(char* str) which reverses a null-terminated string.
#include <string>
#include <iostream>

using namespace std;

void reverse(char* str) {
  char* start = str;
  char* end = start +strlen(str) -1;

  char temp;

  while (start < end) {
    temp = *end;
    *end = *start;
    *start = temp;
    start++;
    end--;
  }
}

int main() {
  char test[] = "Retake the falling snow: each drifting flake";
  cout << test << endl;
  reverse(test);
  cout << test << endl;
}