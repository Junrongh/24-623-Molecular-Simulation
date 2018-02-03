#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdlib>
#include <math.h>
#include <time.h>
using namespace std;

ifstream position("../liquid256.txt");
ofstream p_out("p.txt");

const int N = 256, STEP = 1000000;
const double TRIALMAX = 0.1;
const double L = 7.26194, RC = 2.5;
const double KB = 1.3806e-23;
const double T = 100;
const double EPSILON = 1.67e-21;
const double SIGMA = 3.4e-10;
const double MASS = 6.63e-26;
const double BETA = 1 / (KB * T);


void checkr(double r[3], double bot, double up);
double random(double min, double max);
double distance(double r1[3], double r2[3]);
double getURC(double r);
double getFRC(double r);
double LJ(double r, double URC, double FRC);
double force(double r, double URC, double FRC);
double potential(double r[N][3], double URF, double FRC);
double trial(double r[N][3], int n, double r_ori[3], double r_trial[3], double URC, double FRC);
double pressure(double T, double r[N][3], double URC, double FRC);


int main() {
    srand(unsigned(time(NULL)));
    int i, j, k, t, n;
    double r[N][3], m[N];
    double U, Utotal, deltaU; // Define energy and momenta
    double P, Ptotal;
    double URC, FRC;
    double tempr, tempf, temp;
    double r_ori[3], r_trial[3];
    double epsilon, B;

    URC = getURC(RC);
    FRC = getFRC(RC);
    Utotal = 0;
    Ptotal = 0;

    // Initialize the position, mass, force, energy, generate random value of velocity
    for (i = 0; i < N; i++) {
        for (k = 0; k < 3; k++) {
            position >> r[i][k];
            r[i][k] = r[i][k]/6.8*L;
        }
        m[i] = 1;
        checkr(r[i], 0, L);
    }

    // Loop with steps
    for (t = 0; t < STEP; t++) {
        if (t % 1000 == 0) {
            cout << "Time step: " << t << endl;
        }
        n = floor(random(0, N));
        for (k = 0; k < 3; k++) {
            r_ori[k] = r[n][k];
            r_trial[k] = r_ori[k] + random(-TRIALMAX, TRIALMAX);
        }
        checkr(r_trial, 0, L);
        deltaU = trial(r, n, r_ori, r_trial, URC, FRC);
        if (deltaU <= 0) {
            for (k = 0; k < 3; k++) {
                r[n][k] = r_trial[k];
            }
        }
        else {
            B = exp(-BETA * deltaU * EPSILON);
            epsilon = random(0, 1);
            if (epsilon <= B) {
                for (k = 0; k < 3; k++) {
                    r[n][k] = r_trial[k];
                }
            }
        }

        P = pressure(T, r, URC, FRC);
        Ptotal = Ptotal + P;
        if (t % 10000 ==0) {
            p_out << t << ' ' << P << ' ' << Ptotal / (t + 1) << endl;
            cout << Ptotal / (t + 1) << endl;
        }
    }
    cout << Ptotal/(STEP) << endl;
}

// Calculate the cutoff potential and force(they are both constant values)
double getURC(double r) {
    double u;
    double r2, r4, r6;
    r2 = r * r;
    r4 = r2 * r2;
    r6 = r4 * r2;
    u = 4 / (r6 * r6) - 4 / r6;
    return u;
}
double getFRC(double r) {
    double f;
    double r2, r4, r6;
    r2 = r * r;
    r4 = r2 * r2;
    r6 = r4 * r2;
    f = 48 / (r6 * r6 * r) - 24 / (r6 * r);
    return f;
}
double random(double min, double max) {
    double res;
    res = (max - min) * rand() / RAND_MAX + min;
    return res;
}

void checkr(double r[3], double bot, double up) {
    int k;
    for (k = 0; k < 3; k++) {
        if (r[k] > up) {
            r[k] = r[k] - L;
        }
        else if (r[k] < bot) {
            r[k] = r[k] + L;
        }
    }
}
// Given two vectors, calculate the distance scalar between the two given atoms
double distance(double r1[3], double r2[3]) {
    double d = 0;
    double vecr[3];
    int k;
    for (k = 0; k < 3; k++) {
        vecr[k] = r1[k] - r2[k];
    }
    checkr(vecr, -L / 2, L / 2);
    for (k = 0; k < 3; k++) {
        d = d + vecr[k] * vecr[k];
    }
    return sqrt(d);
}
// Given distance between atoms, calculate the potential energy
double LJ(double r, double URC, double FRC) {
    double u;
    double r2, r4, r6;
    if (r > RC) {
        u = 0;
    }
    else {
        r2 = r * r;
        r4 = r2 * r2;
        r6 = r4 * r2;
        u = 4 / (r6 * r6) - 4 / r6 - URC + FRC * (r - RC);
    }

    return u;
}
// Given distance between atoms, calculate the force/distance scalar
double force(double r, double URC, double FRC) {
    double f;
    double r2, r4, r6;
    if (r > RC) {
        f = 0;
    }
    else {
        r2 = r * r;
        r4 = r2 * r2;
        r6 = r4 * r2;
        f = 48 / (r6 * r6 * r) - 24 / (r6 * r) - FRC;
    }
    return f;
}

// Given position of all atoms, calculate teh system potential energy
double potential(double r[N][3], double URC, double FRC) {
    double d, Potential;
    int i, j;
    Potential = 0;
    for (i = 0; i < N; i++) {
        for (j = i + 1; j < N; j++) {
            d = distance(r[i], r[j]);
            Potential = Potential + LJ(d, URC, FRC);
        }
    }
    return Potential;
}

// Given a original position and a trial move, calculate the deltaU
double trial(double r[N][3], int n, double r_ori[3], double r_trial[3], double URC, double FRC) {
    int i;
    double d_ori, d_trial;
    double deltaU;
    double Potential_ori, Potential_trial;
    Potential_ori = Potential_trial = 0;
    for (i = 0; i < N; i++) {
        if (i != n) {
            d_ori = distance(r_ori, r[i]);
            d_trial = distance(r_trial, r[i]);
            Potential_ori = Potential_ori + LJ(d_ori, URC, FRC);
            Potential_trial = Potential_trial + LJ(d_trial, URC, FRC);
        }
    }
    deltaU = Potential_trial - Potential_ori;
    return deltaU;
}
// Calculate time-related Pressure with given Force and Position
double pressure(double T,  double r[N][3], double URC, double FRC) {
    double Pressure;
    int i, j, k;
    double tempr,  tempf;
    double vecr[3], zeror[3], vecf[3];
    zeror[0] = zeror[1] = zeror[2] = 0;
    Pressure = N * KB * T;
    for (i = 0; i < N; i++) {
        for (j = i + 1; j < N; j++) {
            // Check whether the vector rij matches the minimum mirror rule
            for (k = 0; k < 3; k++) {
                vecr[k] = r[i][k] - r[j][k];
            }
            checkr(vecr, -L / 2, L / 2);
            tempr = distance(vecr, zeror);
            tempf = force(tempr, URC, FRC);
            for (k = 0; k < 3; k++) {
                vecf[k] = tempf / tempr * vecr[k];
                Pressure = Pressure + vecf[k] * vecr[k] * EPSILON / 3;
            }
        }
    }
    Pressure = Pressure / (L * SIGMA * L * SIGMA * L * SIGMA);
    return Pressure;
}