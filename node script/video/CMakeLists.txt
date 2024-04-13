#cmake_minimum_required(VERSION 3.15)
#project( videostab )
#find_package( OpenCV REQUIRED )
#include_directories( ${OpenCV_INCLUDE_DIRS} )

#add_executable( videostab videostab.cpp )
#add_executable( videostabKalman videostabKalman.cpp )
#target_link_libraries( videostab  ${OpenCV_LIBS} )
#target_link_libraries( videostabKalman  ${OpenCV_LIBS} )

#target_link_libraries(videostab ${Python3_LIBRARIES})


#-----------------------


cmake_minimum_required(VERSION 3.8 FATAL_ERROR)
project(matplotlib_cpp LANGUAGES CXX)

include(GNUInstallDirs)
set(PACKAGE_NAME matplotlib_cpp)
set(INSTALL_CONFIGDIR ${CMAKE_INSTALL_LIBDIR}/${PACKAGE_NAME}/cmake)


# Library target
add_library(matplotlib_cpp INTERFACE)
target_include_directories(matplotlib_cpp
  INTERFACE
    $<BUILD_INTERFACE:${PROJECT_SOURCE_DIR}/examples>
    $<INSTALL_INTERFACE:include>
)
target_compile_features(matplotlib_cpp INTERFACE
  cxx_std_11
)
# TODO: Use `Development.Embed` component when requiring cmake >= 3.18
find_package(Python3 COMPONENTS Interpreter Development REQUIRED)
target_link_libraries(matplotlib_cpp INTERFACE
  Python3::Python
  Python3::Module
)
find_package(Python3 COMPONENTS NumPy)
if(Python3_NumPy_FOUND)
  target_link_libraries(matplotlib_cpp INTERFACE
    Python3::NumPy
  )
else()
  target_compile_definitions(matplotlib_cpp INTERFACE WITHOUT_NUMPY)
endif()
install(
  TARGETS matplotlib_cpp
  EXPORT install_targets
)

find_package( OpenCV REQUIRED )
include_directories( ${OpenCV_INCLUDE_DIRS})


# Examples
add_executable(videostab videostab.cpp)
add_executable(videostabKalman videostabKalman.cpp)
target_link_libraries(videostab  matplotlib_cpp)
target_link_libraries(videostabKalman  matplotlib_cpp)
target_link_libraries( videostab  ${OpenCV_LIBS} ) #mod
target_link_libraries( videostabKalman  ${OpenCV_LIBS} ) #mod
set_target_properties(videostab PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}")
set_target_properties(videostabKalman PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}")

