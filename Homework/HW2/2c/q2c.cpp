#include <iostream>
#include <fstream>
#include <iomanip>
#include <math.h>
#include <time.h>
using namespace std;

ofstream x_out("x_out.txt");
ofstream v_out("v_out.txt");

int main(){
    int i;
    double v, x, v2, dlt = 0.001;
    v = sqrt(2);
    x = 0;

    for (i = 0; i < 20000; i++) {
        x_out << x << endl;
        v_out << v << endl;
        v2 = v - x / 2 * dlt;
        x = x + v2 * dlt;
        v = v2 - x / 2 * dlt;
    }
}
