# [↓](#↑)

[TOC]



## Introduction

- **Functional language**
  - Definition and application of **functions**
    - written as code
    - treated as values
  - Everything is an **expression**
- **No side effects**
  - Computation is by **evaluation**
  - Allowed in printing output
  - Expressions creates a **new element** associated with the result
- **Higher-order functions**
  - Functions can functions as values
- **Polymorphism**
  - A function can have arguments of **different types**
  - Possibility to define a stack that works for different types
- **Abstract Data Types** (structures)
  - **Elegant** type system
  - Ability to construct **new types**
  - Constructs that restrict access to objects of a **given type**
- **Recursion**
  - Strongly encouraged
  - Implemented efficiently
- **Rule based programming**
  - If-then-else rules implemented via **pattern matching**
- **Strong typing**
  - Values and variables have types that are determined at “**compile-time**”
  - Variable **declaration not needed**
- **Standard basis**
  - Built-in structures `Int`, `Real` etc.



### Running ML

- Command line: `poly`

  - ```ocaml
    > 1 + 2 * 3;
    val it = 7: int
    ```

  - `val`: value of expression
    `int`: type of result, inferred automatically

- From file: `poly < filename`




## Types

- **Basic types**
  - `int real bool char string`
  - `unit exn instream outstream`
- **Compound types**
  - `T1 * T2 * ... * Tn`  (tuples)
  - `T list`
- **Functions**
  - `T1 -> T2`
- **Options**
  - `T1 option`



### Constants

- **Integers**
  - Normal  `420`
  - Negative  `~420`
  - Hexadecimal  `(~)0x420`
- **Reals**
  - Decimal  `(~)4.20`
  - Scientific  `(~)4.2e(~)20`
- **Booleans**  `true` and `false`
- **Strings**  `"foo"`
- **Characters**  `#"a"`



### Conversion

- **Integer to real**
  - `real(4)`
  - `real 4`
- **Real to integer**
  - `floor`  round down
  - `ceil`  round up
  - `round`  nearest integer
  - `trunc`  truncate
- **Characters and integers**
  - `ord #"a"`  char to int (`97`)
  - `chr 97`  int to char (`#"a"`)
  - `str #"a"`  char to string (`"a"`)
- **Primitive to string**
  - `Int.toString(420)`
  - `Real.toString(42.0)`
  - `Bool.toString(true)`



### Variables

```ocaml
> val pi = 3;
val pi = 3: int
```

```ocaml
> val pi = 3.14159;
val pi = 3.14159: real
```

- **No** variable **declaration** needed
  - ML deduces the **type automatically**
- A new declaration creates a **new variable**
  - The type can change
  - Old definition is no longer accessible



### Tuples

Collection of elements of **different types** (tuples too)

```ocaml
> val t = (1, 2, 3);
val t = (1, 2, 3): int * int * int
```

```ocaml
> val t = (1, (2, 3, 4));
val t = (1, (2, 3, 4)): int * (int * int * int)
```

```ocaml
> val t = (4, 5.0, "six");
val t = (4, 5.0, "six"): int * real * string
```

**Accessing components**  `#1 t;`

```ocaml
> #1 (t);
val it = 4: int
> #2 (t);
val it = 5.0: real
> #3 (t);
val it = "six": string
```



### Lists

Collection of elements of the **same type**

```ocaml
> val L = [1, 2, 3];
val L = [1, 2, 3]: int list
```

```ocaml
> [];
val it = []: 'a list
> nil;
val it = []: 'a list
```

- **Head**  `hd (L)`

  ```ocaml
  > hd (L);
  val it = 1: int
  ```

- **Tail**  `tl (L)`

  ```ocaml
  > tl (L);
  val it = [2, 3]: int list
  ```

- **Concatenation**  `L1 @ L2`

  ```ocaml
  > [1,2] @ [3,4];
  val it = [1, 2, 3, 4]: int list
  ```

  Lists must be the **same type**

