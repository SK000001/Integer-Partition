prt:
	g++ -lgmpxx -lgmp -std=c++11 partition.cpp -o partition && ./partition

dprt:
	g++ -lgmpxx -lgmp -std=c++11 dynamic_partition.cpp -o dynamic_partition && ./dynamic_partition
