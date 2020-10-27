#include "mytar.h"
using namespace std;

int main(int argc , char **argv){
    mytar tar(argv[1]);
    tar.startRead();
    tar.printfile();
}