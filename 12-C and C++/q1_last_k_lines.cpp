// Write a method to print the last K lines of an input file.

#include <iostream>
#include <fstream>

using namespace std;

void printLastKLines(char* fileName, int K) {
  const int k = K;
  ifstream file (fileName);
  string L[k];
  int size = 0;

  while (file.peek() != EOF) {
    getline(file, L[size%k]);
    size++;
  }

  int start = size > k ? (size%k) : 0;
  int count = min(k, size);

  for (int i = 0; i < count; i++) {
    cout << L[(start+i)%k] << endl;
  }
}

int main() {
  printLastKLines((char*)"q1_testFile.txt", 7);
}