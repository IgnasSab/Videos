= Introduction

Welcome back! In our last video, we explored the creation of natural numbers and their operations like addition and multiplication. Today, we will take a step further and delve into the world of integers. To be perfectly clear, we will talk about numbers that very much resemble natural ones, that we described in the previous video, but with a negative counterpart. We will see how integers can be constructed using natural numbers as building blocks, and explore explore their addition, subtraction, and multiplication. 

= Cartesian Product

Before we delve into the actual material, I would like to introduce some definitions first. We will introduce a set operation called cartesian product. It is defined as follows: Given two sets A and B, the cartesian product of A and B is the set of all ordered pairs $(a, b)$ (ordered here means that $(a, b) != (b, a)$) where a is an element of A and b is an element of B. So for example, if $A = {1, 2}$ and $B = {3, 4}$, then the cartesian product of A and B is the set of all ordered pairs $(a, b)$ where $a$ is in $A$ and $b$ is in $B$, which is equal to 

$

 A times B = {(1, 3), (1, 4), (2, 3), (2, 4)}.

$


= Relations

To understand integers, we first need to understand the concept of relations. A relation $R$ on a set $A$ is a subset of the Cartesian product $A times A$. In simpler terms, a relation is a way of pairing elements of a set with each other.  Take $A = {1, 2 , 3}$ then 

$ 
  
  A times A = {(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)}
  
$

And a relation $R subset.eq A times A$ could be the set 

$
  
  R = {(1, 1), (1, 2), (2, 1), (2, 2), (3, 3)}
  
$

This relation pairs the elements of $A$ in a specific way. For example, $(1, 1)$ and $(2, 1)$ are in $R$, but $(1, 3)$ is not. To remove the abstraction a little bit, we could say that $1$ is related to $2$ and $2$ is related to $1$, but $1$ is not related to $3$. 

A more concrete example would be the following relation on the set $A$:

$  
  R = {(1, 1), (2, 2), (3, 3)}
$

When defining relations we can call (the squigly sign) $~$ to mean that that "ils related to" so $a ~ b$ means that $a$ is related to $b$. In this case, $a ~ b$ if $a$ is a number identical to $b$, in other words. We usually call this relation the identity relation and denote it as $=$ instead of $~$. So that $1 = 1, 2 = 2, 3 = 3$. 

Relations don't have to be defined in terms of numbers, we can have a mathematical model of relations between people and other objects. It is a very powerful tool that can be used to model many different things. But for now, we will stick to numbers.

#underline("Notes:") 
- Provide an example of a relation not between numbers in the background after reading the last text
- Remind them of what is a subet

= Equivalence Relations

Now, we will take a look into a specific type of relation that will be used later. An equivalence relation is a relation that is reflexive, symmetric, and transitive. In other words, it satisfies the following properties:

- Reflexive: For all $a$ in $A$, $(a, a)$ is in $R$.
- Symmetric: For all $a, b$ in $A$, if $(a, b)$ is in $R$, then $(b, a)$ is in $R$.
- transitive: For all $a, b, c$ in $A$, if $(a, b)$ is in $R$ and $(b, c)$ is in $R$, then $(a, c)$ is in $R$.

Take a look at an example: let ste $A = {1, 2, 3, 4, 5}$ and relation $R subset.eq A times A$ to be the set of all pairs $(a, b)$ such that $a + b$ is even, in more mathematical terms we define $~$ to be $a ~ b arrow.l.r.double a + b "is even"$. For example, $(1, 1)$ is in $R$ because $1 + 1 = 2$ is even. There are more ordered pairs that satisfy the condition and these are listed here: ${(1, 1), (1, 3), (1, 5), (2, 2), (2, 4) (3, 1), (3, 3), (3, 5) (4, 2), (4, 4), (5, 1), (5, 3), (5, 5)}$. 
- This relation is reflexive because for all $a$ in $A$, $a + a$ is even. (We can see that $1 + 1$, $2 + 2$, and $3 + 3$ are all even.)
- It is symmetric because if $(a, b)$ is in $R$, then $a + b$ is even, so $b + a$ is also even. (We can see that $1 + 3$ and $3 + 1$ are both even.) 
- It is transitive because if $(a, b)$ and $(b, c)$ are in $R$, then $a + b$ and $b + c$ are even, so $a + c$ is also even. For example, since $(1, 3), (3, 5)$ are in $R$, $(1, 5)$ is also in $R$ as desired.

One property that equivalence classes have is that they partition the set $A$ into disjoint subsets, which we will not prove here. This means that each element of $A$ belongs to exactly one equivalence class. We define the equivalence class $[a]$ of element $a$ to be the following set:

$
  [a] = {b in A | a ~ b}  
$

So it contains all the elements to which a is equivalent.
In our example, the equivalence classes are 
$
[1] &= {1, 3, 5} \
[2] &= {2, 4}

$
where $[1]$ represents the equivalence class of $1$ and $[2]$ represents the equivalence class of $2$. In this particular example, we can say that the relation $~$ partitions the set $A$ into even and odd numbers.

#underline("Notes:") The numbers in the equivalence classes are equal to each other in the sense of the relation $~$ and they are thus equivalent to each other and not distinguishable, we should look at the as the same

= Creating Integers

