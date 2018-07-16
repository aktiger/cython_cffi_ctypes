#include "libblog.h"

char *increment_string(char *str, int n)
{
  for(int i = 0; str[i]; i++) {
    str[i] = str[i] + n;
  }
  return (str);
}

void generate_points(t_test *test, int nb) {
  t_point *points = (t_point*)calloc(nb+1, sizeof(t_point));
  for(int i = 0; i < nb; i++) {
    points[i].x = rand();
    points[i].y = rand();
      
  }
  test->points = points;
  test->nb_points = nb;
}

void distance_between_points(t_test *test)
{
  int nb = test->nb_points;
  double *distances = (double *)calloc(nb * nb + 1, sizeof(double));

  for(int i=0; i < nb; i++){
    for(int j=0; j < nb; j++) {
      distances[i * nb + j] = sqrt((test->points[j].x - test->points[i].x) * (test->points[j].x - test->points[i].x) + (test->points[j].y - test->points[i].y) * (test->points[j].y - test->points[i].y));
    }
  }
  test->distances = distances;
}
