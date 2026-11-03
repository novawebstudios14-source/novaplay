#include "recomp/elf.hpp"
#include <cassert>
#include <cstdio>
int main() {
    auto image=recomp::Image::raw(0x900000,std::vector<std::uint8_t>(256,0x12),{64,128});
    assert(!image.executable(0x90003c));
    assert(image.executable(0x900040));
    assert(image.executable(0x90007c));
    assert(!image.executable(0x900080));
    assert(image.word(0x9000fc).value()==0x12121212);
    assert(image.text().first==0x900040 && image.text().second==0x900080);
    puts("Raw image absolute text bounds and readable non-code data passed");
}
