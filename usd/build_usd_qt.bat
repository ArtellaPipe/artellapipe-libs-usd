:: USD compiled root
set USD_ROOT=D:\dev\artellapipe\artellapipe-libs-usd\usd\build\USD

:: Dependencies
set TBB_INCLUDE_DIR=%USD_ROOT%/src/tbb2017_20170412oss
set Boost_INCLUDE_DIR=%USD_ROOT%/include/boost-1_70

set BUILD_DIR=D:\dev\artellapipe\artellapipe-libs-usd\usd\build\usd-qt

:: Cmake the Visual Studio solution
cd /D D:\dev\artellapipe\artellapipe-libs-usd\usd\usd-qt
cmake -G "Visual Studio 14 2015 Win64" -DBoost_INCLUDE_DIR="%Boost_INCLUDE_DIR%" -DTBB_ROOT_DIR="%TBB_INCLUDE_DIR%" -DBOOST_LIBRARYDIR=%USD_ROOT%/lib -B %BUILD_DIR% -DCMAKE_INSTALL_PREFIX=%BUILD_DIR%/install

:: Build with Visual Studio
cmake --build %BUILD_DIR% --config Release 

:: Trigger cmake_install.cmake
cd /D %BUILD_DIR% 
cmake -P cmake_install.cmake