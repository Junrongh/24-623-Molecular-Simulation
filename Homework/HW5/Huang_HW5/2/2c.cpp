#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdlib>
#include <math.h>
#include <time.h>
using namespace std;

ofstream data_out("2c.txt");

const int STEP = 2000000; // Number of states
const double BETA = 10; // Constant beta in calculation
const double Utotal1 = 0;
const double Utotal2 = 1;
const double Utotal3 = 1;
const double Utotal4 = 3;

double random(double min, double max);

int main() {
    int i;
    double trial, Utrial;
    double B, epsilon;
    double U;
    double Usum;

    srand(time(NULL));

    Usum = 0;
    U = Utotal1;
    for (i = 0; i < STEP; i++) {
        Usum = Usum + U;
        data_out << i + 1 << ' ' << U << ' ' << Usum / (i + 1) << endl;
        trial = random(0, 1);
        if (trial <0.25 and trial >= 0) {
            Utrial = Utotal1;
        }
        else if (trial <0.50 and trial >= 0.25) {
            Utrial = Utotal2;
        }
        else if (trial <0.75 and trial >= 0.50) {
            Utrial = Utotal3;
        }
        else if (trial <= 1 and trial >= 0.75) {
            Utrial = Utotal4;
        }
        if (U > Utrial) {
            U = Utrial;
        }
        else {
            B = exp(-BETA * (Utrial - U));
            epsilon = random(0, 1);
            if (epsilon <= B) {
                U = Utrial;
            }
            else {
                U = U;
            }
        }
    }
    cout << Usum / (i + 1) << endl;
}

double random(double min, double max) {
    double res;
    res = (max - min) * rand() / RAND_MAX + min;
    return res;
}