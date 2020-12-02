all: main

CC=g++

main: Main.cpp
	$(CC) Main.cpp -o main
dep:
	$(CC) -MM Main.cpp > .dep

clean:
	rm -f *.o main
