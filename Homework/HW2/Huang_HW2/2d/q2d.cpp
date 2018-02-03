#include <iostream>
#include <fstream>
#include <iomanip>
#include <math.h>
#include <time.h>
using namespace std;

ofstream x1_out("x1_2_out.txt");
ofstream x2_out("x2_2_out.txt");
ofstream v1_out("v1_out.txt");
ofstream v2_out("v2_out.txt");

int main() {
    int i;
    double E, v1, v2, x1, x2, tempv, dlt = 0.001;
    E = 2;
    v1 = sqrt(2 * E);
    v2 = -sqrt(2 * E);
    x1 = 1;
    x2 = -1;

    for (i = 0; i < 20000; i++) {
        // Store current position and velocity
        x1_out << x1 << endl;
        x2_out << x2 << endl;
        v1_out << v1 << endl;
        v2_out << v2 << endl;

        // Using Velocity Verlet method to calculate the next X, V

        tempv = v1 + (-4 * x1 * x1 * x1 + 4 * x1) / 2 * dlt;
        x1 = x1 + tempv * dlt;
        v1 = tempv + (-4 * x1 * x1 * x1 + 4 * x1) / 2 * dlt;

        tempv = v2 + (-4 * x2 * x2 * x2 + 4 * x2) / 2 * dlt;
        x2 = x2 + tempv * dlt;
        v2 = tempv + (-4 * x2 * x2 * x2 + 4 * x2) / 2 * dlt;

    }
}
