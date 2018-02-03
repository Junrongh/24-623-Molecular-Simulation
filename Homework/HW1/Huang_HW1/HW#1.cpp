#include <iostream>
#include <fstream>
#include <iomanip>
#include <math.h>
#include <time.h>
using namespace std;


int polynomialInt(int i);
double polynomialDouble(double i);


ifstream data_in("input.txt");
ofstream data_out("output.txt");


int main()
{
    int i, j, k;
    const int upper = 11;
    int numbers[upper];
    bool pr;
    int polInt;
    double polDouble;

    int n, divisor, remainder;
    char prime[200];

    // read in data from file "input.txt"
    for (i = 0; i < upper; i++) data_in >> numbers[i];

    // determin if the number is a prime
    for (i = 0; i < upper; i++){
        sprintf(prime, " is a prime");
        if (numbers[i] <= 1)
            sprintf(prime, " Error: prime number has to be natural number that larger than 1");
        else if (numbers[i] == 2)
            sprintf(prime, " is prime");
        else
        {
            n = numbers[i];
            divisor = 2;

            // loop from 2 to input number to determine whether it is prime or not
            while (divisor < n) {
                remainder = numbers[i] % divisor;
                if (remainder == 0){
                    sprintf(prime, " is not a prime");
                    break;
                }
                divisor = divisor + 1;
            }
        }
        // calculate the polynomial with int or double input & output
        polInt = polynomialInt(numbers[i]);
        polDouble = polynomialDouble(numbers[i]);

        // output data into All integers out.txt
        data_out << "The number " << numbers[i] << ":"  << prime << endl;
        data_out << "It returns a value of " << polInt << " when inserted into the function polynomialInt.\n" << endl;
        data_out << "The number " << numbers[i] << ":"  << prime << endl;
        data_out << "It returns a value of " << polDouble << " when inserted into the function polynomialDouble.\n" << endl;
    }
}


int polynomialInt(int i) {
    int f, pow2, pow4, pow6;
    pow2 = i * i;
    pow4 = pow2 * pow2;
    pow6 = pow4 * pow2;
    f = 2 * pow6 - 3 * pow4 + 5 * pow2 - 7;
    return f;
}

double polynomialDouble(double i) {
    double f, pow2, pow4, pow6;
    pow2 = i * i;
    pow4 = pow2 * pow2;
    pow6 = pow4 * pow2;
    f = 2 * pow6 - 3 * pow4 + 5 * pow2 - 7;
    return f;
}
