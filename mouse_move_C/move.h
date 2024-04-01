#ifndef __AI_CHEAT_MOVE_H__
#define __AI_CHEAT_MOVE_H__

#include <windows.h>
#include <stdio.h>

#ifndef BUILD_DLL
#define DLL_EXPORT __declspec(dllexport)
#else
#define DLL_EXPORT __declspec(dllimport)
#endif

extern "C" {
    DLL_EXPORT void move_relpix(int x, int y);
    DLL_EXPORT void move_gamepix(int x, int y);
    DLL_EXPORT void move_smooth(int x, int y);
}

#endif // __AI_CHEAT_MOVE_H__