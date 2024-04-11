cmake_minimum_required(VERSION 2.8)
project( videostabKalman )
find_package( OpenCV REQUIRED )
include_directories( ${OpenCV_INCLUDE_DIRS} )
add_executable( videostabKalman videostabKalman.cpp )
target_link_libraries( videostabKalman  ${OpenCV_LIBS} )

