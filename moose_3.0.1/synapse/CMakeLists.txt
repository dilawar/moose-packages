cmake_minimum_required(VERSION 2.6)
include_directories(../basecode ../utility ../kinetics)
add_library(synapse
    SimpleSynHandler.cpp
    Synapse.cpp
    SynHandlerBase.cpp
    testSynapse.cpp
    )
