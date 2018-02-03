#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdlib>
#include <math.h>
#include <time.h>
using namespace std;

ofstream result("result.txt");

const double Q = 0;
const double PI = 3.14159265358979;
const double m = 1;

double random(double min, double max);
double potential(double x);
double x_start(double epsilon);

int main() {
    int i;
    int M = 0;
    int STEP = 1000000;
    double trialmax = 1;
    double epsilon = 0.1;
    double beta = 0.1;
    double x_old, x_new;
    double U_old, U_new;
    double prob, B;
    double ktst;
    srand(time(NULL));
    for (i = 0; i < STEP; i++) {
        if (i % 1000 == 0) {
            cout << i << endl;
        }
        result << x_start(epsilon) << endl;
    }
}

// Generate random number bertween (min, max)
double random(double min, double max) {
    double res;
    res = (max - min) * rand() / RAND_MAX + min;
    return res;
}
// Potential equation
double potential(double x) {
    double x2, U;
    x2 = x * x;
    U = x2 * x2 - 2 * x2 + 1;
    return U;
}
// Generate starting point according to Boltzmann distribution
double x_start(double epsilon) {
    int i, step = 10000;
    double x, x_trial;
    double U, U_trial;
    double beta = 0.1;
    double trialmax = 1; // From HW5 we get that trialmax = 2.5
    double prob, B;
    x = -1;
    for (i = 0; i < step; i++) {
        x_trial = x + random(-trialmax, trialmax);
        U = potential(x);
        U_trial = potential(x_trial);
        if (x_trial >= Q + epsilon / 2) {
            x = x;
        }
        else if (U_trial < U) {
            x = x_trial;
        }
        else {
            B = exp(-beta * (U_trial - U));
            prob = random(0, 1);
            if (prob <= B) {
                x = x_trial;
            }
            else {
                x = x;
            }
        }
    }
    return x;
}