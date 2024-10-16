### Project Title: Distributed Computing - Custom MapReduce Framework

### Description:

This project implements a custom MapReduce framework in Python, designed for distributed computing. The framework supports **Natural Join** operations, simulating functionalities of well-known distributed computing frameworks like Apache Hadoop and Spark, without relying on existing libraries. The project provides hands-on experience with parallel processing and gRPC for inter-process communication. The framework includes dynamic resource allocation and optimized data partitioning.

### Technologies Used:

* **Programming Language:** Python
* **Communication Protocol:** gRPC
* **Parallel Processing:** Python Multiprocessing Module

### Installation:

**Python and gRPC Setup:**

This project requires Python 3.x, gRPC, and Protocol Buffers. Follow these steps to set up the environment:

1. **Install dependencies**:
   ```bash
   pip install grpcio grpcio-tools
   ```

2. **Generate gRPC Code**:
   ```bash
   python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. natural_join.proto
   ```

### Usage:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/herschelle19045/assignments-iiitd.git
   cd assignments-iiitd/Distributed\ Computing/Project
   ```

2. **Run the Program**:
   ```bash
   python main.py
   ```

3. **View the Output**:
   The output files will be saved in the `output/` directory after running the program. The program reads input files from the `input/` directory and processes them using the custom MapReduce framework.

### Algorithm Overview:

The MapReduce framework performs the following steps:

1. **Data Partitioning**: The master node splits the input data into chunks, which are distributed to individual mapper processes.
2. **Mapping**: Each mapper processes its assigned data chunk and generates key-value pairs based on the Natural Join operation.
3. **Shuffling and Partitioning**: The master initiates partitioning and shuffling to assign intermediate data to reducers.
4. **Reducing**: Reducers aggregate the partitioned data and output the final joined data based on key-value pairs.

### Future Work:

The project can be extended by:
  - Adding support for additional queries like **Word Count** or **Inverted Index**.
  - Optimizing partitioning and shuffling for increased performance with larger datasets.
  - Integrating the framework with a multi-node distributed environment.