- **Cons**  `::`

  **Combines** an element of type `'a` and a list of type `'a list`

  `::` is **right associative**

  ```ocaml
  > 2 :: [3,4];
  val it = [2, 3, 4]: int list
  ```

  ```ocaml
  > 2 :: nil;
  val it = [2]: int list
  > 2 :: [];
  val it = [2]: int list
  ```

  ```ocaml
  > 1 :: 2 :: 3 :: nil;
  val it = [1, 2, 3]: int list
  > (1 :: (2 :: (3 :: nil)));
  val it = [1, 2, 3]: int list
  ```



### Strings

- **Concatenation**  `str1 ^ str2`

  ```ocaml
  > "ab" ^ "cd";
  val it = "abcd": string
  ```

- **Strings to lists**  `explode (str)`

  ```ocaml
  > explode ("abcd");
  val it = [#"a", #"b", #"c", #"d"]: char list
  ```

- **Lists to string**  `implode (L)`

  ```ocaml
  > implode ([#"a", #"b", #"c", #"d"]);
  val it = "abcd": string
  ```



### Equality types

Types that allow the use of **equality tests** (`= <>`)

- Int, bool, char, string
- Tuples and lists of equality types
- Not reals and functions
- Identified as `''a`



## Operators

- **Arithmetic**

  - `+ - * / div mod ~`
  - Precedence rules
  - `Function: + : 'a * 'a -> 'a`
    - Use prefix form  `+ (a, b)`
    - Allow infix notation  `a + b`
    - Have one argument, that is a tuple of two numbers  `(a, b)`
    - Type of the operator is  `'a * 'a -> 'a`
      Based on the first argument
    - Can't unify different types
  - `Function: {~ + - * div mod} : int * int -> int`
  - `Function: {~ + - * /} : real * real -> real`
  
- **Comparison**
- `= < > <= >= <>`
  - `= <>`  **not** allowed for **reals** and **functions**
  - `= <>`  allowed for **tuples** and **lists** of equality types
  
- **Logical**

  - `not andalso orelse`
  - Lazy evaluation
  - Precedence  `not (1 < 2)`



## Conditionals

### If then else

- Is an **expression**

  - It must have a **value**
  - `else` is **not optional**

- It must have a well-defined **type**




### Case

```ocaml
> datatype 'a option = NONE | SOME of 'a;
datatype 'a option = NONE | SOME of 'a
> fun sum a b =
    case (a,b) of
      (NONE, SOME x) => x |
      (SOME x, NONE) => x |
      (SOME x, SOME y) => x + y;
val fun = fn: 'a option -> 'a option -> 'a
```



## Functions

**Syntax**  `fun <name> <parameters> = <expression>;`

**Type**  `fn: 'a -> 'b`

```ocaml
> fun upper(c) = chr (ord(c) - 32);
val upper = fn: char -> char
> upper (#"b");
val it = #"B": char
> upper #"a";
val it = #"A": char
```

- `'a -> 'b`  is the **type** of a function that takes an object of type `'a` and produces one of type `'b`
- ML deduces the **types** of functions **automatically**

- `'a`  and `'b` can be any type, including **function types**

- **Associativity**  `'a -> 'b -> 'c`  means `'a -> ('b -> 'c)`

- **Specifying types**  `(<val>:<type>)`

  ```ocaml
  > fun square (x) = x * x;
  val square = fn: int -> int
  > fun square (x:real) = x * x;
  val square = fn: real -> real
  ```

- **Multiple arguments** are treated as a single parameter of type **tuple**

  ```ocaml
  > fun max3 (a:real, b, c) =  (* maximum of reals *)
  	if a > b then
    	  if a > c then a else c
    	else
    	  if b > c then b else c;
  val max3 = fn: real * real * real -> real
  > max3 (5.0, 4.0, 7.0);
  val it = 7.0: real
  ```

- **Referencing external values**

  The value of a variable is that when the function is **defined**

  ```ocaml
  > val x = 3;
  > fun addx (a) = a + x;
  > val x = 10;
  > addx (2);
  val it = 5: int
  ```



### Recursion

Main mechanism for **iteration**

- **Basis**: compute the result directly for sufficiently small arguments
- **Inductive step**: call the function recursively with smaller arguments


