cmake_minimum_required(VERSION 3.8 FATAL_ERROR)
project( videostab )
find_package( OpenCV REQUIRED )
include_directories( ${OpenCV_INCLUDE_DIRS} )
add_executable(videostab videostab.cpp)
add_executable(videostabKalman videostabKalman.cpp)
target_link_libraries( videostab  ${OpenCV_LIBS} ) #mod
target_link_libraries( videostabKalman  ${OpenCV_LIBS} ) #mod
set_target_properties(videostab PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}")
set_target_properties(videostabKalman PROPERTIES RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}")

