########## MACROS ###########################################################################
#############################################################################################

# Requires CMake > 3.15
if(${CMAKE_VERSION} VERSION_LESS "3.15")
    message(FATAL_ERROR "The 'CMakeDeps' generator only works with CMake >= 3.15")
endif()

if(gmp_FIND_QUIETLY)
    set(gmp_MESSAGE_MODE VERBOSE)
else()
    set(gmp_MESSAGE_MODE STATUS)
endif()

include(${CMAKE_CURRENT_LIST_DIR}/cmakedeps_macros.cmake)
include(${CMAKE_CURRENT_LIST_DIR}/gmpTargets.cmake)
include(CMakeFindDependencyMacro)

check_build_type_defined()

foreach(_DEPENDENCY ${gmp_FIND_DEPENDENCY_NAMES} )
    # Check that we have not already called a find_package with the transitive dependency
    if(NOT ${_DEPENDENCY}_FOUND)
        find_dependency(${_DEPENDENCY} REQUIRED ${${_DEPENDENCY}_FIND_MODE})
    endif()
endforeach()

set(gmp_VERSION_STRING "6.3.0")
set(gmp_INCLUDE_DIRS ${gmp_INCLUDE_DIRS_RELEASE} )
set(gmp_INCLUDE_DIR ${gmp_INCLUDE_DIRS_RELEASE} )
set(gmp_LIBRARIES ${gmp_LIBRARIES_RELEASE} )
set(gmp_DEFINITIONS ${gmp_DEFINITIONS_RELEASE} )

# Only the first installed configuration is included to avoid the collision
foreach(_BUILD_MODULE ${gmp_BUILD_MODULES_PATHS_RELEASE} )
    message(${gmp_MESSAGE_MODE} "Conan: Including build module from '${_BUILD_MODULE}'")
    include(${_BUILD_MODULE})
endforeach()


