/*
file1.seekg(1234,ios::cur);        // 把檔案讀取指標從目前位置向後移1234個字元
file2.seekp(1234,ios::beg);       // 把檔案的輸出指標從開頭向後移1234個字元 
*/
#include "mytar.h"
mytar::mytar(const char *file)
{
    blocksize = 512;
    inputfile.open(file, ifstream::in | ifstream::binary);

    if (!inputfile.is_open())
    {
        cout << "Open file failed" << endl;
        exit(0);
    }
}
void mytar::readBlock()
{
    struct TarHeader tempHeader;
    inputfile.read(tempHeader.filename, 100);
    inputfile.read(tempHeader.filemode, 8);
    inputfile.read(tempHeader.userid, 8);
    inputfile.read(tempHeader.groupid, 8);
    inputfile.read(tempHeader.filesize, 12);
    inputfile.read(tempHeader.mtime, 12);
    inputfile.read(tempHeader.checksum, 8);
    inputfile.read(&tempHeader.type, 1);
    inputfile.read(tempHeader.lname, 100);
    inputfile.read(tempHeader.USTAR_id, 6);
    inputfile.read(tempHeader.USTAR_ver, 2);
    inputfile.read(tempHeader.username, 32);
    inputfile.read(tempHeader.groupname, 32);
    inputfile.read(tempHeader.devmajor, 8);
    inputfile.read(tempHeader.devminor, 8);
    inputfile.read(tempHeader.prefix, 155);
    inputfile.read(tempHeader.pad, 12);

    tarVector.push_back(tempHeader);
}

int mytar::startRead()
{
    int i, sizecnt = 0, jumpblock;
    readBlock();
    //cout<<"Name:"<<tarVector[tarVector.size()-1].filesize<<endl;
    for (i = 0; i < 11; i++){
        sizecnt += (int(tarVector[tarVector.size() - 1].filesize[i]) - 48) * pow(8, 10 - i);
    }
    jumpblock = sizecnt / 512 + 1;
    sizecnt = 0;
    while (inputfile.seekg(512 * jumpblock, inputfile.cur)){
        readBlock();
        for (i = 0; i < 11; i++){
            sizecnt += (int(tarVector[tarVector.size() - 1].filesize[i]) - 48) * pow(8, 10 - i);
        }
        jumpblock = sizecnt / 512 + 1;
        sizecnt = 0;
    }
    cout<<"Name:"<<tarVector[tarVector.size()-2].filename<<endl;
    cout<<"done with "<<tarVector.size()<<"items\n";
    return 1;
}

void printfile(){

}