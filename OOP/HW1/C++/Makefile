all: main main2

CC=g++

main2: stack.o main2.o
	$(CC) -o main2 main2.o stack.o
main: stack.o main.o
	$(CC) -o main main.o stack.o
stack.o: stack.cpp stack.h
	$(CC) -c stack.cpp
main.o: main.cpp
	$(CC) -c main.cpp
main2.o: main2.cpp
	$(CC) -c main2.cpp
dep:
	$(CC) -MM main.cpp main2.cpp > .dep

clean:
	rm -f stack.o main.o main .dep main2 main2.o
