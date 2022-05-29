cmake_minimum_required(VERSION 3.5)

message("test order of Config model")
set(CMAKE_PREFIX_PATH "/usr/local/share/OpenCV")
message("CMAKE_PERFIX_PATH" ${CMAKE_PREFIX_PATH})
#message(STATUS "OpenCV_DIR = ${OpenCV_DIR}")

#经过实验，Config先查找_DIR路径，再查找CMAKE_PREFIX_PATH路径
#找ros中的opencv
# set(OpenCV_DIR "/opt/ros/kinetic/share/OpenCV-3.3.1-dev")#这个去掉之后，找到的就是自己安装的Opencv3.4.7
find_package(OpenCV  REQUIRED)

message(STATUS "CMAKE_MOUDLE_PATH = ${CMAKE_MOUDLE_PATH}")
message(STATUS "CMAKE_ROOT = ${CMAKE_ROOT}")
message(STATUS "OpenCV_DIR = ${OpenCV_DIR}")

message("opencv version is " ${OpenCV_VERSION})

set(CMAKE_BUILD_TYPE "Debug")
set(EXECUTABLE_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/bin)

include_directories(${OpenCV_INCLUDE_DIRS})
message("opencv include dirs is " ${OpenCV_INCLUDE_DIRS})

#add_executable(huidu huidu.cpp)
#target_link_libraries(huidu ${OpenCV_LIBS})

add_executable(cv_FileStorage ./src/cv_FileStorage.cpp)
target_link_libraries(cv_FileStorage ${OpenCV_LIBS})