- **Nonlinear recursion**: a function that call itself recursively multiple times

  ```ocaml
  > fun comb (n, m) = (* assumes 0 <= m <= n *)
  	if m = 0 orelse m = n then 1
  	else comb (n-1, m) + comb (n-1, m-1);
  val comb = fn: int * int -> int
  > comb (5, 2);
  val it = 10: int
  ```

- **Mutual recursion**: two functions that call one another recursively (`and`)

  ```ocaml
  > fun
  	take(L) =
  	  if L = nil then nil
  	  else hd(L) :: skip(tl(L))
    and  (* necessary for declaration *)
      skip(L) =
        if L = nil then nil
        else take(tl(L));
  val skip = fn: ''a list -> ''a list
  val take = fn: ''a list -> ''a list
  > take ([1,2,3,4,5]);
  val it = [1, 3, 5]: int list
  ```



### Patterns

Powerful mechanism for **defining functions**

Function definition uses a **sequence of patterns**, with the first one that matches the parameter being used

The list of **alternatives** must be exhaustive 

A **variable** must be used **only once** in a pattern

```ocaml
> fun reverse (nil) = nil
   |  reverse (x::xs) = reverse (xs) @ [x];
val reverse = fn: 'a list -> 'a list
```

- **Parameters**

  - <u>Allowed</u>: constants, expressions with `::`, tuples
  - <u>Not allowed</u>: arithmetics, concatenation, reals, multiple use of variables
  - <u>Warning</u>: redundant patterns

- **`as` statement**: match patterns and assign variables

  ```ocaml
  > fun merge (nil, M) = M
     |  merge (L, nil) = L
     |  merge (L as x::xs, M as y::ys) =
  		if x<y then x::merge(xs,M)
  		else y::merge (L,ys);
  val merge = fn: int list * int list -> int list
  ```

- **Anonymous variables `_`**: match a pattern without referring to the value

  ```ocaml
  > fun comb (_, 0) = 1
     |  comb (n, m) =
     	    if m = n then 1
     	    else comb (n-1, m) + comb (n-1, m-1);
  val comb = fn: int * int -> int
  ```



### Local environments

Create **local values** inside a function declaration (`let`)

No need to introduce **new names**

```ocaml
> fun pow100 (x:real) =
    let 
  	  val x = x*x*x*x*x;
  	  val x = x*x*x*x*x;
    in
  	  x*x*x*x
    end;
val pow100 = fn: real -> real
```

Possibility to **decompose** the result with `val (a,b,c) = f (...)`

```ocaml
> fun split (nil) = (nil, nil)
   |  split (a::nil) = ([a], nil)
   |  split (a::b::cs) =
   		let
   		  val (M, N) = split (cs)
   		in
   		  (a::M, b::N)
   		end;
val split = fn: ’a list -> ’a list * ’a list
> split [1,2,3,4,5];
val it = ([1, 3, 5], [2, 4]): int list * int list
```

```ocaml
> fun mergeSort (nil) = nil  (* stoCazzo! *)
   |  mergeSort ([a]) = [a]
   |  mergeSort (L) =
        let
          val (M, N) = split L;
        in 
          merge (M, N)
        end;
val mergeSort = fn: int list -> int list
> mergeSort [1,4,2,3,8,7];
val it = [1, 2, 4, 3, 7, 8]: int list
```



## Input / output

- **Console output**

  - `print(x)` prints a **string** (type `unit`)

    ```ocaml
    > print;
    val it = fn: string -> unit
    ```

    ```ocaml
    > print ("420\n");
    420
    val it = (): unit
    > print (Real.toString(42.0));
    42.0val it = (): unit
    ```

  - **Compound statements** (type of the last statement)

    ```ocaml
    > ( print(str(#"A")); print(str(#"\n")); 1 );
    A
    val it = 1: int
    ```

