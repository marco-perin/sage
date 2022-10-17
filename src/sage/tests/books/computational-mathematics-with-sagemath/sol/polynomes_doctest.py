## -*- encoding: utf-8 -*-
"""
This file (./sol/polynomes_doctest.sage) was *autogenerated* from ./sol/polynomes.tex,
with sagetex.sty version 2011/05/27 v2.3.1.
It contains the contents of all the sageexample environments from this file.
You should be able to doctest this file with:
sage -t ./sol/polynomes_doctest.sage
It is always safe to delete this file; it is not used in typesetting your
document.

Sage example in ./sol/polynomes.tex, line 10::

  sage: x = polygen(QQ, 'y'); y = polygen(QQ, 'x')

Sage example in ./sol/polynomes.tex, line 78::

  sage: T = sage.symbolic.function_factory.function('T', nargs=2)
  sage: def to_chebyshev_basis(pol):
  ....:     (x,) = pol.variables()
  ....:     res = 0
  ....:     for n in range(pol.degree(), -1, -1):
  ....:         quo, pol = pol.quo_rem(chebyshev_T(n, x))
  ....:         res += quo * T(n, x)
  ....:     return res

Sage example in ./sol/polynomes.tex, line 105::

  sage: x = polygen(QQ)
  sage: p = 4*x^6 + 4*x^5 + 1/9*x^4 - 2*x^3 + 2/19*x^2 + 1
  sage: p_cheb = to_chebyshev_basis(p); p_cheb
  1/8*T(6, x) + 1/4*T(5, x) + 55/72*T(4, x) + 3/4*T(3, x) +
  2713/1368*T(2, x) + T(1, x) + 1069/456*T(0, x)
  sage: p_cheb.substitute_function(T, chebyshev_T).expand()
  4*x^6 + 4*x^5 + 1/9*x^4 - 2*x^3 + 2/19*x^2 + 1

Sage example in ./sol/polynomes.tex, line 131::

  sage: def mydiv(u, v, n):
  ....:     v0 = v.constant_coefficient()
  ....:     quo = 0; rem = u
  ....:     for k in range(n+1):
  ....:         c = rem[0]/v0
  ....:         rem = (rem - c*v) >> 1  # shifting the coefficients
  ....:         quo += c*x^k
  ....:     return quo, rem

Sage example in ./sol/polynomes.tex, line 161::

  sage: def mydiv2(u, v, n):
  ....:     x = u.parent().gen()
  ....:     quo = (u / (v + O(x^(n+1)))).polynomial()
  ....:     rem = (u - quo*v) >> (n+1)
  ....:     return quo, rem

Sage example in ./sol/polynomes.tex, line 179::

  sage: x = polygen(QQ)
  sage: u = -5*x^10 + 7/2*x^9 + 3*x^8 - x^6 - 1/3*x^5 - x^4 - 1/2*x^3 + 15*x^2 - 1/42*x + 2
  sage: v = 3*x^4 + 3/8*x^3 - 1/2*x^2 + x + 5/2
  sage: n = 8
  sage: q, r = mydiv(u, v, n)
  sage: u - q*v - x^(n+1)*r
  0
  sage: q, r = mydiv2(u, v, n)
  sage: u - q*v - x^(n+1)*r
  0

Sage example in ./sol/polynomes.tex, line 296::

  sage: Poly.<x> = Integers(10^5)[]
  sage: P = x^1000 - 23*x^729 + 5*x^2 - 12*x - 7
  sage: Quo.<s> = Poly.quo(P)
  sage: op = s^(10^10000)  # long time
  sage: add(op[n]*(n+7) for n in range(1000))  # long time
  63477

Sage example in ./sol/polynomes.tex, line 383::

  sage: from sage.matrix.berlekamp_massey import berlekamp_massey
  sage: berlekamp_massey([1, 1, 2, 3, 8, 11, 34, 39, 148, 127])
  x^3 - 5*x + 2

Sage example in ./sol/polynomes.tex, line 408::

  sage: R.<x> = GF(17)[]
  sage: pairs = [(0,-1), (1,0), (2,7), (3,5)]
  sage: s = R(QQ['x'].lagrange_polynomial(pairs)); s
  6*x^3 + 2*x^2 + 10*x + 16
  sage: [s(i) for i in range(4)]
  [16, 0, 7, 5]

Sage example in ./sol/polynomes.tex, line 428::

  sage: s.rational_reconstruction(mul(x-i for i in range(4)), 1, 2)
  (15*x + 2, x^2 + 11*x + 15)

Sage example in ./sol/polynomes.tex, line 454::

  sage: S.<x> = PowerSeriesRing(QQ)
  sage: t = S(0)
  sage: for i in range(7): # here t is correct up to degree 2i+1
  ....:     # with O(x^15) we prevent the truncation order to grow
  ....:     t = (1+t^2).integral() + O(x^15)
  sage: t
  x + 1/3*x^3 + 2/15*x^5 + 17/315*x^7 + 62/2835*x^9 + 1382/155925*x^11
  + 21844/6081075*x^13 + O(x^15)

"""
