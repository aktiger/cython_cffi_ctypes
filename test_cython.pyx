import cython
import random

from libc.stdlib cimport calloc, free
from libc.math cimport sqrt

#Import C structures and functions from the C header

cdef extern from "libblog.h":
  ctypedef struct t_point:
    double x
    double y


ctypedef struct t_test:
  char *sentence
  int nb_points
  t_point *points
  double *distances

# C function written in python syntax
cdef char *increment_string(char *str, int n):
  cdef int i = 0

  while str[i]:
      str[i] = str[i] + n
      i += 1
  return str


cdef void generate_points(t_test * test, int nb):
  cdef t_point *points = <t_point*> calloc(nb+1, sizeof(t_point))

  for i in range(nb):
      points[i].x = random.random()
      points[i].y = random.random()
  test.points = points
  test.nb_points = nb


cdef void distance_between_points(t_test *test):
  cdef int nb = test.nb_points
  cdef double *distances = <double*> calloc(nb * nb + 1, sizeof(double))
  cdef int i;
  cdef int j;

  for i from 0 <= i < nb:
    for j from 0 <= j < nb:
      distances[i * nb + j] = sqrt((test.points[j].x - test.points[i].x) * (test.points[j].x - test.points[i].x) + (test.points[j].y - test.points[i].y) * (test.points[j].y - test.points[i].y))
  test.distances = distances


def test():
   # Declare the sructrue and set the values
     cdef t_test test

     py_sentence = "A nice sentence to test.".encode('utf-8')
     test.sentence = py_sentence
     test.nb_points = 0
     test.points = NULL
     test.distances = NULL
     # Call C functions written in python
     generate_points(&test, 10000)
     test.sentence = increment_string(test.sentence, 1)
     distance_between_points(&test)

     # Call C function free
     free(test.points)
     free(test.distances)