- **File input**

  ```bash
  $ cat test
  12
  ab
  ```

  ```ocaml
  (* open the file (instream) *)
  > val infile = TextIO.openIn ("test");
  val infile = ?: TextIO.instream
  ```

  ```ocaml
  (* check end of stream / file *)
  > TextIO.endOfStream (infile);
  val it = false: bool
  (* read n char *)
  > TextIO.inputN (infile, 4);
  val it = "12\na": string
  > TextIO.inputN (infile, 1);
  val it = "b": string
  > TextIO.inputN (infile, 1);
  val it = "\n": string
  (* check end of stream / file *)
  > TextIO.endOfStream (infile);
  val it = true: bool
  ```

  ```ocaml
  (* read one line until #"\n" *)
  > TextIO.inputLine (infile);
  val it = SOME "12\n": string option
  > TextIO.inputLine (infile);
  val it = SOME "ab\n": string option
  > TextIO.inputLine (infile);
  val it = NONE: string option
  ```

  ```ocaml
  (* read complete file *)
  > val s = TextIO.input (infile);
  val s = "12\nab\n": string
  ```

  ```ocaml
  (* read single char *)
  > TextIO.input1 (infile);
  val it = SOME #"1": char option
  (* read next char and leave it in the input stream *)
  > TextIO.lookahead (infile);
  val it = SOME #"2": char option
  > TextIO.lookahead (infile);
  val it = SOME #"2": char option
  ```

  ```ocaml
  (* check if there are at least n char on instream *)
  > TextIO.canInput (infile,1);
  val it = SOME #1: int option
  > TextIO.canInput (infile,10);
  val it = SOME #6: int option
  ```

  ```ocaml
  (* close the file (instream) *)
  > TextIO.closeIn (infile);
  val it = (): unit
  ```
  
  **Summary**
  
  ```ocaml
  val file = TextIO.openIn("test");	(* TextIO.instream *)
  TextIO.endOfStream	(file);			(* bool *)
  TextIO.canInput		(file, 4);		(* int option *)
  TextIO.lookahead	(file);			(* char option *)
  TextIO.input1		(file);			(* char option *)
  TextIO.inputLine	(file);			(* string option *)
  TextIO.inputN		(file, 4);		(* string *)
  TextIO.input		(file);			(* string *)
  TextIO.closeIn		(file)			(* unit *)
  ```



## Exceptions

- **Built-in**

  ```ocaml
  > 5 div 0;
  Exception- Div raised
  > hd (nil: int list);
  Exception- Empty raised
  > chr (500);
  Exception- Chr raised
  ```

- **User defined**

  ```ocaml
  > exception Foo;
  exception Foo
  > raise Foo;
  Exception- Foo raised
  ```

  ```ocaml
  (* with parameters *)
  > exception Foo of string;
  exception Foo
  > raise Foo ("bar");
  Exception- Foo "bar" raised
  > raise Foo (5);
  poly: : error: Type error in function application.
  > raise Foo;
  poly: : error: Exception to be raised must have type exn.
  ```

- **Handling exceptions**

  ```ocaml
  > exception OutOfRange of int * int;
  > fun comb1 (n,m) =
      if n <= 0 then raise OutOfRange (n, m)
      else if m < 0 orelse m > n then raise OutOfRange (n, m)
      else if m = 0 orelse m = n then 1
      else comb1 (n-1, m) + comb1 (n-1, m-1);
  val comb1 = fn: int * int -> int
  > fun comb (n, m) = comb1 (n, m)
      handle OutOfRange (0,0) => 1
        |    OutOfRange (n,m) => ( print ("out of range: n=");
                                   print (Int.toString(n));
                                   print (" m=");
                                   print (Int.toString(m));
                                   print ("\n");
                                   0 );
  val comb = fn: int * int -> int
  > comb (4,2);
  val it = 6: int
  > comb (3,4);
  out of range: n=3 m=4
  val it = 0: int
  > comb (0,0);
  val it = 1: int
  ```



## Polymorphic functions

Functions which permits **multiple types**

ML is **strongly typed**: it must determine the type of any program **statically**

```ocaml
> fun identify (x) = x;
val identify = fn: 'a -> 'a
> identify (2);
val it = 2: int
> identify (2.0);
val it = 2.0: real
>  identify (ord);
val it = fn: char -> int
> identity (2) + floor (identity (3.5));
val it = 5: int
```

**Built in reversal**

```ocaml
> rev;
val it = fn: 'a list -> 'a list
> rev [1, 2, 4, 3, 7, 8];
val it = [8, 7, 3, 4, 2, 1]: int list
```



### Equality tests

**Testing for empty list**

