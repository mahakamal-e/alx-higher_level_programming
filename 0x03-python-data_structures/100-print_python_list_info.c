#include <Python.h>
/**
 * print_python_list_info - prints some basic info about Python lists.
 * @p: PyObject
 */
void print_python_list_info(PyObject *p)
{
	int _size;
	int i;
	int c;
	PyObject *obj;

	_size = PyList_Size(p);
	c = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", _size);
	printf("[*] Allocated = %d\n", c);
	for (i = 0; i < _size; i++)
	{
		obj = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(obj)->tp_name);
	}
}
