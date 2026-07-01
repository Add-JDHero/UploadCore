cmake_minimum_required(VERSION 3.10.0)
project(UploadCore VERSION 0.1.0 LANGUAGES C CXX)

find_package(
    userver
    COMPONENTS core #
    QUIET
)

add_executable(UploadCore 
    src/main.cpp
)

target_include_directories(UploadCore PRIVATE
    include
)

target_link_libraries(UploadCore PRIVATE
    userver::core
)



