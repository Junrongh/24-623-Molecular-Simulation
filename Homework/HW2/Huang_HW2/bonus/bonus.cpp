#include <iostream>
#include <fstream>
#include <iomanip>
#include <math.h>
#include <time.h>
using namespace std;

ofstream gen("2-9.txt");
ifstream input("2-9.txt");
ofstream energy_out("energy.txt");
ofstream momenta_out("momenta.txt");
ofstream VMD_out("vmd.xyz");

const int T = 40000;
const double dlt = 0.002, ETA = 2;

double pow6m(double x);
double distance(double r1[3], double r2[3]);
double potential(double r);
double force(double r);
double kinetic(double v[3]);
double verletv1(double v, double f, double m, double eta);
double verletv2(double v, double f, double m, double eta);


int main() {
    int N, n;
    cout << "Enter the number of atoms: ";
    cin >> N;
    int i, j, k, t;
    double m[N]; // Define Mass
    double r[N][3], v[N][3], f[N][3], tempv[N][3];
    double K[T], U[T], E[T], M[T][3]; // Define energy and momenta
    double tempr, tempu, tempf;
    int label[N];

    n = 27;
    srand((unsigned)time(NULL));
    label[0] = rand() % n + 1;
    for (i = 0; i < N; i++) {
Lab:  label[i] = rand() % n + 1;
        for (j = 0; j < i; j++) {
            if (label[i] == label[j]) goto Lab;
            else if ((label[i] % 3 + (label[i] / 3) % 3 + ((label[i] / 3) / 3) % 3) % 2 == 1) goto Lab;

        }
    }

    for (i = 0; i < N; i++) {
        r[i][2] = label[i] % 3 * 1 + 0.95;
        r[i][1] = (label[i] / 3) % 3 * 1 + 0.95;
        r[i][0] = ((label[i] / 3) / 3) % 3 * 1 + 0.95;
        gen << r[i][0] << ' ' << r[i][1] << ' ' << r[i][2] << endl;
    }

    // Initialize the mass, position and velocity
    for (i = 0; i < N; i++) {
        for (k = 0; k < 3; k++) {
            input >> r[i][k];
            m[i] = 1;
            v[i][k] = 0;
            f[i][k] = 0;
            tempv[i][k] = 0;
        }
    }

    // Loop one step and initialize the force of each atom
    for (i = 0; i < N; i++) {
        for (j = 0; j < N; j++) {
            if (j == i) ;
            else {
                tempr = distance(r[i], r[j]); // Calculate the distance between two atoms
                tempf = force(tempr); // Calculate the force(scalar) between two atoms
                for (k = 0; k < 3; k++) {
                    f[i][k] += tempf / tempr * (r[i][k] - r[j][k]); // Spilt force into each axis
                }
            }
        }
    }

    // Loop for T steps
    for (t = 0; t < T; t++) {
        K[t] = 0;
        U[t] = 0;
        E[t] = 0;
        for (k = 1; k < 3; k++) {
            M[t][k] = 0; // Initialize the monenta
        }
        // Make general VMD output form
        VMD_out << N << "\n";
        VMD_out << N << " Ar LJ Simulization\n";
        for (i = 0; i < N; i++)
        {
            VMD_out << "Ar " << r[i][0] << " "
                    << r[i][1] << " " << r[i][2] << "\n";
        }
        // Loop for every atom
        for (i = 0; i < N; i++) {
            for (k = 0; k < 3; k++) {
                tempv[i][k] = verletv1(v[i][k], f[i][k], m[i], ETA); // Verlet loop, calculate the velocity of (t + dlt / 2)
                r[i][k] = r[i][k] + tempv[i][k] * dlt; // Verlet loop, calculate the new position of (t + dlt)
            }
        }

        for (i = 0; i < N; i++) {
            // Initialize the temp storage of f
            tempf = 0;
            for (k = 0; k < 3; k++) {
                f[i][k] = 0;
            }
            // Update the potential energy, kinetic energy and force with time step
            for (j = 0; j < N; j++) {
                if (j == i) {
                    continue;
                }
                else {
                    tempr = distance(r[i], r[j]); // Same as line 50 - 54
                    tempf = force(tempr);
                    for (k = 0; k < 3; k++) {
                        f[i][k] += tempf / tempr * (r[i][k] - r[j][k]);
                    }
                    U[t] += potential(tempr); // Collecting potential energy
                }
            }
        }
        for (i = 0; i < N; i++) {
            for (k = 0; k < 3; k++) {
                v[i][k] = verletv2(tempv[i][k], f[i][k], m[i], ETA); // verlet loop, calculate the new velocity of (t + dlt)
                M[t][k] += v[i][k]; // Collecting monenta vectors
            }
            K[t] += kinetic(v[i]);

        }
        U[t] = U[t] / 2; // For double counting, (U_ij=U_ji)
        E[t] = K[t] + U[t];
        energy_out << t*dlt << ' ' << U[t] << ' ' << K[t] << ' ' <<  E[t] << endl;
        momenta_out << M[t][0] << ' ' << M[t][1] << ' ' << M[t][2] << endl;
    }
}

// Given two vectors, calculate the distance scalar between the two given atoms
double distance(double r1[3], double r2[3]) {
    double d;
    d = sqrt((r1[0] - r2[0]) * (r1[0] - r2[0]) +
             (r1[1] - r2[1]) * (r1[1] - r2[1]) +
             (r1[2] - r2[2]) * (r1[2] - r2[2]));
    return d;
}
// Given distance between atoms, calculate the potential energy
double potential(double r) {
    double u;
    u = 4 * (1 / pow(r, 12) - 1 / pow(r, 6));
    return u;
}
// Given distance between atoms, calculate the force scalar
double force(double r) {
    double f;
    f = - 4 * (-12 / pow(r, 13) + 6 / pow(r, 7));
    return f;
}
// Given velovity vector of an atom, calculate its kinetic energy
double kinetic(double v[3]) {
    double k;
    int i;
    k = 0;
    for (i = 0;  i < 3; i++) {
        k += 0.5 * v[i] * v[i];
    }
    return k;
}
// Verlet loop for velocity at (t + dlt / 2)
double verletv1(double v, double f, double m, double eta) {
    double vdlt;
    vdlt = v + (f / m - eta * v) * dlt / 2;
    return vdlt;
}
double verletv2(double v, double f, double m, double eta) {
    double vdlt;
    vdlt = (v + f * dlt / (2 * m)) / (1 + eta * dlt / 2);
    return vdlt;
}