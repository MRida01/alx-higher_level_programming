#include <Python.h>

/**
 * print_python_list_info - prints info about the python lists
 * @p: PyObject list
 */
void print_python_list_info(PyObject *p)
{
  int size, alloc, n;
  PyObject *obj;

  size = Py_Size(p);
  alloc =((PyListObject *)p)->allocated;

  printf("[*] Size of the Python List = %d'\n", size);
  printf("[*] Allocated = %d\n", alloc);

  for (n = 0; n < size; n++)
    {
      printf("Element %d: ", n);

      obj = PyList_GetItem(p, n);
      printf("%s\n", Py_TYPE(obj)->tp_name);
    }
}
