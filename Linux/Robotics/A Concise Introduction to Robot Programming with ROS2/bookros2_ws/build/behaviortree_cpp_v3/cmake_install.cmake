# Install script for directory: /home/edmund-munene/Documents/Programming-language-basics/Linux/Robotics/AConciseIntroductiontoRobotProgrammingwithROS2/bookros2_ws/src/ThirdParty/BehaviorTree.CPP

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/edmund-munene/Documents/Programming-language-basics/Linux/Robotics/AConciseIntroductiontoRobotProgrammingwithROS2/bookros2_ws/install/behaviortree_cpp_v3")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

# Set default install directory permissions.
if(NOT DEFINED CMAKE_OBJDUMP)
  set(CMAKE_OBJDUMP "/usr/bin/objdump")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  include("/home/edmund-munene/Documents/Programming-language-basics/Linux/Robotics/AConciseIntroductiontoRobotProgrammingwithROS2/bookros2_ws/build/behaviortree_cpp_v3/ament_cmake_symlink_install/ament_cmake_symlink_install.cmake")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/behaviortree_cpp_v3/cmake/behaviortree_cpp_v3TargetsExport.cmake")
    file(DIFFERENT _cmake_export_file_changed FILES
         "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/behaviortree_cpp_v3/cmake/behaviortree_cpp_v3TargetsExport.cmake"
         "/home/edmund-munene/Documents/Programming-language-basics/Linux/Robotics/AConciseIntroductiontoRobotProgrammingwithROS2/bookros2_ws/build/behaviortree_cpp_v3/CMakeFiles/Export/9d80895784f3b2b7bded7d2b18b89a67/behaviortree_cpp_v3TargetsExport.cmake")
    if(_cmake_export_file_changed)
      file(GLOB _cmake_old_config_files "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/behaviortree_cpp_v3/cmake/behaviortree_cpp_v3TargetsExport-*.cmake")
      if(_cmake_old_config_files)
        string(REPLACE ";" ", " _cmake_old_config_files_text "${_cmake_old_config_files}")
        message(STATUS "Old export file \"$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/behaviortree_cpp_v3/cmake/behaviortree_cpp_v3TargetsExport.cmake\" will be replaced.  Removing files [${_cmake_old_config_files_text}].")
        unset(_cmake_old_config_files_text)
        file(REMOVE ${_cmake_old_config_files})
      endif()
      unset(_cmake_old_config_files)
    endif()
    unset(_cmake_export_file_changed)
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/behaviortree_cpp_v3/cmake" TYPE FILE FILES "/home/edmund-munene/Documents/Programming-language-basics/Linux/Robotics/AConciseIntroductiontoRobotProgrammingwithROS2/bookros2_ws/build/behaviortree_cpp_v3/CMakeFiles/Export/9d80895784f3b2b7bded7d2b18b89a67/behaviortree_cpp_v3TargetsExport.cmake")
  if(CMAKE_INSTALL_CONFIG_NAME MATCHES "^()$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/behaviortree_cpp_v3/cmake" TYPE FILE FILES "/home/edmund-munene/Documents/Programming-language-basics/Linux/Robotics/AConciseIntroductiontoRobotProgrammingwithROS2/bookros2_ws/build/behaviortree_cpp_v3/CMakeFiles/Export/9d80895784f3b2b7bded7d2b18b89a67/behaviortree_cpp_v3TargetsExport-noconfig.cmake")
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/edmund-munene/Documents/Programming-language-basics/Linux/Robotics/AConciseIntroductiontoRobotProgrammingwithROS2/bookros2_ws/src/ThirdParty/BehaviorTree.CPP/include/" FILES_MATCHING REGEX "/[^/]*\\.h[^/]*$")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libbehaviortree_cpp_v3.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libbehaviortree_cpp_v3.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libbehaviortree_cpp_v3.so"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/home/edmund-munene/Documents/Programming-language-basics/Linux/Robotics/AConciseIntroductiontoRobotProgrammingwithROS2/bookros2_ws/build/behaviortree_cpp_v3/libbehaviortree_cpp_v3.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libbehaviortree_cpp_v3.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libbehaviortree_cpp_v3.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libbehaviortree_cpp_v3.so"
         OLD_RPATH "/opt/ros/jazzy/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libbehaviortree_cpp_v3.so")
    endif()
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/cmake/behaviortree_cpp_v3/behaviortree_cpp_v3Targets.cmake")
    file(DIFFERENT _cmake_export_file_changed FILES
         "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/cmake/behaviortree_cpp_v3/behaviortree_cpp_v3Targets.cmake"
         "/home/edmund-munene/Documents/Programming-language-basics/Linux/Robotics/AConciseIntroductiontoRobotProgrammingwithROS2/bookros2_ws/build/behaviortree_cpp_v3/CMakeFiles/Export/f632a83f59300ac560526cf113f6094b/behaviortree_cpp_v3Targets.cmake")
    if(_cmake_export_file_changed)
      file(GLOB _cmake_old_config_files "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/cmake/behaviortree_cpp_v3/behaviortree_cpp_v3Targets-*.cmake")
      if(_cmake_old_config_files)
        string(REPLACE ";" ", " _cmake_old_config_files_text "${_cmake_old_config_files}")
        message(STATUS "Old export file \"$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/cmake/behaviortree_cpp_v3/behaviortree_cpp_v3Targets.cmake\" will be replaced.  Removing files [${_cmake_old_config_files_text}].")
        unset(_cmake_old_config_files_text)
        file(REMOVE ${_cmake_old_config_files})
      endif()
      unset(_cmake_old_config_files)
    endif()
    unset(_cmake_export_file_changed)
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/behaviortree_cpp_v3" TYPE FILE FILES "/home/edmund-munene/Documents/Programming-language-basics/Linux/Robotics/AConciseIntroductiontoRobotProgrammingwithROS2/bookros2_ws/build/behaviortree_cpp_v3/CMakeFiles/Export/f632a83f59300ac560526cf113f6094b/behaviortree_cpp_v3Targets.cmake")
  if(CMAKE_INSTALL_CONFIG_NAME MATCHES "^()$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/behaviortree_cpp_v3" TYPE FILE FILES "/home/edmund-munene/Documents/Programming-language-basics/Linux/Robotics/AConciseIntroductiontoRobotProgrammingwithROS2/bookros2_ws/build/behaviortree_cpp_v3/CMakeFiles/Export/f632a83f59300ac560526cf113f6094b/behaviortree_cpp_v3Targets-noconfig.cmake")
  endif()
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("/home/edmund-munene/Documents/Programming-language-basics/Linux/Robotics/AConciseIntroductiontoRobotProgrammingwithROS2/bookros2_ws/build/behaviortree_cpp_v3/sample_nodes/cmake_install.cmake")
  include("/home/edmund-munene/Documents/Programming-language-basics/Linux/Robotics/AConciseIntroductiontoRobotProgrammingwithROS2/bookros2_ws/build/behaviortree_cpp_v3/tests/cmake_install.cmake")
  include("/home/edmund-munene/Documents/Programming-language-basics/Linux/Robotics/AConciseIntroductiontoRobotProgrammingwithROS2/bookros2_ws/build/behaviortree_cpp_v3/tools/cmake_install.cmake")
  include("/home/edmund-munene/Documents/Programming-language-basics/Linux/Robotics/AConciseIntroductiontoRobotProgrammingwithROS2/bookros2_ws/build/behaviortree_cpp_v3/examples/cmake_install.cmake")

endif()

if(CMAKE_INSTALL_COMPONENT)
  set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
file(WRITE "/home/edmund-munene/Documents/Programming-language-basics/Linux/Robotics/AConciseIntroductiontoRobotProgrammingwithROS2/bookros2_ws/build/behaviortree_cpp_v3/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
