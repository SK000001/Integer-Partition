#include <iostream>
#include <vector>
#include <gmpxx.h>
#include <fstream>
using namespace std;

int initializePXY(fstream & fp, int *hint, vector<mpz_class> *p) {
    if (!fp) {
        cout << "file creation failed!";
        return -1;
    }

    fp.seekg(0);
    int x = fp.peek();
    fp.seekg(0);

    if (x == EOF) {
        fp << hint[0] << ' ' << hint[1] << ' ';
        p->push_back(hint[0]);
        p->push_back(hint[1]);
        return 1;
    }

    char ch;
    string s = "";

    while (1) {
        fp.get(ch);
        if (fp.eof()) { break; }

        if (ch == ' ') { p->push_back(mpz_class(s, 10)); s = ""; continue; }

        s += ch;
    }

    return 1;
}

void prt(vector<mpz_class> *p, vector<mpz_class> *x, vector<mpz_class> *y, fstream & fp) {
    int a = -1, sub = 0, xDiff = 0, aflg;
    int b = 1, count = 1, yDiff = 1, bflg;
    mpz_class val = 0;

    while (true) {
        a++;
        aflg = 0, bflg = 0;

        if (a == 4) {
            a = -1;
            continue;
        }

        count = p->size() - sub - 1;
        if (count < 0) {
            break;
        }

        if (a < 2) {
            val += p->at(count);
            aflg = 1;
        }

        if (b % 2 == 0) {
            sub += y->at(yDiff).get_ui();
            yDiff++;
            bflg = 1;
        }

        if (aflg == 0) {
            val -= p->at(count);
        }

        if (bflg == 0) {
            sub += x->at(xDiff).get_ui();
            xDiff++;
        }
        b++;     
    }

    p->push_back(val);
    fp << p->back() << ' ';
}

int main() {
    int n;
    cout << "Enter a num: ";
    cin >> n;
    int pp[] = {1, 1}, px[] = {1, 2}, py[] = {1, 3};

    fstream fp_p, fp_x, fp_y;
    fp_p.open("p.txt", ios::in | ios::app);
    fp_x.open("x.txt", ios::in | ios::app);
    fp_y.open("y.txt", ios::in | ios::app);

    vector<mpz_class> p; initializePXY(fp_p, pp, &p);
    vector<mpz_class> x; initializePXY(fp_x, px, &x);
    vector<mpz_class> y; initializePXY(fp_y, py, &y);

    while (p.size() <= n) {
        try {
            prt(&p, &x, &y, fp_p);
        } catch (out_of_range) {
            x.push_back(x.back()+1);
            fp_x << x.back() << ' ';
            y.push_back(y.back()+2);
            fp_y << y.back() << ' ';
            prt(&p, &x, &y, fp_p);
        }
    }

    fp_p.close(); fp_x.close(); fp_y.close();

    cout << "p(" << n << "): " << p.at(n);

    return 0;
}