- ```ocaml
  (* Accepts only lists of equality types *)
  > fun f(L) = if L = nil then nil else ...
  ```

- ```ocaml
  (* No equality tests *)
  > fun g(nil) = nil | g(L) = ...
  > fun h(L) = if null(L) then nil else ...
  ```



## Higher order functions

Functions that take **functions as arguments**

```ocaml
(* Integration *)
> fun trap (a, b, n, F) =
    if n <= 0 orelse b-a <= 0.0 then 0.0
    else
      let
      	val delta = (b-a) / real(n)
      in
        delta*(F(a)+F(a+delta))/2.0 + integ(a+delta,b,n-1,F)
      end;
val trap = fn: real * real * int * (real -> real) -> real
```



### Map

Built in `map(fn F, 'a list)`: take a function `F` and a list `[a1,..,an]` and produces the list `[F(a1),..,F(an)]`

```ocaml
> fun simpleMap (F,nil) = nil
   |  simpleMap (F,x::xs) = F(x) :: simpleMap (F,xs);
val simpleMap = fn: ('a -> 'b) * 'a list -> 'b list
```

Function `F` could be

- Previously declared (`fun F(x) = x*x;`)
- Unary operator (`~`)
- Anonymous function (`fn x => x*x`)



### Reduce

Returns a **single value** that is the application of a **function** on all the elements

<u>Definition</u>

- List `[a1]` returns `a1`
- List `[a1,..,an]` reduces tail with `F` obtaining `b`, then compute `F(a1,b)`
- Reducing by
  - **Addition**: sum of the elements
  - **Multiplication**: product of the elements
  - **AND**: true if all the elements are true
  - **max**: largest element
  - **Infix operators**: must convert to prefix with `op *`

```ocaml
> exception EmptyList;
exception EmptyList
> fun reduce (F,nil) = raise EmptyList
   |  reduce (F,[a]) = a
   |  reduce (F,x::xs) = F(x,reduce(F,xs));
val reduce = fn: ('a * 'a -> 'a) * 'a list -> 'a
> reduce (op +, [1,2,3]);
val it = 6: int
```



### Filter

**Select** those elements from a list that satisfy a **boolean condition**

```ocaml
> fun filter (P, nil) = nil
   |  filter (P,x::xs)=(if P(x) then [x] else [])@filter(P,xs);
val filter = fn: ('a -> bool) * 'a list -> 'a list
> filter (fn x => x>=10, [1,10,23,5,16]);
val it = [10, 23, 16]: int list
```



### Curried functions

Functions have only **one argument**

**Multiple arguments** can be

- **Tuple**

- **Curried function**

  - **Unary function** that takes argument `x`
  - The **result is a function** `f(x)` that takes argument `y`

```ocaml
> fun exponent1 (x,0) = 1.0
|  exponent1 (x,y) = x * exponent1 (x,y-1);
val exponent1 = fn: real * int -> real
> fun exponent2 x 0 = 1.0
|  exponent2 x y = x * exponent2 x (y-1);
val exponent1 = fn: real -> int -> real
> exponent1 (3.0,4);
val it = 81.0: real
> exponent2 3.0 4 ;
val it = 81.0: real
```

**Partial instantiation**

```ocaml
> val g = exponent2 3.0;
val g = fn: int -> real
> g 4;
val it = 81.0: real
> g (4);
val it = 81.0: real
```



### Built-in higher order functions

```ocaml
> fun F x = x+3;
val F = fn: int -> int
> fun G y = y*y + 2*y;
val G = fn: int -> int
```

- **Composition** of functions

  ```ocaml
  > fun comp (F,G,x) = G(F(x));
  val comp = fn: ('a -> 'b) * ('b -> 'c) * 'a -> 'c
  > comp (F, G, 10);
  val it = 195: int
  ```

- **Operator `o`**

  ```ocaml
  > val H = G o F;
  val H = fn: int -> int
  > H 3;
  val it = 48: int
  ```

- `o` like function

  ```ocaml
  > fun comp F G =
  	let
  	  fun H x = G(F(x));
  	in
  	  H
  	end;
  val comp = fn: ('a -> 'b) -> ('b -> 'c) -> 'a -> 'c
  > val H = comp F G;
  val H = fn: int -> int
  > H 10;
  val it = 195: int
  ```

