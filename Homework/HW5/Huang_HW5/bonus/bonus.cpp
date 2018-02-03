#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdlib>
#include <math.h>
#include <time.h>
using namespace std;

ofstream data_out("output.txt");
ofstream avgdata_out("avgoutput.txt");

const double TRIALMAX = 2.5; // Maximum trial
const int STEP = 1000000; // Number of states
const double X0 = 0; // Initial position
const double BETA = 10; // Constant beta in calculatio

double random(double min, double max);
double Potential(double x);

int main() {
    double trial, Utrial;
    double B, epsilon;
    double U, x, x2;
    double Usum, xsum, x2sum;
    int i;

    srand(time(NULL));

    Usum = xsum = x2sum = 0;

    x = X0;
    U = Potential(x);
    for (i = 0; i < STEP; i++) {
        Usum = Usum + U;
        xsum = xsum + x;
        x2sum = x2sum + x * x;
        data_out << i + 1 << ' ' << U << ' ' << x << ' ' << x*x << endl;
        avgdata_out << Usum / (i + 1) << ' ' << xsum / (i + 1) << ' ' << x2sum / (i + 1) << endl;

        trial = random(-TRIALMAX, TRIALMAX);
        Utrial = Potential(x + trial);

        epsilon = random(0, 1);
        B = exp(-BETA * (Utrial - U)) / (exp(-BETA * (Utrial - U)) + 1);
        if (epsilon <= B) {
            x = x + trial;
            U = Utrial;
        }
        else {
            x = x;
            U = U;
        }

    }
    cout << Usum / STEP << ' ' << xsum / STEP << ' ' << x2sum / STEP << endl;
}

double random(double min, double max) {
    double res;
    res = (max - min) * rand() / RAND_MAX + min;
    return res;
}

double Potential(double x) {
    double P;
    P = x * x * x * x - 2 * x * x + 1;
    return P;
}