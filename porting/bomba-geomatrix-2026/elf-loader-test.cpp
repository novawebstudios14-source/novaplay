#include "ps2/system.hpp"
#include "ps2/memory.hpp"
#include <vector>
#include <fstream>
#include <cstring>
#include <cstdio>
static void u32(std::vector<unsigned char>& b,int o,unsigned v){std::memcpy(b.data()+o,&v,4);}
static void u16(std::vector<unsigned char>& b,int o,unsigned short v){std::memcpy(b.data()+o,&v,2);}
int main(int argc,char** argv){
 if(argc!=2){std::fprintf(stderr,"usage: elf-loader-test <temporary ELF path>\n");return 2;}
 std::vector<unsigned char>b(0x201);std::memcpy(b.data(),"\177ELF",4);u32(b,24,0x100000);u32(b,28,52);u16(b,42,32);u16(b,44,3);
 auto ph=[&](int i,unsigned off,unsigned addr,unsigned size,unsigned mem){int o=52+i*32;u32(b,o,1);u32(b,o+4,off);u32(b,o+8,addr);u32(b,o+16,size);u32(b,o+20,mem);};
 ph(0,0x200,0x100000,1,4);b[0x200]=0xa5;ph(1,0x300,0x101000,0,16);ph(2,0x300,0x3000000,0,0x800);
 auto load=[&]{std::ofstream f(argv[1],std::ios::binary);f.write((char*)b.data(),b.size());f.close();unsigned e;return ps2::load_elf(argv[1],e);};
 if(!load()||ps2::g_ram[0x100000]!=0xa5)return 1;
 ph(2,0x200,0x3000000,1,0x800);if(load())return 3;
 ph(2,0x300,0x101000,1,0x800);if(load())return 4;
 std::puts("ELF loader checks passed: empty reservations accepted; invalid payloads rejected");
}