- `map` with only one argument of `fn` type

  ```ocaml
  > fun map F =
  	let
  	  fun M nil = nil
  	   |  M (x::xs) = F x :: M xs;
  	in
  	  M
  	end;
  val map = fn: ('a -> 'b) -> 'a list -> 'b list
  > val square = map (fn x => x*x);
  val square = fn: int list -> int list
  > square [1,2,3];
  val it = [1, 4, 9]: int list
  ```



### Folding lists

ML provides two functions `foldr` and `foldl`

Given a list `L = [a1,..,an]`, it associate a function `F_ai` with `ai` and compose all these functions `F_a1 o ... o F_an`

The key step is going from `ai` to `F_ai`

<u>Definition</u> of `foldr` and `foldl`

```ocaml
> fun foldr F y nil = y
   |  foldr F y (x::xs) = F (x, foldr F y xs);
val foldr = fn: ('a * 'b -> 'b) -> 'b -> 'a list -> 'b
> fun foldl F y nil = y
   |  foldl F y (x::xs) = foldl F (F(x,y)) xs;
val foldl = fn: ('a * 'b -> 'b) -> 'b -> 'a list -> 'b
> fun F (a,x) = a*x;
val F = fn: int * int -> int
> foldr F 1 [2,3,4];
val it = 24: int
> fun F (a,x) = x+1;
val F = fn: 'a * int -> int
> foldr F 0 [1,2,3,4];
val it = 4: int
> val prod = foldr op * 1;
val prod = fn: int list -> int
> prod [2,3,4];
val it = 24: int
```



## User defined types

### Keyword types

**Abbreviations** that are equal to the specified type

  ```ocaml
> type newtype = int list;
type newtype = int list
> val v = [1,2];
val v = [1, 2]: int list
> val w = [1,2]: newtype;
val w = [1, 2]: newtype
> v = w;
val it = true: bool
  ```



### Parametrized type definitions

Given two types `'a` and `'b`, we declare `mapping` to be a type of **list of pairs of these two types**

```ocaml
> type ('c, 'd) mapping = ('c * 'd) list;
type ('a, 'b) mapping = ('a * 'b) list
> val words = [("in", 6), ("a", 1)]: (string, int) mapping;
val words = [("in", 6), ("a", 1)]: (string, int) mapping
```



### Datatypes

`datatype` creates **new types**, in two parts

- **Type constructor**: the name of datatype
- **Data constructor**: the possible values

```ocaml
> datatype fruit = Apple | Pear | Grape | Weed;
datatype frtuit = Apple | Pear | Grape | Weed
> fun isApple (x) = (x = Apple);
val isApple = fn: fruit -> bool
```

#### Constructor expressions

Very limited expressions like `Apple`, that can be parametrized

```ocaml
Banana of int  (* of/on ??? *)
Banana (23)
```

#### Unions

- **First** component: type `'a`
- **Second** component: type `'b`  (if it exists)

```ocaml
> datatype ('a, 'b) element = P of 'a * 'b | S of 'a;
datatype ('a, 'b) element = P of 'a * 'b | S of 'a
```

```ocaml
> P("a", 1);
val it = P ("a", 1): (string, int) element
> P(1.0, 2.0);
val it = P (1.0, 2.0): (real, real) element
> S(["a","b"]);
val it = S ["a", "b"]: (string list, 'a) element
> S(["a","b"], 2); 
val it = S (["a", "b"], 2): (string list * int, 'a) element
```

```ocaml
(* Given a list of (string,int), sum the int *)
> fun sum (nil) = 0
   |  sum (S(s)::L) = sum(L)
   |  sum (P(s,i)::L) = i + sum(L);
val sumElList = fn: ('a, int) element list -> int
> sumElList [ P("in",6), S("function"), P("as",2) ];
val it = 8: int
```

#### Recursive definition - Bynary tree

In a **binary tree** each **node** could

- Be empty
- Have two children, which are binary trees

```ocaml
> datatype 'label btree =
	Empty |
    Node of 'label * 'label btree * 'label btree;
datatype 'a btree = Empty | Node of 'a btree * 'a btree
```

