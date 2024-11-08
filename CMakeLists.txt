cmake_minimum_required(VERSION 3.15)
project(qumeas)


include(GNUInstallDirs)

# Set C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_FLAGS_RELEASE "-O3")
set(CMAKE_POSITION_INDEPENDENT_CODE ON)
add_compile_options(-fPIC)

# Include directories
include_directories(${CMAKE_SOURCE_DIR}/include)

# Output directories
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/python/qumeas)

# Eigen
find_package(Eigen3 QUIET)
if(NOT TARGET Eigen3::Eigen)
    message(STATUS "Eigen3 not found. Using the version in external/eigen.")
    include_directories(${CMAKE_SOURCE_DIR}/external/eigen)
endif()

# pybind11
find_package(pybind11 QUIET)
if(NOT TARGET pybind11::module)
    message(STATUS "pybind11 not found. Using the version in external/pybind11.")
    add_subdirectory(external/pybind11)
endif()


# Enable OpenMP
find_package(OpenMP)
if(OpenMP_CXX_FOUND)
    message(STATUS "Found OpenMP")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${OpenMP_CXX_FLAGS}")
endif()

# Add subdirectories
add_subdirectory(src/cpp)
add_subdirectory(src/bindings)

# Platform-Specific Adjustments
if (CMAKE_SYSTEM_NAME STREQUAL "Darwin")  # macOS
    message(STATUS "Configuring for macOS")
    set(CMAKE_MACOSX_RPATH ON)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -stdlib=libc++")
    set(CMAKE_SHARED_LIBRARY_SUFFIX ".dylib")

elseif (CMAKE_SYSTEM_NAME STREQUAL "Linux")  # Linux
    message(STATUS "Configuring for Linux")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fPIC")

elseif (CMAKE_SYSTEM_NAME STREQUAL "Windows")  # Windows
    message(STATUS "Configuring for Windows")
    set(CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS ON)
    set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)
    set(CMAKE_SHARED_LIBRARY_SUFFIX ".dll")
    
    if (MSVC)
        add_compile_options(/W4 /WX)  # Treat warnings as errors in MSVC
    endif()
endif()
