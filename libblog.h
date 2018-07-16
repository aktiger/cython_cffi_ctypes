#include <stdlib.h>
#include <math.h>
typedef struct s_point
{
  double x;
  double y;
} t_point;

typedef struct s_test
{
  char *sentence;
  int nb_points;
  t_point *points;
  double *distances;
} t_test;

char *increment_string(char *str, int n);
void generate_points(t_test *test, int nb);
void distance_between_points(t_test *test);