```ocaml
> Node ("ML",
	Node ("as",
	  Node ("a",  Empty, Empty),
	  Node ("in", Empty, Empty)
	),
	Node ("types", Empty, Empty)
  );
val it =
   Node
    ("ML", Node ("as", Node ("a", Empty, Empty),
    Node ("in", Empty, Empty)),
     Node ("types", Empty, Empty)): string btree
```

#### Mutually recursive

Keyword `and` (as with functions)

 ```ocaml
> datatype
	'a etree =  (* even nodes from root to leaves *)
	  Empty |
	  Enode of 'a * 'a otree * 'a otree
  and
    'a otree =  (* odd nodes from root to leaves *)
	  Onode of 'a * 'a etree * 'a etree;
datatype 'a etree = Empty | Enode of 'a * 'a otree * 'a otree
datatype 'a otree = Onode of 'a * 'a etree * 'a etree
 ```

```ocaml
> val t1 = Onode (1,Empty,Empty);
val t1 = Onode (1, Empty, Empty): int oddTree
> val t2 = Onode (1,Empty,Empty);
val t2 = Onode (1, Empty, Empty): int oddTree
> val t3 = Enode (3,t1,t2);
val t3 = Enode (3, Onode (1, Empty, Empty),
		 Onode (1, Empty, Empty)): int evenTreenot visible
> val t4 = Onode (4,t3,Empty);
val t4 = Onode (4, Enode (3, Onode (1, Empty, Empty),
		 Onode (1, Empty, Empty)), Empty): int oddTree
```



## Signatures and structures

- **Structure**: sequence of declarations comprising components of structure
  - May be bound to a structure variable using a **structure binding**
  - Components are accessed using **long identifiers** or **paths**
- **Signature**: specify the type of the structure (similar to interface or class)

Relation between signatures and structure is **many-to-many**



### Structures

```ocaml
> structure IntLT = struct
	type t = int;
	val lt = (op <)
	val eq = (op =)
  end;
structure IntLT:
  sig val eq: ''a * ''a -> bool
  	  val lt: int * int -> bool
  	  eqtype t
  end
> structure IntDiv = struct
	type t = int;
	fun lt (m,n) = (n mod m = 0);
	val eq = (op =)
  end;
structure IntDiv:
  sig val eq: ''a * ''a -> bool
      val lt: int * int -> bool
      eqtype t
  end
```

#### Long identifiers

- **Referring** to functions

  ```ocaml
  > IntLT.lt;
  val it = fn: int * int -> bool
  > IntDiv.lt;
  val it = fn: int * int -> bool
  ```

- **Using** functions

  ```ocaml
  > IntLT.lt (3,4);
  val it = true: bool
  > IntDiv.lt (3,4);
  val it = false: bool
  ```



### Signatures

```ocaml
> signature ORDERED = sig
	type t
	val lt: t * t -> bool
	val eq: t * t -> bool
  end;
signature ORDERED = sig
  val eq: t * t -> bool
  val lt: t * t -> bool
  type t
end
```



## Data structures

### Queue

<u>Signature</u>

```ocaml
> signature QUEUE = sig
	type 'a queue
	exception QueueError
	val empty	  : 'a queue
	val isEmpty	  : 'a queue -> bool
	val singleton : 'a -> 'a queue
	val insert	  : 'a * 'a queue -> 'a queue
	val peek	  : 'a queue -> 'a
	val remove	  : 'a queue -> 'a * 'a queue
  end;
```

<u>Implementation</u>

The **declaration `:>`** specify that

- `TwoListQueue` is an **implementation** of the `QUEUE` signature
- Any type component not in the signature are **not visible** outside

```ocaml
> structure TwoListQueue :> QUEUE = struct
	type 'a queue = 'a list * 'a list
	exception QueueError
	val empty = ([],[])
	fun isEmpty ([],[]) = true
	 |  isEmpty _ = false
	fun singleton a = ([],[a])
	fun insert (a, ([],[])) = ([], [a])
	 |  insert (a, (ins, outs)) = (a::ins, outs)
	fun peek (_,[]) = raise QueueError
	 |  peek (ins, a::outs) = a
	fun remove (_,[]) = raise QueueError
	 |  remove (ins, [a]) = (a, ([], rev ins))
	 |  remove (ins, a::outs) = (a, (ins, outs))
  end;
structure TwoListQueue: QUEUE
```



