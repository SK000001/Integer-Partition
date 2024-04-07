prt:
	g++ partition.cpp -lgmpxx -lgmp -o partition
	./partition

dprt:
	g++ dynamic_partition.cpp -lgmpxx -lgmp -o dynamic_partition
	./dynamic_partition