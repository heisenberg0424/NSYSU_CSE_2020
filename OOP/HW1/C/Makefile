all: main main2

CC=gcc

main2: stack.o main2.o
	$(CC) -o main2 main2.o stack.o
main: stack.o main.o
	$(CC) -o main main.o stack.o
stack.o: stack.c stack.h
	$(CC) -c stack.c
main.o: main.c
	$(CC) -c main.c
main2.o: main2.c
	$(CC) -c main2.c
dep:
	$(CC) -M main.c main2.c > dep

clean:
	rm -f stack.o main.o main dep main2.o main2
