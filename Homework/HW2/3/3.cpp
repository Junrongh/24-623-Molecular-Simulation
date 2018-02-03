#include <iostream>
#include <fstream>
#include <iomanip>
#include <math.h>
#include <time.h>
using namespace std;

ifstream input("../10.txt");
ofstream energy_out("energy.txt");
ofstream momenta_out("momenta.txt");
ofstream VMD_out("vmd.xyz");

const int N = 10, T = 1000;
const double dlt = 0.002;

double distance(double r1[3], double r2[3]);
double potential(double r);
double force(double r);
double kinetic(double v[3], double m);
double verletv(double v, double f, double m);


int main() {
    int i, j, k, t;
    double m[N]; // Define Mass
    double r[N][3], v[N][3], f[N][3], tempv[N][3];
    double K[T], U[T], E[T], M[T][3]; // Define energy and momenta
    double tempr2, tempu, tempf;

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
                tempr2 = distance(r[i], r[j]); // Calculate the distance between two atoms
                tempf = force(tempr2); // Calculate the force(scalar) between two atoms
                for (k = 0; k < 3; k++) {
                    f[i][k] = f[i][k] + tempf * (r[i][k] - r[j][k]); // Spilt force into each axis
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
        VMD_out << "10 \n";
        VMD_out << "10 Ar LJ Simulization\n";
        for (i = 0; i < N; i++)
        {
            VMD_out << "Ar " << r[i][0] << " "
                    << r[i][1] << " " << r[i][2] << "\n";
        }
        // Loop for every atom, Verlet loop 1, 2 step
        for (i = 0; i < N; i++) {
            for (k = 0; k < 3; k++) {
                tempv[i][k] = v[i][k] + f[i][k] * dlt / (2 * m[i]); // Verlet loop, calculate the velocity of (t + dlt / 2)
                r[i][k] = r[i][k] + tempv[i][k] * dlt; // Verlet loop, calculate the new position of (t + dlt)
            }
        }

        // Loop for every atom, initialize the temp storage of f
        for (i = 0; i < N; i++) {
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
                    tempr2 = distance(r[i], r[j]); // Same as line 50 - 54
                    tempf = force(tempr2);
                    for (k = 0; k < 3; k++) {
                        f[i][k] = f[i][k] + tempf * (r[i][k] - r[j][k]);
                    }
                    U[t] += potential(tempr2); // Collecting potential energy
                }
            }
        }
        for (i = 0; i < N; i++) {
            for (k = 0; k < 3; k++) {
                v[i][k] = tempv[i][k] + f[i][k] * dlt / (2 * m[i]); // verlet loop, calculate the new velocity of (t + dlt)
                M[t][k] = M[t][k] + v[i][k] * m[i]; // Collecting monenta vectors
            }
            K[t] = K[t] + kinetic(v[i], m[i]);

        }
        U[t] = U[t] / 2; // For double counting, (U_ij=U_ji)
        E[t] = K[t] + U[t];
        energy_out << t*dlt << ' ' << U[t] << ' ' << K[t] << ' ' <<  E[t] << endl;
        momenta_out << M[t][0] << ' ' << M[t][1] << ' ' << M[t][2] << endl;
    }
}

// Given two vectors, calculate the distance square scalar between the two given atoms
double distance(double r1[3], double r2[3]) {
    double d = 0;
    int i;
    for (i = 0; i < 3; i++) {
        d = d + (r1[i] - r2[i]) * (r1[i] - r2[i]);
    }
    return d;
}
// Given distance between atoms, calculate the potential energy
double potential(double r) {
    double u;
    double r4, r6;
    r4 = r * r;
    r6 = r4 * r;
    u = 4 * (1 / (r6 * r6) - 1 / r6);
    return u;
}
// Given distance between atoms, calculate the force/distance scalar
// The reason we do this cause in this way we don't need to do the calculation the squareroot
double force(double r) {
    double f;
    double r4, r6;
    r4 = r * r;
    r6 = r4 * r;
    f = - 4 * (-12 / (r6 * r6 * r) + 6 / (r6 * r));
    return f;
}
// Given velovity vector of an atom, calculate its kinetic energy
double kinetic(double v[3], double m) {
    double k;
    int i;
    k = 0;
    for (i = 0;  i < 3; i++) {
        k = k + 0.5 * m * v[i] * v[i];
    }
    return k;
}
// Verlet loop for velocity at (t + dlt / 2)
double verletv(double v, double f, double m) {
    double vdlt;
    vdlt = v + f * dlt / (2 * m);
    return vdlt;
}