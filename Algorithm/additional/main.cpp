#include <iostream>
#include <cstdio>
#include <ctime>
#include <fstream>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;
void sa(vector< vector<float> > distance,int size){
    float temperature=50000,endTemp=0.00000001,rate=0.98,random0to1;
    vector<int> bestPath;
    vector<int> path;
    double currentDistance=0,bestDistance,deltaT;
    int swapA,swapB,i;
    
    for (i=0;i<size;i++){
        path.push_back(i);
    }
    //cnt distance
    for (i=0;i<size;i++){
        currentDistance+=distance[path[i]][path[i+1]];
    }
    currentDistance+=distance[path[size-1]][path[0]];
    bestPath=path;
    bestDistance=currentDistance;
    //start simulateing
    for (;temperature>endTemp;temperature*=rate){
        
        //times for each temperature
        for (int j=0;j<1000;j++){
        
            //choose 2 points to swap
            do {
                swapA=rand()%size;
                swapB=rand()%size;
            } while (swapA==swapB);
            swap(path[swapA],path[swapB]);
            //cnt distance
            currentDistance=0;
            for (i=0;i<size;i++){
                currentDistance+=distance[path[i]][path[i+1]];
            }
            currentDistance+=distance[path[size-1]][path[0]];
            //cal delta T
            deltaT=bestDistance-currentDistance;
            if (deltaT>0){
                bestDistance=currentDistance;
                bestPath=path;
            }
            else{
                random0to1=(float)rand()/RAND_MAX;
                if(exp(deltaT/temperature)>random0to1){
                    bestDistance=currentDistance;
                    bestPath=path;
                }
            }
        
        }
            
    }
    //output result:
    cout<<"SOLU: ";
    for (i=0;i<size;i++){
        cout<<bestPath[i]+1<<" ";
    }
    cout<<endl<<"Distance: "<<bestDistance<<endl;
}

int main(int argc,char **argv){
    srand(time(NULL));
    //read file
    ifstream input(argv[1]);
    vector< vector<int> > data; //stores station info
    int stationName,x,y;    //input file form
    while(input>>stationName){
        vector<int> tempXY;
        input>>x>>y;
        tempXY.push_back(x);
        tempXY.push_back(y);
        data.push_back(tempXY);
    }
    //check file
    /*
    for (int i=0;i<data.size();i++){
        cout<<data[i][0]<<" "<<data[i][1]<<endl;
    }
    */
    vector< vector<float> > distance;   //distance array
    int i,j;
    for (i=0;i<data.size();i++){
        vector<float> temp;
        for (j=0;j<data.size();j++){
            temp.push_back(0);
        }
        distance.push_back(temp);
    }
    
    for (i=0;i<data.size();i++){
        for (j=0;j<data.size();j++){
            float x1=data[i][0],
                  y1=data[i][1],
                  x2=data[j][0],
                  y2=data[j][1];
            distance[i][j]=sqrt(pow((x1-x2),2)+pow((y1-y2),2));
        }
    }
    sa(distance,data.size());
}
