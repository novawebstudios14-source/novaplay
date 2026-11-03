// Include the raster translation unit to exercise its private interpolation.
#include "runtime/src/gs/raster.cpp"
#include <cstdio>
int main() {
    using namespace ps2::gs::raster;
    Attr a{128,128,128,128,0,0,1,128,65535};
    unsigned failures=0;
    for (int y=0;y<448;++y) for (int x=0;x<512;++x) {
        float wa=float(x)/512.0f, wb=float(y)/448.0f;
        if (wa+wb>1) continue;
        float wc=1.0f-wa-wb;
        Attr r=lerp3(a,a,a,wa,wb,wc);
        if (r.z!=a.z || r.a!=a.a || r.q!=a.q) ++failures;
    }
    if(failures) { std::fprintf(stderr,"constant attributes drifted in %u samples\n",failures); return 1; }
    Attr b=a,c=a; b.z=32768;c.z=0;
    auto r=lerp3(a,b,c,0.25f,0.5f,0.25f);
    if(r.z!=32767.75) return 2;
    puts("Raster constant depth/alpha and varying depth interpolation passed");
}
