all: libblog.so test_cython.so
.PHONY:all

libblog.so:
	gcc -fPIC -g -O3 -shared -o libblog.so libblog.c 
test_cython.so:
	python cython_setup.py build; cp -f build/**/test_cython.so ./
clean:
	rm -fr ./libblog.so ./test_cython.so build/**/*.so build/**/*.o *.pyc 
test:
	@echo "cython_time is:----------------------"
	time -p python test_cython.py
	@echo "cffi time is:------------------------"
	time -p python test_cffi.py;
	@echo "ctyes time is:-----------------------"
	time -p python test_ctypes.py;
	@echo "pure python time is:-----------------"
	time -p python python_point.py
