#include "mytar.h"
mytar::mytar(const char *file)
{
    inputfile.open(file, ifstream::in | ifstream::binary);

    if (!inputfile.is_open())
    {
        cout <<"mytar: "<<file<< ": Cannot open : No such file or directory" << endl;
        cout <<"mytar: Error is not recoverable: exiting now"<<endl;
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
        jumpblock = ceil(sizecnt / 512.0)  ;
        sizecnt = 0;
    }
    //cout<<"Name:"<<tarVector[0].filemode<<endl;
    //cout<<"done with "<<tarVector.size()<<"items\n";
    return 1;
}

void mytar::printfile(){
    int mode;
    bool modeselect[3];
    char dictionary[3]={'r','w','x'};
    for (int i=0; i< tarVector.size()-1;i++){
        //mode
        if (tarVector[i].type=='5')
            cout<<'d';
        else
            cout<<'-';
        
        for(int j=4; j<7;j++){
            //init
            for (int k=0;k<3;k++)
                modeselect[k]=0;

            mode=int(tarVector[i].filemode[j])-'0';
            if(mode>=4){
                modeselect[0]=1;
                mode-=4;
            }
            if(mode>=2){
                modeselect[1]=1;
                mode-=2;
            }
            if(mode){
                modeselect[2]=1;
            }
            //output
            for (int k=0;k<3;k++)
                if(modeselect[k]){
                    cout<<dictionary[k];
                }
                else{
                    cout<<'-';
                }
                
        }

        // name/group
        cout<<" "<<tarVector[i].username<<"/"<<tarVector[i].groupname;
        // size
        int sizecnt=0;
        for (int j = 0; j < 11; j++){
            sizecnt += (int(tarVector[i].filesize[j]) - 48) * pow(8, 10 - j);
        }
        cout<<setw(6)<<sizecnt<<" ";
        //time
        int timecnt=0;
        for (int j = 0; j < 11; j++){
            timecnt += (int(tarVector[i].mtime[j]) - 48) * pow(8, 10 - j);
        }
        time_t temp=timecnt+28800;
        tm *t=gmtime(&temp);
        stringstream ss;
        ss<<put_time(t,"%Y-%m-%d %H:%M");
        string output =ss.str();
        cout<<output<<" ";

        //filename
        cout<<tarVector[i].filename<<" ";
        //done
        cout<<endl;
    }
}