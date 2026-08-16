#----------------------------------------------------------------
# Generated CMake target import file.
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "yaets::yaets" for configuration ""
set_property(TARGET yaets::yaets APPEND PROPERTY IMPORTED_CONFIGURATIONS NOCONFIG)
set_target_properties(yaets::yaets PROPERTIES
  IMPORTED_LOCATION_NOCONFIG "${_IMPORT_PREFIX}/lib/libyaets.so"
  IMPORTED_SONAME_NOCONFIG "libyaets.so"
  )

list(APPEND _cmake_import_check_targets yaets::yaets )
list(APPEND _cmake_import_check_files_for_yaets::yaets "${_IMPORT_PREFIX}/lib/libyaets.so" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
