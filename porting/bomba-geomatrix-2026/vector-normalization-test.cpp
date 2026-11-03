#include "ps2/vu_ops.hpp"
#include <bit>
#include <random>
#include <cstdio>
int main(){std::mt19937 r(42);for(int n=0;n<100000;n++){ps2::vuops::v4u a={r(),r(),r(),r()};auto fixed=ps2::vuops::vfix(a);for(int j=0;j<4;j++){auto scalar=std::bit_cast<unsigned>(ps2::vuops::fin(a[j]));if(scalar!=fixed[j]){std::printf("mismatch %x %x %x\n",a[j],fixed[j],scalar);return 1;}}}std::puts("400000 vector normalization comparisons passed");}
