#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdlib>
#include <math.h>
#include <time.h>
using namespace std;

const double beta = 10;
const double dltx = 0.001;

double Potential(double x);

int main() {
    double x, P, U, base;
    double intU, intX, intX2;

    base = 0;

    for (x = -100; x <= 100; x += dltx) {
        U = Potential(x);
        base += exp(-beta * U) * dltx;
    }
    cout << base << endl;

    intU = 0;
    for (x = -100; x <= 100; x += dltx) {
        U = Potential(x);
        P = exp(-beta * U);
        intU += U * P * dltx / base;
    }
    cout << "<U> = " << intU << endl;

    intX = 0;
    for (x = -100; x <= 100; x += dltx) {
        U = Potential(x);
        P = exp(-beta * U);
        intX += x * P * dltx / base;
    }
    cout << "<x> = " << intX << endl;

    for (x = -100; x <= 100; x += dltx) {
        U = Potential(x);
        P = exp(-beta * U);
        intX2 += x * x * P * dltx / base;
    }
    cout << "<x2> = " << intX2 << endl;

}

double Potential(double x) {
    double potential;
    potential = x * x / 2;
    return potential;
}