#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdlib>
#include <math.h>
#include <time.h>
using namespace std;

ofstream trial_out("trialout.txt");


const int STEP = 100000; // Number of states
const double X0 = 0; // Initial position
const double BETA = 10; // Constant beta in calculation

double random(double min, double max);
double Potential(double x);

int main() {
    double trial, Utrial;
    double B, epsilon;
    double U, x, x2;
    double Usum, xsum, x2sum;
    int i;
    double TRIALMAX;

    srand(time(NULL));

    for (TRIALMAX = 0.01; TRIALMAX < 20; TRIALMAX += 0.01) {
        cout << TRIALMAX << endl;
        Usum = xsum = x2sum = 0;
        x = X0;
        U = Potential(x);
        for (i = 0; i < STEP; i++) {
            Usum = Usum + U;
            xsum = xsum + x;
            x2sum = x2sum + x * x;

            trial = random(-TRIALMAX, TRIALMAX);
            Utrial = Potential(x + trial);
            if (Utrial <= U) {
                x = x + trial;
                U = Utrial;
            }
            else {
                epsilon = random(0, 1);
                B = exp(-BETA * (Utrial - U));
                if (epsilon <= B) {
                    x = x + trial;
                    U = Utrial;
                }
                else {
                    x = x;
                    U = U;
                }
            }
        }
        trial_out << TRIALMAX << ' ' << Usum / STEP << ' ' << xsum / STEP << ' ' << x2sum / STEP << endl;
    }

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