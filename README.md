# LinearAlgebraHomeworkHelper

Here's a small project I wrote to output step-by-step the process of solving a linear algebra problem so that I can easily check my homework. It can perform simple operations such as matrix inversion, matrix multiplication, and matrix transpose. During this process, intermediate processes can be output in $\LaTeX$ format.

## Approach

There are three main difficulties in this project:

1. Solve RREF. [sympy](https://docs.sympy.org/latest/tutorials/intro-tutorial/matrices.html) provides library functions`.rref()`, so convert to Matrix format and you can use it easily (don't forget to convert back).
2. Matrix inversion. I use [Gaussian elimination](https://en.wikipedia.org/wiki/Gaussian_elimination#Finding_the_inverse_of_a_matrix) to solve this problem.
3. Fractional output. By using [fractions](https://docs.python.org/3/library/fractions.html), I got the output in fractional form, and then taking the numerator and denominator separately, I was able to output `\frac{}{}` format.

## Setup

You need to use [python](https://www.python.org/) to run the program. In addition, you also need to install some dependent library files:

```python
pip install numpy sympy fractions
```

If you can only download at extremely low speeds for some reason, try using mirror sites:

```python
pip install numpy sympy fractions -i https://pypi.tuna.tsinghua.edu.cn/simple/
```

## Usage

If the function requires a `trace` parameter, when `trace = 2`, it will output the process in latex format. By default, all matrix operation functions get in and out matrices in `numpy` format.

- `MatRREF(a, trace = 0)`:  Return the inverse of matrix `a`.
- `MatProduct(A, B)`: Return the product of matrix `A` and `B`.
- `MatInv(a, trace = 0)`: Return the inversion of matrix `a`.

There are also functions for formatted output of matrices:

- `formatPrint(A)`: Print matrix in $\LaTeX$ format.
- `uniPrint(A, I)`: Merge the output of two matrices, which are used to output `A` and `I` at the same time in matrix inversion.
- `uniFormatPrint(A, I)`: Like `uniPrint`, but in $\LaTeX$ format.

## Example

### MatRREF

Input

```python
Mat1 = np.array([[1, 2, 3, 13], [2, 2, 1, 9], [4, -1, -2, 1]])
MatRREF(Mat1, 2)
```

Output:

```latex
\left[\begin{array}{cccc}
1 & 2 & 3 & 13 \\
2 & 2 & 1 & 9 \\
4 & -1 & -2 & 1 
\end{array}\right]
\stackrel{\text{reduced echelon form}}\longrightarrow
\left[\begin{array}{cccc}
1 & 0 & 0 & 2 \\
0 & 1 & 0 & 1 \\
0 & 0 & 1 & 3 
\end{array}\right]
```

$$
\left[\begin{array}{cccc}
1 & 2 & 3 & 13 \\
2 & 2 & 1 & 9 \\
4 & -1 & -2 & 1 
\end{array}\right]
\stackrel{\text{reduced echelon form}}\longrightarrow
\left[\begin{array}{cccc}
1 & 0 & 0 & 2 \\
0 & 1 & 0 & 1 \\
0 & 0 & 1 & 3 
\end{array}\right]
$$

### MatInv

Input

```python
Mat1 = np.array([[1.0, 2.0, 3.0], [2.0, 2.0, 1.0], [4.0, -1.0, -2.0]])
MatInv(Mat1, 2)
```

Output

```latex
\left[\begin{array}{cccccc}
1 & 2 & 3 & 1 & 0 & 0 \\
2 & 2 & 1 & 0 & 1 & 0 \\
4 & -1 & -2 & 0 & 0 & 1 \end{array}\right]
\stackrel{[2] = [2] + (
-2)\times[1]}\longrightarrow
\left[\begin{array}{cccccc}
1 & 2 & 3 & 1 & 0 & 0 \\
0 & -2 & -5 & -2 & 1 & 0 \\
4 & -1 & -2 & 0 & 0 & 1 \end{array}\right]
\stackrel{[3] = [3] + (
-4)\times[1]}\longrightarrow
\left[\begin{array}{cccccc}
1 & 2 & 3 & 1 & 0 & 0 \\
0 & -2 & -5 & -2 & 1 & 0 \\
0 & -9 & -14 & -4 & 0 & 1 \end{array}\right]
\stackrel{[1] = [1] + (
1)\times[2]}\longrightarrow
\left[\begin{array}{cccccc}
1 & 0 & -2 & -1 & 1 & 0 \\
0 & -2 & -5 & -2 & 1 & 0 \\
0 & -9 & -14 & -4 & 0 & 1 \end{array}\right]
\stackrel{[3] = [3] + (
-\frac{9}{2})\times[2]}\longrightarrow
\left[\begin{array}{cccccc}
1 & 0 & -2 & -1 & 1 & 0 \\
0 & -2 & -5 & -2 & 1 & 0 \\
0 & 0 & \frac{17}{2} & 5 & -\frac{9}{2} & 1 \end{array}\right]
\stackrel{[1] = [1] + (
\frac{4}{17})\times[3]}\longrightarrow
\left[\begin{array}{cccccc}
1 & 0 & 0 & \frac{3}{17} & -\frac{1}{17} & \frac{4}{17} \\
0 & -2 & -5 & -2 & 1 & 0 \\
0 & 0 & \frac{17}{2} & 5 & -\frac{9}{2} & 1 \end{array}\right]
\stackrel{[2] = [2] + (
\frac{10}{17})\times[3]}\longrightarrow
\left[\begin{array}{cccccc}
1 & 0 & 0 & \frac{3}{17} & -\frac{1}{17} & \frac{4}{17} \\
0 & -2 & 0 & \frac{16}{17} & -\frac{28}{17} & \frac{10}{17} \\
0 & 0 & \frac{17}{2} & 5 & -\frac{9}{2} & 1 \end{array}\right]
\stackrel{[2] = [2] / (
-2)}\longrightarrow\stackrel{[3] = [3] / (
\frac{17}{2})}\longrightarrow\left[\begin{array}{cccccc}
1 & 0 & 0 & \frac{3}{17} & -\frac{1}{17} & \frac{4}{17} \\
0 & 1 & 0 & -\frac{8}{17} & \frac{14}{17} & -\frac{5}{17} \\
0 & 0 & 1 & \frac{10}{17} & -\frac{9}{17} & \frac{2}{17} \end{array}\right]
```

The formula block on Github cannot wrap automatically. This code can be displayed perfectly on my TeXworks editor, so I wrap it manually.

$$
\left[\begin{array}{cccccc}
1 & 2 & 3 & 1 & 0 & 0 \\
2 & 2 & 1 & 0 & 1 & 0 \\
4 & -1 & -2 & 0 & 0 & 1 \end{array}\right]
\stackrel{[2] = [2] + (
-2)\times[1]}\longrightarrow
\left[\begin{array}{cccccc}
1 & 2 & 3 & 1 & 0 & 0 \\
0 & -2 & -5 & -2 & 1 & 0 \\
4 & -1 & -2 & 0 & 0 & 1 \end{array}\right]
$$

$$
\stackrel{[3] = [3] + (
-4)\times[1]}\longrightarrow
\left[\begin{array}{cccccc}
1 & 2 & 3 & 1 & 0 & 0 \\
0 & -2 & -5 & -2 & 1 & 0 \\
0 & -9 & -14 & -4 & 0 & 1 \end{array}\right]
\stackrel{[1] = [1] + (
1)\times[2]}\longrightarrow
\left[\begin{array}{cccccc}
1 & 0 & -2 & -1 & 1 & 0 \\
0 & -2 & -5 & -2 & 1 & 0 \\
0 & -9 & -14 & -4 & 0 & 1 \end{array}\right]
$$

$$
\stackrel{[3] = [3] + (
-\frac{9}{2})\times[2]}\longrightarrow
\left[\begin{array}{cccccc}
1 & 0 & -2 & -1 & 1 & 0 \\
0 & -2 & -5 & -2 & 1 & 0 \\
0 & 0 & \frac{17}{2} & 5 & -\frac{9}{2} & 1 \end{array}\right]
\stackrel{[1] = [1] + (
\frac{4}{17})\times[3]}\longrightarrow
\left[\begin{array}{cccccc}
1 & 0 & 0 & \frac{3}{17} & -\frac{1}{17} & \frac{4}{17} \\
0 & -2 & -5 & -2 & 1 & 0 \\
0 & 0 & \frac{17}{2} & 5 & -\frac{9}{2} & 1 \end{array}\right]
$$

$$
\stackrel{[2] = [2] + (
\frac{10}{17})\times[3]}\longrightarrow
\left[\begin{array}{cccccc}
1 & 0 & 0 & \frac{3}{17} & -\frac{1}{17} & \frac{4}{17} \\
0 & -2 & 0 & \frac{16}{17} & -\frac{28}{17} & \frac{10}{17} \\
0 & 0 & \frac{17}{2} & 5 & -\frac{9}{2} & 1 \end{array}\right]
\stackrel{[2] = [2] / (
-2)}\longrightarrow\stackrel{[3] = [3] / (
\frac{17}{2})}\longrightarrow\left[\begin{array}{cccccc}
1 & 0 & 0 & \frac{3}{17} & -\frac{1}{17} & \frac{4}{17} \\
0 & 1 & 0 & -\frac{8}{17} & \frac{14}{17} & -\frac{5}{17} \\
0 & 0 & 1 & \frac{10}{17} & -\frac{9}{17} & \frac{2}{17} \end{array}\right]
$$

