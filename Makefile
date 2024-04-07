prt_cpp:
	@echo "Compiling partition.cpp..."
	@g++ partition.cpp -lgmpxx -lgmp -o partition
	@echo "Executing partition..."
	@./partition
	@echo.
	@pause
	@del partition.exe

dprt_cpp:
	@echo "Compiling dynamic_partition.cpp..."
	@g++ dynamic_partition.cpp -lgmpxx -lgmp -o dynamic_partition
	@echo "Executing dynamic_partition..."
	@./dynamic_partition
	@echo.
	@pause
	@del dynamic_partition.exe

dprt:
	@powershell -Command "echo 'language choice:'; echo '1. C++'; echo '2. Python'; $$input = Read-Host -Prompt 'Enter your Choice'; clear; if ($$input -eq '1') { make dprt_cpp } else { python3 dynamic_partition.py }"

prt:
	@powershell -Command "echo 'language choice:'; echo '1. C++'; echo '2. Python'; $$input = Read-Host -Prompt 'Enter your Choice'; clear;  if ($$input -eq '1') { make prt_cpp } else { python3 partition.py }"

clean:
	@del x.bin y.bin p.bin

partition:
	@powershell -Command "echo 'Lets start the partition!'; echo '1. Partition (high number = SLOW!!)'; echo '2. Dynamic Partition (Saves Each iteration, so FAST!!)'; $$input = Read-Host -Prompt 'Enter your Choice'; clear; if ($$input -eq '1') { make prt } else { make dprt }"