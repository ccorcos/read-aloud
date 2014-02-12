#!/usr/bin/env python
# -*- coding: utf-8 -*- 

text = u"""

Smoothing and Mapping or SAM
A smoothing approach to SLAM involves not just the most current robot location, but the entire robot trajectory up to the current time. A number of authors considered the problem of smoothing the robot trajectory only [9, 56, 57, 40, 46, 24], which is particularly suited to sensors such as laser- range finders that easily yield pairwise constraints between nearby robot poses. More generally, one can consider the full SLAM problem [77], i.e., the problem of optimally estimating the entire set of sensor poses along with the parameters of all features in the environment. In fact, this problem has a long history in surveying [36], photogrammetry [7, 37, 68, 10], where it is known as “bundle adjustment”, and computer vision [25, 72, 73, 79, 41], where it is referred to as “structure from motion”. Especially in the last five years there has been a flurry of work where these ideas were applied in the context of SLAM [16, 22, 23, 43, 30, 31, 26, 27, 28, 29, 77].
In this paper we show how smoothing can be a very fast alternative to filtering-based methods,
and that in many cases keeping the trajectory around helps rather than hurts performance. In
particular, the optimization problem associated with full SLAM can be concisely stated in terms
of sparse linear algebra, which is traditionally concerned with the solution of large least-squares
problems [35]. In this framework, we investigate factorizing either the information matrix I or
the measurement Jacobian A into square root form, as applied to the problem of simultaneous
smoothing and mapping (SAM). Because they are based on matrix square roots, we will refer to
this family of approaches as square root SAM, or
√
￼√
SAM for short, first introduced in [18]. We SAM is a fundamentally better approach to the problem of SLAM than the EKF,
￼propose that
based on the realization that,
• in contrast to the extended Kalman filter covariance or information matrix, which both be- come fully dense over time [65, 78], the information matrix I associated with smoothing is and stays sparse;
• in typical mapping scenarios (ie. not repeatedly traversing a small environment) this matrix I or, alternatively, the measurement Jacobian A, are much more compact representations of the map covariance structure
• I or A, both sparse, can be factorized efficiently using sparse Cholesky or QR factorization, respectively, yielding a square root information matrix R that can be used to immediately obtain the optimal robot trajectory and map;
Factoring the information matrix is known in the sequential estimation literature as square root information filtering (SRIF), and was developed in 1969 for use in JPL’s Mariner 10 missions to Venus (as recounted by [3]). The use of square roots of either the covariance or information matrix results in more accurate and stable algorithms, and, quoting Maybeck [59] “a number of
2 SLAM AND ITS GRAPHS 3
practitioners have argued, with considerable logic, that square root filters should always be adopted in preference to the standard Kalman filter recursion”. Maybeck briefly discusses the SRIF in a chapter on square root filtering, and it and other square root type algorithms are the subject of a book by Bierman [3]. However, as far as this can be judged by the small number of references in the literature, the SRIF and the square root information smoother (SRIS) are not often used.

"""

import re

p = re.compile(r'\s\[[0-9 ,]*\]')

# remove paper references
while 1:
	if (p.search(text)):
		text = p.sub('',text)
	else:
		break

p = re.compile('[^\x00-\x7F]+')

# remove unicode
while 1:
	if (p.search(text)):
		text = p.sub('',text)
	else:
		break

p = re.compile(r'\n[0-9]+[A-Za-z0-9 _,]+[0-9]+\n')

# remove page titles/footers
while 1:
	if (p.search(text)):
		text = p.sub(' ',text)
	else:
		break


import os

print "say -i -r 250 "+text
os.system("say -i -r 200 \""+text+"\"")

# print repr(text)

