#include <iostream>
#include <ctime>
using namespace std;
int main()
{
    time_t epch = 013262551156;
    cout<<asctime(gmtime(&epch));
}
