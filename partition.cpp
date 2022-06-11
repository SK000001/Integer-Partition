#include <iostream>
#include <vector>
#include <gmpxx.h>
using namespace std;

mpz_class prt(vector<mpz_class> p, vector<int> x, vector<int> y) {
    int a = -1, sub = 0, xDiff = 0;
    int b = 1, count = 1, yDiff = 1;
    mpz_class val = 0;


    while (true) {
        a++;
        int aflg = 0, bflg = 0;

        if (a == 4) {
            a = -1;
            continue;
        }

        int count = p.size() - sub - 1;
        if (count < 0) {
            break;
        }

        if (a < 2) {
            val += p[count];
            aflg = 1;
        }

        if (b % 2 == 0) {
            sub += y.at(yDiff);
            yDiff++;
            bflg = 1;
        }


        if (aflg == 0) {
            val -= p[count];
        }

        if (bflg == 0) {
            sub += x.at(xDiff);
            xDiff++;
        }
        b++;     
    }

    return val;
}

int main() {
    int n;
    mpz_class val;
    cout << "Enter a num: ";
    cin >> n;
    vector<mpz_class> p {1, 1};
    vector<int> x = {1, 2};
    vector<int> y = {1, 3};

    while (p.size() <= n) {
        try {
            val = prt(p, x, y);
        } catch (out_of_range) {
            x.push_back(x.back()+1);
            y.push_back(y.back()+2);
            val = prt(p, x, y);
        }

        p.push_back(val);
    }

    cout << "p(" << n << "): " << p.back();

    return 0;
}
