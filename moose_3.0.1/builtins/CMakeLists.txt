include_directories(../msg)
include_directories(../basecode)
include_directories(../external/muparser)
add_library(moose_builtins
    Arith.cpp
    Group.cpp
    Mstring.cpp
    Func.cpp
    Function.cpp
    Variable.cpp
    TableBase.cpp
    Table.cpp
    Interpol.cpp
    StimulusTable.cpp
    TimeTable.cpp
    Stats.cpp
    Interpol2D.cpp
    HDF5WriterBase.cpp
    HDF5DataWriter.cpp
    testBuiltins.cpp
    )
