# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 2.8

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canoncical targets will work.
.SUFFIXES:

# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list

# Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = "/Applications/CMake 2.8-5.app/Contents/bin/cmake"

# The command to remove a file.
RM = "/Applications/CMake 2.8-5.app/Contents/bin/cmake" -E remove -f

# The program to use to edit the cache.
CMAKE_EDIT_COMMAND = "/Applications/CMake 2.8-5.app/Contents/bin/ccmake"

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /Users/sheyne/Dropbox/Dev/libfreenect/wrappers/python

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Users/sheyne/Dropbox/Dev/libfreenect/wrappers/python

# Include any dependencies generated for this target.
include CMakeFiles/cython_freenect.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/cython_freenect.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/cython_freenect.dir/flags.make

CMakeFiles/cython_freenect.dir/freenect.o: CMakeFiles/cython_freenect.dir/flags.make
CMakeFiles/cython_freenect.dir/freenect.o: freenect.c
	$(CMAKE_COMMAND) -E cmake_progress_report /Users/sheyne/Dropbox/Dev/libfreenect/wrappers/python/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building C object CMakeFiles/cython_freenect.dir/freenect.o"
	/usr/bin/gcc  $(C_DEFINES) $(C_FLAGS) -o CMakeFiles/cython_freenect.dir/freenect.o   -c /Users/sheyne/Dropbox/Dev/libfreenect/wrappers/python/freenect.c

CMakeFiles/cython_freenect.dir/freenect.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/cython_freenect.dir/freenect.i"
	/usr/bin/gcc  $(C_DEFINES) $(C_FLAGS) -E /Users/sheyne/Dropbox/Dev/libfreenect/wrappers/python/freenect.c > CMakeFiles/cython_freenect.dir/freenect.i

CMakeFiles/cython_freenect.dir/freenect.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/cython_freenect.dir/freenect.s"
	/usr/bin/gcc  $(C_DEFINES) $(C_FLAGS) -S /Users/sheyne/Dropbox/Dev/libfreenect/wrappers/python/freenect.c -o CMakeFiles/cython_freenect.dir/freenect.s

CMakeFiles/cython_freenect.dir/freenect.o.requires:
.PHONY : CMakeFiles/cython_freenect.dir/freenect.o.requires

CMakeFiles/cython_freenect.dir/freenect.o.provides: CMakeFiles/cython_freenect.dir/freenect.o.requires
	$(MAKE) -f CMakeFiles/cython_freenect.dir/build.make CMakeFiles/cython_freenect.dir/freenect.o.provides.build
.PHONY : CMakeFiles/cython_freenect.dir/freenect.o.provides

CMakeFiles/cython_freenect.dir/freenect.o.provides.build: CMakeFiles/cython_freenect.dir/freenect.o

freenect.c:
	$(CMAKE_COMMAND) -E cmake_progress_report /Users/sheyne/Dropbox/Dev/libfreenect/wrappers/python/CMakeFiles $(CMAKE_PROGRESS_2)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Generating freenect.c"
	CYTHON_EXECUTABLE-NOTFOUND -o freenect.c /Users/sheyne/Dropbox/Dev/libfreenect/wrappers/python/freenect.pyx

# Object files for target cython_freenect
cython_freenect_OBJECTS = \
"CMakeFiles/cython_freenect.dir/freenect.o"

# External object files for target cython_freenect
cython_freenect_EXTERNAL_OBJECTS =

freenect.so: CMakeFiles/cython_freenect.dir/freenect.o
freenect.so: CMakeFiles/cython_freenect.dir/build.make
freenect.so: CMakeFiles/cython_freenect.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking C shared module freenect.so"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/cython_freenect.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/cython_freenect.dir/build: freenect.so
.PHONY : CMakeFiles/cython_freenect.dir/build

CMakeFiles/cython_freenect.dir/requires: CMakeFiles/cython_freenect.dir/freenect.o.requires
.PHONY : CMakeFiles/cython_freenect.dir/requires

CMakeFiles/cython_freenect.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/cython_freenect.dir/cmake_clean.cmake
.PHONY : CMakeFiles/cython_freenect.dir/clean

CMakeFiles/cython_freenect.dir/depend: freenect.c
	cd /Users/sheyne/Dropbox/Dev/libfreenect/wrappers/python && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/sheyne/Dropbox/Dev/libfreenect/wrappers/python /Users/sheyne/Dropbox/Dev/libfreenect/wrappers/python /Users/sheyne/Dropbox/Dev/libfreenect/wrappers/python /Users/sheyne/Dropbox/Dev/libfreenect/wrappers/python /Users/sheyne/Dropbox/Dev/libfreenect/wrappers/python/CMakeFiles/cython_freenect.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/cython_freenect.dir/depend