Now that we understand relations, let's move on to creating integers. Integers can be defined as equivalence classes of pairs of ordered pairs natural numbers $(a, b)$. What it means is that we instead of having a relation between two numbers as before, we will have relation between two pairs of numbers, lets say $(a, b)$ and $(c, d)$, which will represent two integers. The intuition behind is that the integer represented by $(a, b)$ is $a - b$, but we don't have subtraction, so we need to define it in terms of addition. 

We set the ordered pairs of number $(a, b)$ and $(c, d)$, which represent our integers, to be equivalent if $a + d = b + c$, so $(a, b) ~ (c, d) arrow.l.r.double a + d = b + c$. In other words, if we allow for subtraction, we can see that $(a, b)$ and $(c, d)$ represent the same integer if $a - b = c - d$. Where, as mentioned before, $a - b$ and $c - d$ are integers. Since equivalence classes partition the set of pairs of natural numbers, we can define the set of integers as the set of all equivalence classes of pairs of natural numbers as follows:

$
  ZZ &= {[(a, b)] | a, b in NN}, \
   &"where" \ 
  [(a, b)] &= {(c, d) in NN times NN | a + d = b + c}
$

Lets unpack it for a bit. The set $ZZ$ is the set of all integers, and each element of $ZZ$ is an equivalence class of pairs of natural numbers. The equivalence class $[(a, b)]$ is the set of all pairs $(c, d)$ such that $a + d = b + c$. This means that $[(a, b)]$ virtually represents the integer $a - b$. 

Take equivalence class $[(3, 1)]$ for example, it is equal to the following set:

$
  
  [(3, 1)] = {(2, 0), (3, 1), (4, 2), (5, 3), (6, 4), dots}  

$

and represents the integer $3 - 1 = 2$.

Now, take a look at the equivalence class $[(1, 3)]$, it is equal to the following set:

$
  
  [(1, 3)] = {(0, 2), (1, 3), (2, 4), (3, 5), (4, 6), dots}
  
$

and represents the integer $1 - 3 = -2$.

We will occasionally use a simpler notation to represent integers, for example the equivalence class $[(a, b)]$ will represent the integer $overline(a - b)$ and we use the overline to distinguish integers from natural numbers. As an example, we could have $[(2, 5)] = overline(-3)$

#underline("Notes:") We don't have subtraction yet as we didn't define it for natural number, and whenever I use the negative sign, like $a - b$ it means that $a = b + c$ for $c = a - b$.  

= Adding and Subtracting Integers

With our definition of integers in place, we can now explore how to add and subtract them. 

- *Addition*: To add two integers represented by pairs of natural numbers, we simply add the corresponding components of the pairs. For example, $[(a, b)] + [(c, d)] = [(a + c, b + d)]$.

Consider adding $[(1, 2)]$ and $[(3, 5)]$:

$ 

  [(1, 2)] + [(3, 5)] = [(1 + 3, 2 + 5)] = [(4, 7)]

$

which represents the integer addition $overline(-1) + overline(-2) = overline(-3)$.

- *Subtraction*: To subtract one integer from another, we add the first integer to the negation of the second. For example, $[(a, b)] - [(c, d)] = [(a + d, b + c)]$.

Consider subtracting $[(1, 2)]$ from $[(3, 5)]$:

$ 

  [(3, 5)] - [(1, 2)] = [(3 + 2, 5 + 1)] = [(5, 6)]

$

which represents the integer subtraction $overline(-2) - overline(-1) = overline(-1)$.

- *Multiplication*: To multiply two integers, we multiply the corresponding components of the pairs and add the cross products. For example, $[(a, b)] dot [(c, d)] = [(a dot c + b dot d, a dot d + b dot c)]$. This definition is pretty abstract at first look, but if we look at an example the definition should become a little bit more intuitive. 
Consider multiplying $[(1, 2)] dot [(3, 5)]$:

$

  [(1, 2)] dot [(3, 5)] = [(1 dot 3 + 2 dot 5, 1 dot 5 + 2 dot 3)] = [(3 + 10, 5 + 6)] = [(13, 11)]

$ 

Here, the class $[(1, 2)]$ represents the number $overline(-1)$ and $[(3, 5)]$ represents the number $overline(-2)$, so the result of the multiplication is $overline(2)$ which conforms to our intuition and how we were taught, since $overline(-1) dot overline(-2)$ is indeed $overline(2)$.

#underline("Notes:"):
- Keep in mind that we use the multiplication of natural numbers here in each of the equivalence classes

= Conclusion

In this video, we explored the concept of relations and a special type of it, called an equivalence relation. We used the later to define integers as equivalence classes of pairs of natural numbers. We then looked at how to perform addition and subtraction and finally multiplication. There are lost of other properties to consider that come straight out of the construction of integers as we did, but we will leave that for another time.

*Addition:* \ 
Associativity: $a + (b + c) = (a + b) + c$ \
Commutativity: $a + b = b + a$ \
Identity: $a + 0 = a$ \
Inverse: $a + (-a) = 0$ \
*Multiplication:* \
Associativity: $a dot (b dot c) = (a dot b) dot c$ \
Commutativity: $a dot b = b dot a$ \
Identity: $a dot 1 = a$ \

Distributivity: $a dot (b + c) = a dot b + a dot c$ \ 
