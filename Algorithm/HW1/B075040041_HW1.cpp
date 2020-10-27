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
    int tempi, tempx, tempy;                            //variables for input file
    ifstream input("readfile.txt");                     //open file
    int i, j, cnt = 0;                                  //cnt for number of data

    while (input >> tempi >> tempx >> tempy) {          //input data
        cnt++;                                          //save data
        datax[tempi - 1] = tempx;
        datay[tempi - 1] = tempy;
    }

    int path[cnt];                                      //array to store trip order
    for (i = 0; i < cnt; i++)
        path[i] = i;
    float minpath = MAXFLOAT;                           //initialize
    float temp;                                         //store trip distance
    int minpath_order[cnt];                             //store min trip order
    clock_t start=clock();                              //timer
    do {
        temp = 0;                                       //initialize trip distance
        for (i = 0; i < cnt - 1; i++)                   //calculate trip distance
            temp += distance(path[i],path[i + 1]);
        temp+=distance(path[cnt-1],path[0]);
        if (temp < minpath) {                           //if trip is shorter
            minpath = temp;                             //store min trip
            for (i = 0; i < cnt; i++)
                minpath_order[i] = path[i];
        }

    } while (next_permutation(path + 1, path + cnt));   //loop next permutation

    clock_t end=clock();
    double elapsed=double(end-start)/CLOCKS_PER_SEC;
    cout<<"Best Vist Order:";                           //output
    for (i = 0; i < cnt; i++)
        cout << minpath_order[i]+1 << " ";
    
    cout << endl<<"Best Distance:"<<minpath<<endl;
    cout << "Execution Time:" <<elapsed<<endl;

    ofstream output("result.txt");                      //output for GNUplot
    for (i=0;i<cnt;i++)
        output<<datax[minpath_order[i]]<<" "<<datay[minpath_order[i]]<<endl;
    
    output<<datax[minpath_order[0]]<<" "<<datay[minpath_order[0]]<<endl;
    
    system("");
}

float distance(int x, int y) {                          //calculate distance between two points
    return sqrt(pow((datax[x] - datax[y]), 2) + pow((datay[x] - datay[y]), 2));
}