### Stack

```ocaml
> datatype 'a option = NONE | SOME of 'a;
> signature STACK = sig
	type 'a stack
	val empty :	'a stack
	val push  : 'a * 'a stack -> 'a stack
	val pop   : 'a stack -> 'a option
  end;
> structure Stack = struct
	type 'a stack = 'a list
	val empty = []
	val push = op ::
	fun pop [] = NONE
	 |  pop (tos::rest) = SOME tos
  end :> STACK;
structure Stack: STACK
```

```ocaml
> val a = Stack.push (1, Stack.empty);
val a = ?: int Stack.stack
> val a = Stack.push (2, a); 
val a = ?: int Stack.stack
> Stack.pop (a);
val it = SOME 2: int option
```



### Bynary search tree

**Order** predicate `lt(x,y)` that is

- Transitive
- Total
- Irreflective

BST **property** for bynary labeled trees

- If `x` is the label of a node `n`, then for every label `y` in the
  - Left subtree of `n`, `lt(y,x)` holds
  - Right subtree of `n`, `lt(x,y)` holds

Order relation for **strings**

```ocaml
> fun strLT (x, y) =
	let
      fun lower (nil) = nil
       |  lower (c::cs) = (Char.toLower c) :: lower (cs);
    in
	  implode (lower (explode x)) < implode (lower (explode y))
	end;
val strLT = fn: string * string -> bool
```

**Lookup**

- Check if the tree **contains** a value

```ocaml
(* lookup <lt> <tree> <value>;                   *)
(* true if <value> is in <tree>, false otherwise *)
> fun lookup lt Empty x = false
   |  lookup lt (Node(y,sx,dx)) x = 
   		if lt(x,y) then lookup lt sx x else
   		if lt(y,x) then lookup lt dx x
   		else true;
val lookup = fn: ('a * 'a -> bool) -> 'a btree -> 'a -> bool
```

**Insertion**

- Creates a **new tree** with the element added
- **Recursive** insertion that at each step creates the appropriate subtree

```ocaml
> fun insert lt Empty x = Node (x, Empty, Empty)
   |  insert lt (T as Node(y,sx,dx)) x = 
   		if lt(x,y) then Node (y, insert lt sx x, dx) else
   		if lt(y,x) then Node (y, sx, insert lt dx x)
   		else T;
val insert =
  fn: ('a * 'a -> bool) -> 'a btree -> 'a -> 'a btree
> val t = insert lt Empty 4;
val t = Node (4, Empty, Empty): int btree
> val t = insert lt t 2;  
val t = Node (4, Node (2, Empty, Empty), Empty): int btree
```

**Deletion**

- Creates a **new tree** with the element removed
- Uses an **auxiliary** function `deletemin`
  - Input tree must be **nonempty**
  - **Returns**
    - The **smallest element** (left-most node)
    - A **new tree** without the smallest element
  - Order relation is not needed

```ocaml
> exception EmptyTree;
exception EmptyTree
> fun deletemin (Empty) = raise EmptyTree
   |  deletemin (Node (x, Empty, dx)) = (x, dx)
   |  deletemin (Node (x, sx, dx)) =
   		let val (y, S) = deletemin (sx);
   		in (y, Node (x, S, dx))
   		end;
val deletemin = fn: 'a btree -> 'a * 'a btree
> fun delete lt Empty x = Empty
   |  delete lt (T as Node (y, sx, dx)) x = 
   		if lt(x,y) then Node(y, delete lt sx x, dx) else
   		if lt(y,x) then Node(y, sx, delete lt dx x) else
   		  case (sx, dx) of
   		    (Empty, d) => d |
   		    (s, Empty) => s |
   		    (s, d) =>
   		      let val (z, d1) = deletemin (d)
   		      in Node (z, s, d1)
   		      end;
val delete = fn: ('a * 'a -> bool) -> 'a btree ->'a -> 'a btree
```



# [↑](#↓)