#include <algorithm>
#include <cmath>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <ctime>
using namespace std;
float distance(int x, int y);
int datax[100] = {0};
int datay[100] = {0};

int main() {
    int tempi, tempx, tempy;
    ifstream input("readfile.txt");
    int i, j, cnt = 0;

    while (input >> tempi >> tempx >> tempy) {
        cnt++;
        datax[tempi - 1] = tempx;
        datay[tempi - 1] = tempy;
    }

    float matrix[cnt][cnt];
    for (i = 0; i < cnt; i++) {
        for (j = 0; j < cnt; j++) {
            matrix[i][j] = distance(i, j);
        }
    }

    // PRINT　MATRIX
    /*for (i=0;i<cnt;i++){
        for (j=0;j<cnt;j++){
            cout<<fixed<<setprecision(3)<<matrix[i][j]<<" ";
        }
        cout<<endl;
    }*/

    int path[cnt];
    for (i = 0; i < cnt; i++) {
        path[i] = i;
    }
    float minpath = MAXFLOAT;
    float temp;
    int minpath_order[cnt];
    clock_t start=clock();
    do {
        temp = 0;
        for (i = 0; i < cnt - 1; i++) {
            temp += matrix[path[i]][path[i + 1]];
            // cout<<temp<<endl;
        }
        temp+=matrix[path[10]][path[0]];
        if (temp < minpath) {
            minpath = temp;
            for (i = 0; i < cnt; i++) {
                minpath_order[i] = path[i];
            }
        }

        /*for (i = 0; i < cnt; i++) {
            cout << path[i] << " ";
        }
        cout << endl;*/

    } while (next_permutation(path + 1, path + cnt));

    clock_t end=clock();
    double elapsed=double(end-start)/CLOCKS_PER_SEC;
    cout<<"Best Vist Order:";
    for (i = 0; i < cnt; i++) {
        cout << minpath_order[i]+1 << " ";
    }
    cout << endl<<"Best Distance:"<<minpath<<endl;
    cout << "Execution Time:" <<elapsed<<endl;

    ofstream output("result.txt");
    for (i=0;i<cnt;i++){
        output<<datax[minpath_order[i]]<<" "<<datay[minpath_order[i]]<<endl;
    }
    output<<datax[minpath_order[0]]<<" "<<datay[minpath_order[0]]<<endl;
}

float distance(int x, int y) {
    return sqrt(pow((datax[x] - datax[y]), 2) + pow((datay[x] - datay[y]), 2));
}