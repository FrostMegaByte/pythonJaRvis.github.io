<head>
    <script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>
    <script type="text/x-mathjax-config">
        MathJax.Hub.Config({
            tex2jax: {
            skipTags: ['script', 'noscript', 'style', 'textarea', 'pre'],
            inlineMath: [['$','$']]
            }
        });
    </script>
</head>
## ABSTRACT

Call graph generation is the foundation of inter-procedural static analysis. PyCG is the state-of-the-art approach for generating call graphs for Python programs. Unfortunately, PyCG does not scale to large programs when adapted to whole-program analysis where dependent libraries are also analyzed. Further, PyCG does not support demand-driven analysis where only the reachable functions from givenentry functions are analyzed. Moreover, PyCG is flow-insensitive and~does not fully support Python's features, hindering its accuracy.

 For example, to track vulnerable functions in external libraries, we are interested to find if the call graphs invoked from main functions in application have reachable paths to the vulnerable functions. 

To overcome these drawbacks, we propose a scalable demand-driven approach for generating call graphs for Python programs,and implement it as a prototype tool maintains an assignment graph (i.e., points-to relations~between program identifiers) for each function in a program to allow reuse and improve scalability. Given a set of entry functions as the demands, generates the call graph on-the-fly, where flow-sensitive intra-procedural analysis and inter-procedural analysis are conducted in turn. Our evaluation on a micro-benchmark of 135 small Python programs and a macro-benchmark of 6 real-world Python applications has demonstrated that  can significantly improve PyCG by at least 67% faster in time, 84% higher in precision, and at least 10% higher in recall.



The paper has been submitted to ESEC/FSE 2023, please see our [code](Jarvis.zip)  and [data](data.zip) here.



# Transfer rules

$$\begin{align*}
&{Import:}~from~m~^\prime~import~x, import~m^\prime \\
&\frac{\begin{matrix}
d_1=new\_def(m,~x), d_2=new\_def(m^\prime,~x), d_3=d_m, d_4=new\_def(m^\prime)
\end{matrix}
}{ \Delta_{e} \leftarrow \langle d_1, d_2, e\rangle, \Delta_{e} \leftarrow \langle d_3, d_4, e\rangle}\\
&{Assign:}~x=y \\
&\frac{d_1=new\_def(x), d_2=new\_def(y)} { \Delta_{e} \leftarrow \langle d_1, d_2, e\rangle} \\
&{Store:}~x.field~=~y\\
&\frac{d_i \in points(x), d_2 = new\_def(y)}{\Delta_{e} \leftarrow \langle d_i.field, d_2, e\rangle}\\
&{Load:}~y~=~x.field\\
&\frac{d_1 \in new\_def(y), d_j \in points(x)}{\Delta_{e} \leftarrow \langle d_1, d_j.field,~e \rangle} \\
&{New:}~y~=~new~x(...) \\
&\frac{d_1=new\_def(y), d_2=new\_def(x)}{
\begin{matrix}
\Delta_{e}~\leftarrow~{inter\_analysis}(f,~e,~\mathcal{FAG}^f_{e.p}), \Delta_{e}~\leftarrow~\langle~d_1,~d_2,~e~\rangle\\
\end{matrix}
} \\
&{Call:}~a=x.m(...) \\
&\frac{
\begin{matrix}
d_1=new\_def(x), d_2=new\_def(d_1.m), d_3=new\_def(a)
\end{matrix}
}
{\begin{matrix}
\Delta_{call}~\leftarrow~{inter\_analysis}(f,~e,~\mathcal{FAG}^f_{e.p}), \Delta_{call}~\leftarrow~\langle~d_3,~d_2.\textit{<ret>},~e\rangle
\end{matrix}
}\\
&{Func:}~def~m^\prime(args...) ...\\
&\frac{d=new\_def(m^\prime),d_{1...n}=new\_def(args_{1...n})}{\Delta_{e} \leftarrow \langle d, \varnothing, e \rangle,\mathcal{F} \leftarrow \langle d,args_{1...n} \rangle}\\
&{Class:}~class~cls(base...) ...\\
&\frac{d=new\_def(cls),base_{1...n}=new\_def(base_{1...n})}{\Delta_{e} \leftarrow \langle d, \varnothing, e \rangle,\mathcal{C} \leftarrow \langle d,base_{1...n} \rangle}\\
&{Return:}~def~m^\prime ...~return~x\\
&\frac{d_1=new\_def(m^\prime), d_2=new\_def(x)}{\Delta_{e} \leftarrow \langle d_1.\textit{<ret>}, d_2, e \rangle}\\
&{With:}~with~cls()~as~f\\
&\frac{
\begin{matrix}
d_1=new\_def(cls), d_2=new\_def(cls.\_\_enter\_\_), d_3=new\_def(f)
\end{matrix}
}
{\begin{matrix}
\Delta_{call}~\leftarrow~{inter\_analysis}(f,~e,~\mathcal{FAG}^f_{e.p}), \Delta_{call}~\leftarrow~\langle~d_3,~d_2.\textit{<ret>},~e\rangle
\end{matrix}
}\\
&{For:}~for~x~in~cls()\\
&\frac{
\begin{matrix}
d_1=new\_def(cls), d_2=new\_def(cls.\_\_iter\_\_), d_3=new\_def(f)
\end{matrix}
}
{\begin{matrix}
\Delta_{call}~\leftarrow~{inter\_analysis}(f,~e,~\mathcal{FAG}^f_{e.p}), \Delta_{call}~\leftarrow~\langle~d_3,~d_2.\textit{<ret>},~e\rangle
\end{matrix}
}\\
\end{align*}$$