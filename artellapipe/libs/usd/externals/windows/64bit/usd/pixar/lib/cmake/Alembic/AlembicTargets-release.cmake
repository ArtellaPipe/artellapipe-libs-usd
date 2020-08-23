#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "Alembic::Alembic" for configuration "Release"
set_property(TARGET Alembic::Alembic APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(Alembic::Alembic PROPERTIES
  IMPORTED_IMPLIB_RELEASE "${_IMPORT_PREFIX}/lib/Alembic.lib"
  IMPORTED_LINK_INTERFACE_LIBRARIES_RELEASE "D:/dev/artellapipe/artellapipe-libs-usd/usd/build/USD/lib/Imath-2_2.lib;D:/dev/artellapipe/artellapipe-libs-usd/usd/build/USD/lib/IlmThread-2_2.lib;D:/dev/artellapipe/artellapipe-libs-usd/usd/build/USD/lib/Iex-2_2.lib;D:/dev/artellapipe/artellapipe-libs-usd/usd/build/USD/lib/IexMath-2_2.lib;D:/dev/artellapipe/artellapipe-libs-usd/usd/build/USD/lib/Half.lib"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/Alembic.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS Alembic::Alembic )
list(APPEND _IMPORT_CHECK_FILES_FOR_Alembic::Alembic "${_IMPORT_PREFIX}/lib/Alembic.lib" "${_IMPORT_PREFIX}/lib/Alembic.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
