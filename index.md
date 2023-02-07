## ABSTRACT

Call graph generation is the foundation of inter-procedural static analysis. PyCG is the state-of-the-art approach for generating call graphs for Python programs. Unfortunately, PyCG does not scale to large programs when adapted to whole-program analysis where dependent libraries are also analyzed. Further, PyCG does not support demand-driven analysis where only the reachable functions from givenentry functions are analyzed. Moreover, PyCG is flow-insensitive and~does not fully support Python's features, hindering its accuracy.

 For example, to track vulnerable functions in external libraries, we are interested to find if the call graphs invoked from main functions in application have reachable paths to the vulnerable functions. 

To overcome these drawbacks, we propose a scalable demand-driven approach for generating call graphs for Python programs,and implement it as a prototype tool maintains an assignment graph (i.e., points-to relations~between program identifiers) for each function in a program to allow reuse and improve scalability. Given a set of entry functions as the demands, generates the call graph on-the-fly, where flow-sensitive intra-procedural analysis and inter-procedural analysis are conducted in turn. Our evaluation on a micro-benchmark of 135 small Python programs and a macro-benchmark of 6 real-world Python applications has demonstrated that  can significantly improve PyCG by at least 67% faster in time, 84% higher in precision, and at least 10% higher in recall.



The paper has been submitted to FSE 2023, please see our [code](Jarvis.zip)  and [dataset](groundTruth.zip) here.



# Transfer rules

