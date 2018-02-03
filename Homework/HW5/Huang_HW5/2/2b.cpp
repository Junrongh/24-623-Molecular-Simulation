#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdlib>
#include <math.h>
#include <time.h>
using namespace std;

ofstream data_out("2b.txt");

int main() {
    double beta;
    double U;
    for (beta = 0.001; beta <= 100; beta += 0.001) {
        U = (3 * exp(-3 * beta) + 2 * exp(-beta)) / (1 + exp(-3 * beta) + 2 * exp(-beta));
        data_out << beta << ' ' << U << endl;
    }
}