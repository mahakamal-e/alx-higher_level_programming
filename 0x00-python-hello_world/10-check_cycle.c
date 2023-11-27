#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * check_cycle - a function that used to check
 * if a singly linked list has a cycle in it.
 *
 * @list: linked list that it be checked pointer to list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow_ptr;
	listint_t *fast_ptr;

	slow_ptr = list;
	fast_ptr = list;

	while (slow_ptr != NULL && fast_ptr->next && fast_ptr != NULL)
	{
		slow_ptr = slow_ptr->next;
		fast_ptr = fast_ptr->next->next;

		if (slow_ptr == fast_ptr)
		{
			return (1);
		}
	}
	return (0);
}
