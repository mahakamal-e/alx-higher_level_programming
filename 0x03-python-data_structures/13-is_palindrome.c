#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * is_palindrome - function that used to check is palindrome
 * A palindrome is a sequence of elements that reads
 * the same forwards as backward
 *
 * @head: head of linkedlist
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow_ptr, *fast_ptr, *prev_ptr, *temp;
	slow_ptr = *head;
	fast_ptr = *head;
	prev_ptr = NULL;

	if (!head || !*head || !(*head)->next)
		return (1);
	while (fast_ptr && fast_ptr->next)
	{
		fast_ptr = fast_ptr->next->next;
		temp = slow_ptr->next;
		slow_ptr->next = prev_ptr;
		prev_ptr = slow_ptr;
		slow_ptr = temp;
	}
	if (fast_ptr)
		slow_ptr = slow_ptr->next;
	while (prev_ptr && slow_ptr)
	{
		if (prev_ptr->n != slow_ptr->n)
			return (0);
		prev_ptr = prev_ptr->next;
		slow_ptr = slow_ptr->next;
	}
	return (1);
}
