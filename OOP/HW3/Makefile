all: main

CC=g++

main: Complex.o main.o
	$(CC) -o main main.o Complex.o
Complex.o: Complex.cpp Complex.h
	$(CC) -c Complex.cpp
main.o: main.cpp
	$(CC) -c main.cpp
dep:
	$(CC) -MM main.cpp > .dep

clean:
	rm -f Complex.o main.o main .dep
