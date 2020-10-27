#include<iostream>
#include<stdio.h>
#include<unistd.h>
using namespace std;

int array[52][52] = {0}, Narray[52][52] = {0},delay_time;

void glider()
{
    array[10][10]=1;
    array[10][11]=1;
    array[10][12]=1;
    array[9][12]=1;
    array[8][11]=1;
    delay_time=300000;
}

void hwss()
{
    array[10][30]=1;
    array[10][31]=1;
    array[10][32]=1;
    array[11][32]=1;
    array[12][31]=1;
    //left
    array[12][35]=1;
    array[12][36]=1;
    array[12][37]=1;
    array[13][37]=1;
    array[14][36]=1;
    //mid
    array[6][38]=1;
    array[6][40]=1;
    array[7][38]=1;
    array[7][39]=1;
    array[8][39]=1;
    //right
    delay_time=300000;
} 

void glider_gun()
{
    array[5][1]=1;
    array[5][2]=1;
    array[6][1]=1;
    array[6][2]=1;
    //left
    array[5][11]=1;
    array[6][11]=1;
    array[7][11]=1;
    array[4][12]=1;
    array[8][12]=1;
    array[3][13]=1;
    array[9][13]=1;
    array[3][14]=1;
    array[9][14]=1;
    array[6][15]=1;
    array[4][16]=1;
    array[8][16]=1;
    array[5][17]=1;
    array[6][17]=1;
    array[7][17]=1;
    array[6][18]=1;
    //left 2
    array[3][21]=1;
    array[4][21]=1;
    array[5][21]=1;
    array[3][22]=1;
    array[4][22]=1;
    array[5][22]=1;
    array[2][23]=1;
    array[6][23]=1;
    array[1][25]=1;
    array[2][25]=1;
    array[6][25]=1;
    array[7][25]=1;
    //right 2
    array[3][35]=1;
    array[3][36]=1;
    array[4][35]=1;
    array[4][36]=1;
    //right
    delay_time=80000;
}

int main() 
{
    int i,j;
    for(i=0 ; i<52 ; i++)
    {
        array[0][i]=-1;
        array[51][i]=-1;
        array[i][0]=-1;
        array[i][51]=-1;
        Narray[0][i]=-1;
        Narray[51][i]=-1;
        Narray[i][0]=-1;
        Narray[i][51]=-1;
    }

    there:
    int op;
    printf("\n1. glider\n2. hwss\n3. glider gun\nPlease enter the mode number:");
    scanf(" %d",&op);
    if(op==1)
        glider();
    else if(op==2)
        hwss();
    else if(op==3)
        glider_gun();
    else
    {
        printf("Error, please enter again!");
        goto there;
    }
    

    while(1)
    {
        system("clear");
        for(i=1 ; i<51 ; i++)
        {
            for(j=1; j<51 ; j++)
                if(array[i][j]==1)
                    printf("● ");
                else
                    printf("  ");
            printf("\n");        
        }
        for(i=1 ; i<51 ; i++)
        {
            for(j=1; j<51 ; j++)
            {
                int count = 0;
                if(array[i][j-1]==1)
                    count++;
                if(array[i][j+1]==1)
                    count++;
                if(array[i-1][j]==1)
                    count++;
                if(array[i-1][j+1]==1)
                    count++;
                if(array[i-1][j-1]==1)
                    count++;
                if(array[i+1][j]==1)
                    count++;
                if(array[i+1][j+1]==1)
                    count++;
                if(array[i+1][j-1]==1)
                    count++;
                
                if((array[i][j]==1) && (count==2 || count==3))
                    Narray[i][j]=1;
                else if((array[i][j]==1) && (count>3 || count<2))
                    Narray[i][j]=0;
                else if((array[i][j]==0) && (count==3))
                    Narray[i][j]=1;
            }
        }
        for(i=1 ; i<51 ; i++)
            for(j=1; j<51 ; j++)
                   array[i][j]=Narray[i][j];
        usleep(delay_time);
    }
}