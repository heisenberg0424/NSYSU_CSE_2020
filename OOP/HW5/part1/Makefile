all: main

CC=g++

main: main.cpp
	$(CC) main.cpp -o main
dep:
	$(CC) -MM main.cpp > .dep

clean:
	rm -f *.o main
