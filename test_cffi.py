from cffi import FFI
ffi = FFI()

ffi.cdef(
"""
typedef struct t_point t_point;
struct t_point 
{
  double x;
  double y;
};

typedef struct t_test t_test;

struct t_test {
  char *sentence;
  int  nb_points;
  t_point *points;
  double *distances;
}; 

char * increment_string(char *str, int n);
void generate_points(t_test * test, int nb);
void distance_between_points(t_test *test);

""")

if __name__ == '__main__':
    # Load C shared libray
    lib = ffi.dlopen('./libblog.so')

    # Declare the C structure
    test = ffi.new("struct t_test *")
    test.sentence = ffi.new("char[]", "A nice sentenc to test.".encode("utf-8"))
    test.nb_points = 0
    test.points = ffi.NULL
    test.distances = ffi.NULL

    #Call C functions
    lib.generate_points(test, 10000)
    test.sentence = lib.increment_string(test.sentence, 1)
    lib.distance_between_points(test)



