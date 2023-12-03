#include <Python.h>
/**
 * print_python_list_info - prints some basic info about Python lists.
 * @p: PyObject
 */
void print_python_list_info(PyObject *p)
{
	long int size;
	int i;
	PyListObject *list;
	PyObject *obj;

	size = Py_SIZE(p);
	obj = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", obj);
	for (i = 0; i < size; i++)
	{
		obl = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(obj)->tp_name);


