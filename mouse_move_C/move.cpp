#include "move.h"

//     # 1  100 -> 120
//     # 2  200 -> 245
//     # 3  300 -> 385
//     # 100 - 184
//     # 200 - 370

DLL_EXPORT void move_relpix(int x, int y)
{
    tagMOUSEINPUT mi;
    mi.dx = x;
    mi.dy = y;
    mi.mouseData = 0;
    mi.dwFlags = MOUSEEVENTF_MOVE;
    mi.time = 0;
    mi.dwExtraInfo = 0;
    tagINPUT input;
    input.type = INPUT_MOUSE;
    input.mi = mi;
    SendInput(1, &input, sizeof(INPUT));
}

DLL_EXPORT void move_gamepix(int x, int y)
{
    float alpha = 0.54348;
    int x_rel = (int)(x * alpha);
    int y_rel = (int)(y * alpha);
    move_relpix(x_rel, y_rel);
}

DLL_EXPORT void move_smooth(int x, int y)
{
    int n = 5;
    int x_rel = x / n;
    int y_rel = y / n;
    for (int i = 0; i < n; i++)
    {        
        move_gamepix(x_rel, y_rel);
        Sleep(10);
    }
}

// int main(int argc, char *argv[])
// {
//     Sleep(5000);
//     move_gamepix(100, 0);
//     Sleep(2000);
//     move_gamepix(-100, 0);
//     return 0;
// }