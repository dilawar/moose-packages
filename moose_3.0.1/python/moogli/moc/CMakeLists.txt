FILE(GLOB SRCS *.cpp)
ADD_LIBRARY(moc STATIC
    ${SRCS}
)

