##### How to Compile #####
g++ -o main main.cpp

##### How to Run #####
./main eil51.txt
./main eil101.txt

the result will show on screen, and the path will output to 'output.txt'

##### How to Draw path #####
gnuplot
plot 'output.txt' using 2:3 with linespoints

### BEST CASES ###
EIL101:
Path: 24 29 79 78 34 35 65 66 71 9 81 33 3 77 68 80 76 50 1 69 70 10 31 27 101 53 58 40 73 74 72 21 26 54 4 55 25 39 67 23 56 75 22 41 15 43 42 97 37 98 93 85 44 38 14 100 91 16 86 61 60 83 18 52 88 62 7 82 48 19 11 63 90 30 51 20 32 64 49 36 47 46 8 45 17 84 5 99 96 94 13 2 57 87 95 92 59 6 89 28 12 

Distance: 748

EIL51:
Path: 19 40 41 13 25 14 24 43 7 23 6 48 8 26 31 28 3 36 35 20 2 22 1 27 32 11 38 5 49 9 50 16 29 21 34 30 10 39 33 45 15 17 4 18 47 51 46 12 37 44 42 

Distance: 441

