NOTE
============================================

Following files:

- boost_python27-vc142-mt-x64-1_70.dll
- boost_python28-vc142-mt-x64-1_70.lib
- boost_python-vc140-mt-x64-1_70.dll
- boost_python-vc140-mt-x64-1_70.lib

are copies of:
- boost_python27-vc140-mt-x64-1_70.dll
- boost_python27-vc140-mt-x64-1_70.lib

Build setups for Autodesk Arnold-USD and Luma USD-qt don't manage Boost libraries with the name boost_python27.
Creating the copies was a quick and dirty way of making those libraries to build against USD 20.0.8.