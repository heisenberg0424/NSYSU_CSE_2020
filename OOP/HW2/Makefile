all: mytar

CC=g++

mytar: mytar.o main.o
	$(CC) -o mytar main.o mytar.o
mytar.o: mytar.cpp mytar.h
	$(CC) -c mytar.cpp
main.o: main.cpp
	$(CC) -c main.cpp
dep:
	$(CC) -MM main.cpp > .dep

clean:
	rm -f mytar.o main.o mytar .dep
