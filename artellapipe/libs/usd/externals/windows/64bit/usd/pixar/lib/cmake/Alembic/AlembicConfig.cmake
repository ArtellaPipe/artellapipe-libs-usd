INCLUDE("${CMAKE_CURRENT_LIST_DIR}/AlembicTargets.cmake")

SET(Alembic_HAS_HDF5 OFF)
SET(Alembic_HAS_SHARED_LIBS ON)

SET(Alembic_USES_BOOST OFF)
if(OFF AND NOT OFF)
    SET(Alembic_USES_TR1 TRUE)
else()
    SET(Alembic_USES_TR1 FALSE)
endif()
