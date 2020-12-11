all: main

CC=g++

main: main.o Trace.o
	$(CC) -o main *.o
main.o: main.cpp Trace.cpp
	$(CC) -c *.cpp

dep:
	$(CC) -MM main.cpp > .dep

clean:
	rm -f *.o main
